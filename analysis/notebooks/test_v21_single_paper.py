"""
Quick Test Script: v2.1 Schema Extraction for Single Paper (O_ISAC_029)
========================================================================
Use this to test the new v2.1 HOW-focused fields without running full pipeline.
Run in Colab after setup steps 1-4.
"""

import os
import json
from groq import Groq

# Import the SYSTEM_PROMPT from the main pipeline
from extraction_pipeline_v3 import SYSTEM_PROMPT, Config

def get_api_key():
    """Get GROQ_API_KEY from Colab secrets or environment."""
    # Try Colab secrets first
    try:
        from google.colab import userdata
        return userdata.get('GROQ_API_KEY')
    except:
        pass
    
    # Fall back to environment variable
    api_key = os.environ.get('GROQ_API_KEY')
    if api_key:
        return api_key
    
    raise ValueError(
        "GROQ_API_KEY not found! Set it in:\n"
        "  - Colab Secrets (🔑 icon in left sidebar), or\n"
        "  - Environment variable: export GROQ_API_KEY=your_key"
    )

def test_single_paper(paper_id="O_ISAC_029"):
    """Test v2.1 extraction on a single paper."""
    
    print(f"\n{'='*70}")
    print(f"🧪 TESTING v2.1 SCHEMA ON: {paper_id}")
    print(f"{'='*70}\n")
    
    # Load markdown content
    md_path = os.path.join(Config.MARKDOWN_DIR, paper_id, paper_id, f"{paper_id}.md")
    if not os.path.exists(md_path):
        # Try alternative path structure
        md_path = os.path.join(Config.MARKDOWN_DIR, paper_id, f"{paper_id}.md")
    
    if not os.path.exists(md_path):
        print(f"❌ Markdown not found: {md_path}")
        return None
    
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"📄 Loaded: {md_path}")
    print(f"   Content length: {len(content):,} chars")
    
    # Truncate if too long
    max_chars = 85000
    if len(content) > max_chars:
        content = content[:max_chars]
        print(f"   Truncated to: {max_chars:,} chars")
    
    # Initialize Groq client with API key
    api_key = get_api_key()
    client = Groq(api_key=api_key)
    
    user_prompt = f"""Extract structured data from this O-ISAC paper.
Paper ID: {paper_id}

--- PAPER CONTENT ---
{content}
--- END PAPER CONTENT ---

Return ONLY valid JSON following the schema. Include all Study_Level fields including the NEW v2.1 fields:
- key_contribution
- gap_addressed  
- performance_enablers (array of enabler types)
- novel_component
- novel_component_specs

And for each Experiment's Receiver section:
- rx_photonic_processing
- rx_modulator_type
- rx_modulator_bandwidth_ghz
- rx_modulator_operating_point
- false_target_mitigation
"""

    print("\n🔄 Calling Groq LLM (llama-3.3-70b-versatile)...")
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.05,
        max_tokens=16000  # Increased for v2.1 schema
    )
    
    raw_response = response.choices[0].message.content
    finish_reason = response.choices[0].finish_reason
    
    print(f"   Response length: {len(raw_response):,} chars")
    print(f"   Finish reason: {finish_reason}")
    
    if finish_reason == "length":
        print("   ⚠️ Response was truncated due to token limit!")
    
    # Parse JSON
    try:
        # Try to extract JSON from response
        if "```json" in raw_response:
            json_str = raw_response.split("```json")[1].split("```")[0]
        elif "```" in raw_response:
            json_str = raw_response.split("```")[1].split("```")[0]
        else:
            json_str = raw_response
        
        result = json.loads(json_str.strip())
        print("✅ JSON parsed successfully!\n")
        
    except json.JSONDecodeError as e:
        print(f"❌ JSON parse error: {e}")
        print(f"Raw response:\n{raw_response[:500]}...")
        return None
    
    # Display v2.1 specific fields
    print("="*70)
    print("📊 v2.1 NEW FIELDS EXTRACTED:")
    print("="*70)
    
    study = result.get("Study_Level", {})
    
    print(f"\n🎯 key_contribution:")
    print(f"   {study.get('key_contribution', 'NOT EXTRACTED')}")
    
    print(f"\n🔍 gap_addressed:")
    print(f"   {study.get('gap_addressed', 'NOT EXTRACTED')}")
    
    print(f"\n⚡ performance_enablers:")
    enablers = study.get('performance_enablers', [])
    if enablers:
        for e in enablers:
            print(f"   • {e}")
    else:
        print("   NOT EXTRACTED")
    
    print(f"\n🔧 novel_component:")
    print(f"   {study.get('novel_component', 'NOT EXTRACTED')}")
    
    print(f"\n📐 novel_component_specs:")
    print(f"   {study.get('novel_component_specs', 'NOT EXTRACTED')}")
    
    # Receiver details
    print(f"\n{'='*70}")
    print("📡 RECEIVER v2.1 FIELDS (per experiment):")
    print("="*70)
    
    for exp in result.get("Experiments", []):
        exp_id = exp.get("experiment_id", "?")
        rx = exp.get("Receiver", {})
        print(f"\n  Experiment {exp_id}:")
        print(f"    rx_photonic_processing: {rx.get('rx_photonic_processing', 'NR')}")
        print(f"    rx_modulator_type: {rx.get('rx_modulator_type', 'NR')}")
        print(f"    rx_modulator_bandwidth_ghz: {rx.get('rx_modulator_bandwidth_ghz', 'NR')}")
        print(f"    rx_modulator_operating_point: {rx.get('rx_modulator_operating_point', 'NR')}")
        print(f"    false_target_mitigation: {rx.get('false_target_mitigation', 'NR')}")
    
    # Save result
    output_path = os.path.join(Config.OUTPUT_DIR, f"test_{paper_id}_v21.json")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"\n💾 Saved: {output_path}")
    
    return result

if __name__ == "__main__":
    test_single_paper("O_ISAC_029")
