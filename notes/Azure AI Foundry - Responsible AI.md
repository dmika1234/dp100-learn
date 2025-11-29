# Azure AI Foundry – Responsible AI Notes

---

## Overview

- **Generative AI**: Enables creation of human-like content using models trained on large datasets.
- **Risks**: Potential for offensive, inaccurate, or harmful outputs.
- **Responsible AI**: Requires identifying, measuring, and mitigating risks throughout the AI solution lifecycle.

---

## Four-Stage Process for Responsible Generative AI

1. **Map** potential harms.
2. **Measure** the presence of these harms.
3. **Mitigate** harms at multiple solution layers.
4. **Manage** the solution responsibly (deployment & operations).

---

## 1. Map Potential Harms

### Steps:
1. **Identify potential harms**
   - Offensive, discriminatory, or inaccurate content.
   - Content supporting illegal/unethical behavior.
   - Use documentation:
     - [Azure OpenAI Transparency Note](https://learn.microsoft.com/en-us/legal/cognitive-services/openai/transparency-note)
     - [GPT-4 System Card](https://cdn.openai.com/papers/gpt-4-system-card.pdf)
     - [Microsoft RAI Impact Assessment Guide](https://msblogs.thesourcemediaassets.com/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Guide.pdf)
     - [Responsible AI Impact Assessment Template](https://msblogs.thesourcemediaassets.com/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf)
     - [Responsible Use of AI Overview](https://learn.microsoft.com/en-us/azure/ai-services/responsible-use-of-ai-overview)
2. **Prioritize identified harms**
   - Assess likelihood and impact.
   - Consider intended use and potential misuse.
   - Example: Recipe assistant—poison recipe (high impact, low likelihood) vs. undercooked food (lower impact, higher likelihood).
3. **Test and verify prioritized harms**
   - Use "red team" testing: Deliberately probe for weaknesses/harmful outputs.
   - Document and review red team findings.
   - [Red Teaming LLMs](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/concepts/red-teaming)
4. **Document and share verified harms**
   - Maintain and update a prioritized list of harms.
   - Share with stakeholders.

---

## 2. Measure Potential Harms

### Steps:
1. **Prepare prompts** likely to elicit each documented harm.
2. **Generate outputs** using the system.
3. **Evaluate outputs** using strict, pre-defined criteria (e.g., "harmful" vs. "not harmful" or graded levels).

- **Manual Testing**: Start with small, manual tests to refine criteria.
- **Automated Testing**: Scale up with automation/classification models.
- **Ongoing Manual Validation**: Periodically check automated results.

---

## 3. Mitigate Potential Harms

### Layered Mitigation Approach:

1. **Model Layer**
   - Choose appropriate model for use case.
   - Fine-tune models with relevant data to reduce risk.
2. **Safety System Layer**
   - Use platform-level content filters (e.g., severity levels: safe, low, medium, high; categories: hate, sexual, violence, self-harm).
   - Implement abuse detection and alerting.
3. **System Message & Grounding Layer**
   - Define behavioral parameters in system prompts.
   - Use prompt engineering and grounding data.
   - Apply Retrieval Augmented Generation (RAG) for context.
4. **User Experience Layer**
   - Constrain user inputs and validate outputs.
   - Provide transparent documentation about system capabilities, limitations, and residual risks.

---

## 4. Manage a Responsible Generative AI Solution

### Prerelease Reviews
- Ensure compliance with:
  - Legal
  - Privacy
  - Security
  - Accessibility

### Release & Operations
- **Phased delivery**: Start with restricted user groups.
- **Incident response plan**: Define response times and actions.
- **Rollback plan**: Steps to revert to previous state if needed.
- **Immediate blocking**: Ability to block harmful responses/users.
- **User feedback**: Allow users to report issues (e.g., "inaccurate", "harmful", "offensive").
- **Telemetry**: Track user satisfaction and system performance, ensuring privacy compliance.

---

## Microsoft Foundry Content Safety

- **Built-in content analysis** for Language, Vision, and Azure OpenAI.
- **Features**:
  - **Prompt shields**: Detect risky user input.
  - **Groundedness detection**: Check if responses are based on source content.
  - **Protected material detection**: Identify copyrighted content.
  - **Custom categories**: Define new risk patterns.
- **Documentation**: [Content Safety Overview](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/overview)

---

## References

- [Azure OpenAI Transparency Note](https://learn.microsoft.com/en-us/legal/cognitive-services/openai/transparency-note)
- [Microsoft RAI Impact Assessment Guide](https://msblogs.thesourcemediaassets.com/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Guide.pdf)
- [Responsible Use of AI Overview](https://learn.microsoft.com/en-us/azure/ai-services/responsible-use-of-ai-overview)
- [Red Teaming LLMs](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/concepts/red-teaming)
- [Content Safety Overview](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/overview)
- [GPT-4 System Card](https://cdn.openai.com/papers/gpt-4-system-card.pdf)
- [Responsible AI Impact Assessment Template](https://msblogs.thesourcemediaassets.com/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf)

---
