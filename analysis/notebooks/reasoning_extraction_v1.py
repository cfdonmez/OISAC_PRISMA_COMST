"""
Stage 2: Reasoning Extraction for O-ISAC Survey
================================================
This module performs deep reasoning extraction to capture the "WHY" and "HOW"
behind paper contributions, complementing Stage 1 structured extraction.

Purpose:
- Extract problem-solution chains
- Identify differentiators from prior work  
- Generate survey-ready narrative sentences
- Localize where the novelty lies

Usage:
    from reasoning_extraction_v1 import extract_reasoning, run_reasoning_pipeline
    
    # Single paper
    result = extract_reasoning("O_ISAC_029")
    
    # All papers
    results = run_reasoning_pipeline()
"""

import os
import json
import asyncio
from datetime import datetime
from pathlib import Path

# ============================================================
# CONFIGURATION
# ============================================================

class ReasoningConfig:
    """Configuration for Stage 2 Reasoning Extraction"""
    
    # Paths (will be set for Colab)
    PROJECT_ROOT = "/content/drive/MyDrive/AKU_WorkSpace/survey_fdgit/OISAC_PRISMA_COMST"
    MARKDOWN_DIR = os.path.join(PROJECT_ROOT, "data/processed_markdowns")
    STAGE1_RESULTS = os.path.join(PROJECT_ROOT, "data/extraction_results_v3/extraction_v3.json")
    OUTPUT_DIR = os.path.join(PROJECT_ROOT, "data/extraction_results_v3")
    OUTPUT_FILE = os.path.join(OUTPUT_DIR, "reasoning_extraction_v1.json")
    
    # Model settings
    MODEL = "llama-3.3-70b-versatile"
    MAX_TOKENS = 4000
    TEMPERATURE = 0.1

# ============================================================
# REASONING PROMPT
# ============================================================

REASONING_PROMPT = """You are an expert technical reviewer analyzing an Optical Integrated Sensing and Communication (O-ISAC) paper for a PRISMA-2020 systematic review survey.

Your task is to perform DEEP REASONING extraction - focusing on the "WHY" and "HOW" behind the contribution, not just metrics.

================================================================================
ANALYSIS FRAMEWORK
================================================================================

Analyze the paper through these lenses:

1. PRIOR LIMITATION
   - What specific technical problem/gap existed in prior approaches?
   - Be specific: "Electronic mixers limit bandwidth" not "There were limitations"

2. PROPOSED SOLUTION  
   - How does THIS paper solve the identified problem?
   - Focus on the mechanism, not just the result

3. WHY IT WORKS
   - What is the technical principle that enables the solution?
   - This should explain the physics/engineering insight

4. DIFFERENTIATOR
   - How is this quantitatively/qualitatively better than baselines?
   - Reference any comparison tables in the paper

5. NOVELTY LOCALIZATION
   - Where exactly is the novelty? (architecture / component / algorithm / integration / application)
   - Be precise about what is new vs. what is reused

6. SURVEY SENTENCE
   - Write ONE sentence that could appear in a survey paper
   - Format: "[Author] et al. demonstrated that [key insight] by [method], achieving [result]"

================================================================================
OUTPUT FORMAT (JSON)
================================================================================

{
  "paper_id": "O_ISAC_XXX",
  
  "prior_limitation": {
    "problem": "1-2 sentence description of the gap/problem",
    "affected_metric": "which metric was limited (bandwidth, resolution, range, etc.)",
    "prior_approach": "what approach was used before"
  },
  
  "proposed_solution": {
    "approach": "1-2 sentence description of the solution",
    "key_component": "the main technical element enabling the solution",
    "mechanism": "HOW the solution works (technical principle)"
  },
  
  "why_it_works": {
    "technical_principle": "The physics/engineering insight",
    "enabling_factor": "What property of the component/method enables this"
  },
  
  "differentiator": {
    "baseline": "What this paper compares against",
    "improvement": "Quantitative improvement (e.g., '2x better resolution')",
    "unique_capability": "Something this approach can do that others cannot"
  },
  
  "novelty": {
    "type": "architecture | component | algorithm | integration | application | multiple",
    "location": "Where exactly the novelty lies",
    "first_demonstration": "Is this the first time X is demonstrated? (yes/no/unclear)"
  },
  
  "survey_sentence": "One publication-ready sentence for the survey",
  
  "taxonomy_position": {
    "primary_category": "e.g., Photonic THz ISAC",
    "sub_category": "e.g., Full-photonic reception",
    "distinguishing_feature": "e.g., Fiber-integrated with TFLN-MZM"
  },
  
  "limitations_noted": ["List any limitations the authors acknowledge"],
  
  "future_directions": ["What do the authors suggest for future work?"]
}

================================================================================
IMPORTANT GUIDELINES
================================================================================

- Focus on INSIGHT, not just description
- Be SPECIFIC, avoid generic statements
- Quote exact numbers when discussing improvements
- If information is not available, use "not_specified"
- The survey_sentence should be directly usable in a publication

================================================================================
PAPER CONTENT
================================================================================

"""

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_api_key():
    """Get Groq API key from Colab secrets or environment"""
    try:
        from google.colab import userdata
        return userdata.get('GROQ_API_KEY')
    except:
        import os
        key = os.environ.get('GROQ_API_KEY')
        if key:
            return key
        raise RuntimeError("GROQ_API_KEY not found!")


def load_markdown(paper_id: str) -> str:
    """Load markdown content for a paper"""
    md_path = os.path.join(
        ReasoningConfig.MARKDOWN_DIR,
        paper_id, paper_id, f"{paper_id}.md"
    )
    
    if os.path.exists(md_path):
        with open(md_path, 'r', encoding='utf-8') as f:
            return f.read()
    return ""


def load_stage1_results() -> dict:
    """Load Stage 1 extraction results"""
    if os.path.exists(ReasoningConfig.STAGE1_RESULTS):
        with open(ReasoningConfig.STAGE1_RESULTS, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return {p['Paper_ID']: p for p in data}
    return {}


def parse_json_response(response_text: str) -> dict:
    """Extract JSON from LLM response"""
    try:
        # Try to find JSON block
        if "```json" in response_text:
            json_str = response_text.split("```json")[1].split("```")[0]
        elif "```" in response_text:
            json_str = response_text.split("```")[1].split("```")[0]
        else:
            json_str = response_text
        
        return json.loads(json_str.strip())
    except json.JSONDecodeError as e:
        return {"error": f"JSON parse error: {str(e)}", "raw_response": response_text[:2000]}

# ============================================================
# MAIN EXTRACTION FUNCTION
# ============================================================

def extract_reasoning(paper_id: str, verbose: bool = True) -> dict:
    """
    Extract reasoning/insights from a single paper.
    
    Args:
        paper_id: Paper ID (e.g., "O_ISAC_029")
        verbose: Print progress messages
        
    Returns:
        Dictionary with reasoning extraction results
    """
    from groq import Groq
    
    if verbose:
        print(f"\n{'='*70}")
        print(f"🧠 REASONING EXTRACTION: {paper_id}")
        print('='*70)
    
    # Load markdown
    markdown = load_markdown(paper_id)
    if not markdown:
        return {"paper_id": paper_id, "error": "Markdown not found"}
    
    if verbose:
        print(f"📄 Loaded markdown: {len(markdown):,} chars")
    
    # Load Stage 1 results for context
    stage1_results = load_stage1_results()
    stage1_data = stage1_results.get(paper_id, {})
    
    # Build context
    context = f"Paper ID: {paper_id}\n\n"
    
    # Add Stage 1 summary if available
    if stage1_data:
        study = stage1_data.get('Study_Level', {})
        context += f"Title: {study.get('title', 'N/A')}\n"
        context += f"Key Contribution (Stage 1): {study.get('key_contribution', 'N/A')}\n"
        context += f"Gap Addressed (Stage 1): {study.get('gap_addressed', 'N/A')}\n"
        context += f"Medium Class: {study.get('oisac_medium_class', 'N/A')}\n\n"
    
    # Truncate markdown if too long (keep abstract + intro + conclusion)
    if len(markdown) > 50000:
        # Keep first 25K (abstract, intro) and last 15K (results, conclusion)
        markdown = markdown[:25000] + "\n\n[... middle sections truncated ...]\n\n" + markdown[-15000:]
    
    context += f"FULL PAPER CONTENT:\n{markdown}"
    
    # Call LLM
    if verbose:
        print(f"🔄 Calling Groq LLM ({ReasoningConfig.MODEL})...")
    
    client = Groq(api_key=get_api_key())
    
    response = client.chat.completions.create(
        model=ReasoningConfig.MODEL,
        messages=[
            {"role": "system", "content": REASONING_PROMPT},
            {"role": "user", "content": context}
        ],
        temperature=ReasoningConfig.TEMPERATURE,
        max_tokens=ReasoningConfig.MAX_TOKENS
    )
    
    raw_response = response.choices[0].message.content
    finish_reason = response.choices[0].finish_reason
    
    if verbose:
        print(f"   Response length: {len(raw_response):,} chars")
        print(f"   Finish reason: {finish_reason}")
    
    # Parse response
    result = parse_json_response(raw_response)
    result['paper_id'] = paper_id
    result['extraction_timestamp'] = datetime.now().isoformat()
    
    if verbose and 'error' not in result:
        print("✅ Reasoning extracted successfully!")
        print(f"\n📝 Survey Sentence:")
        print(f"   {result.get('survey_sentence', 'N/A')}")
    
    return result


def run_reasoning_pipeline(paper_ids: list = None, save: bool = True) -> list:
    """
    Run reasoning extraction on multiple papers.
    
    Args:
        paper_ids: List of paper IDs (None = all papers with Stage 1 results)
        save: Whether to save results to file
        
    Returns:
        List of reasoning extraction results
    """
    print("\n" + "="*70)
    print("🧠 STAGE 2: REASONING EXTRACTION PIPELINE")
    print("="*70)
    
    # Get paper list
    if paper_ids is None:
        stage1_results = load_stage1_results()
        paper_ids = list(stage1_results.keys())
    
    print(f"📄 Papers to process: {len(paper_ids)}")
    
    results = []
    errors = []
    
    for i, paper_id in enumerate(paper_ids, 1):
        print(f"\n[{i}/{len(paper_ids)}] Processing {paper_id}...")
        
        try:
            result = extract_reasoning(paper_id, verbose=False)
            
            if 'error' in result:
                errors.append(paper_id)
                print(f"   ❌ Error: {result.get('error', 'Unknown')[:50]}")
            else:
                results.append(result)
                survey_sent = result.get('survey_sentence', 'N/A')[:80]
                print(f"   ✅ Done - Survey: {survey_sent}...")
                
        except Exception as e:
            errors.append(paper_id)
            print(f"   ❌ Exception: {str(e)[:50]}")
    
    # Summary
    print("\n" + "="*70)
    print(f"✅ Successful: {len(results)}")
    print(f"❌ Errors: {len(errors)}")
    
    if errors:
        print(f"   Failed papers: {errors}")
    
    # Save results
    if save and results:
        os.makedirs(ReasoningConfig.OUTPUT_DIR, exist_ok=True)
        
        with open(ReasoningConfig.OUTPUT_FILE, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        
        print(f"\n💾 Saved: {ReasoningConfig.OUTPUT_FILE}")
    
    return results


# ============================================================
# CONVENIENCE FUNCTIONS
# ============================================================

def view_reasoning(paper_id: str):
    """Display saved reasoning extraction for a paper"""
    if os.path.exists(ReasoningConfig.OUTPUT_FILE):
        with open(ReasoningConfig.OUTPUT_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        for item in data:
            if item.get('paper_id') == paper_id:
                print(f"\n{'='*70}")
                print(f"🧠 REASONING: {paper_id}")
                print('='*70)
                print(json.dumps(item, indent=2, ensure_ascii=False))
                return item
    
    print(f"❌ No reasoning data found for {paper_id}")
    return None


def generate_survey_sentences() -> list:
    """Extract all survey sentences from reasoning results"""
    if not os.path.exists(ReasoningConfig.OUTPUT_FILE):
        print("❌ No reasoning results found. Run run_reasoning_pipeline() first.")
        return []
    
    with open(ReasoningConfig.OUTPUT_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    sentences = []
    print("\n" + "="*70)
    print("📝 SURVEY SENTENCES")
    print("="*70 + "\n")
    
    for item in data:
        paper_id = item.get('paper_id', 'Unknown')
        sentence = item.get('survey_sentence', 'N/A')
        sentences.append({'paper_id': paper_id, 'sentence': sentence})
        print(f"• [{paper_id}] {sentence}\n")
    
    return sentences


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":
    # Test with O_ISAC_029
    result = extract_reasoning("O_ISAC_029")
    print("\n" + "="*70)
    print("FULL RESULT:")
    print("="*70)
    print(json.dumps(result, indent=2, ensure_ascii=False))
