# 🧠 TODO: Chain-of-Thought Entegre Extraction (Option B)

**Oluşturulma Tarihi:** 2025-12-09
**Öncelik:** 🔥 Yüksek - Survey kalitesini artıracak

---

## 💡 Konsept

Mevcut extraction pipeline'ı iki aşamalı değil, **tek aşamalı chain-of-thought** yaklaşımına dönüştürmek. LLM önce "düşünür" (reasoning), sonra structured output üretir.

## 🎯 Motivasyon

- Stage 1 (structured) + Stage 2 (reasoning) = 2x API call = 2x maliyet
- Chain-of-thought ile tek call'da hem reasoning hem structured output
- Reasoning, structured output'un kalitesini artırır (self-consistency)

## 📐 Proposed Architecture

```
┌─────────────────────────────────────────────────────────────┐
│  PROMPT STRUCTURE                                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  [System] You are a technical reviewer...                   │
│                                                             │
│  [Instruction]                                              │
│  Before extracting structured data, THINK through:          │
│                                                             │
│  <thinking>                                                 │
│  1. What is the main problem addressed?                     │
│  2. How does this paper solve it?                           │
│  3. What makes this different from prior work?              │
│  4. What is the key technical innovation?                   │
│  </thinking>                                                │
│                                                             │
│  Then provide structured JSON with your analysis embedded.  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## 🔧 Implementation Ideas

### 1. Thinking Block Extraction
```python
# LLM response'dan thinking block'u parse et
thinking_match = re.search(r'<thinking>(.*?)</thinking>', response, re.DOTALL)
reasoning = thinking_match.group(1) if thinking_match else ""
```

### 2. Hybrid Schema
```yaml
Output:
  Reasoning:
    problem_identified: "..."
    solution_approach: "..."
    differentiator: "..."
    
  Structured:
    Paper_ID: "..."
    Study_Level: { ... }
    Experiments: [ ... ]
```

### 3. Model Selection
- `llama-3.3-70b-versatile` - İyi reasoning, hızlı
- `deepseek-r1` - Exceptional reasoning (if available on Groq)
- `claude-3-opus` - Best reasoning (Anthropic API)

## 📊 Expected Benefits

| Metric | Stage 1+2 (Current) | Chain-of-Thought |
|--------|---------------------|------------------|
| API Calls | 2x per paper | 1x per paper |
| Cost | ~$0.10/paper | ~$0.06/paper |
| Reasoning Quality | Disconnected | Integrated |
| Output Consistency | May conflict | Self-consistent |

## 🗓️ Timeline

- [ ] Design thinking block format
- [ ] Prototype with O_ISAC_029
- [ ] Compare quality vs current approach
- [ ] If better, integrate into main pipeline
- [ ] Create separate Colab notebook for this approach

## 📁 Related Files

- `extraction_pipeline_v3.py` - Current pipeline
- `reasoning_extraction_v1.py` - Stage 2 (Option A)
- `chain_of_thought_extraction.py` - This approach (to be created)

---

> 💬 **Not:** Bu yaklaşım survey kalitesini önemli ölçüde artırabilir. 
> O_ISAC_029 üzerinde test ettikten sonra karar verelim!
