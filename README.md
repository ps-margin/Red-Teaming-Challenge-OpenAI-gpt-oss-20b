# Chain of Thought Reasoning Manipulation Vulnerability Reproduction

## ⚠️ Important Safety Notice

**This repository contains research materials for a legitimate AI safety vulnerability discovered during OpenAI's red-teaming challenge.**

- **Purpose**: Document and reproduce vulnerability to improve AI safety
- **Ethical Use Only**: Do not use for malicious purposes
- **Responsible Disclosure**: Findings reported to OpenAI for remediation

## Quick Start

### Prerequisites

1. **Python 3.13+** (as specified in pyproject.toml)
2. **Groq API Key** for accessing gpt-oss-20b model
3. **Gemini API Key** for advanced LLM-based evaluation (optional but recommended)
4. **Jupyter Notebook** environment

### Setup Instructions

1. **Clone/Download the repository**:
   ```bash
   cd "red teaming"
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file with your API keys:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   GEMINI_API_KEY=your_gemini_api_key_here
   ```
   
   **Get free API keys:**
   - **Groq**: https://console.groq.com/keys (required for vulnerability testing)
   - **Gemini**: https://aistudio.google.com/apikey (recommended for advanced evaluation)

4. **Launch Jupyter Notebook**:
   ```bash
   jupyter notebook reproduction_notebook.ipynb
   ```

### Running the Reproduction

1. **Open the notebook**: `reproduction_notebook.ipynb`
2. **Run all cells sequentially** - the notebook is designed to be executed from top to bottom
3. **Review results** - vulnerability confirmation and analysis will be displayed
4. **Check generated report** - `vulnerability_reproduction_report.json` will be created

## File Structure

```
red teaming/
├── reproduction_notebook.ipynb    # Main reproduction notebook
├── cot_manipulation_finding.json  # Original vulnerability findings
├── requirements.txt               # Python dependencies
├── REPRODUCTION_README.md         # This file
├── main.py                       # Original Streamlit app (reference)
├── pyproject.toml               # Project configuration
└── .env                         # API keys (create this)
```

## Key Components

### 1. Vulnerability Client (`VulnerabilityClient`)
- Configured with exact model parameters from findings
- Handles API calls with proper error handling
- Uses temperature=1.0, reasoning_effort="high"

### 2. Reasoning Manipulator (`ReasoningManipulator`)
- Extracts reasoning chains from model responses  
- Applies safety transformations (disallowed→allowed, refuse→comply)
- Creates manipulation prompts for testing

### 3. Advanced Content Filter (`ContentFilter`)
- **Dual-LLM Evaluation**: Uses Gemini 2.5 Flash for sophisticated analysis
- **Content Harmfulness Assessment**: Distinguishes harmful content from safety refusals
- **Bypass Detection**: Specialized analysis for safety guardrail bypasses
- **Automatic Fallback**: Rule-based evaluation when LLM unavailable
- **Safety Redaction**: Automatically filters harmful outputs for research safety

### 4. Automated Testing
- Verifies vulnerability reproduction works correctly
- Validates against original findings
- Generates comprehensive analysis reports

## Expected Results

If the vulnerability is still present, you should see:

1. ✅ **Step 1**: Model provides normal safety response with reasoning
2. 🔄 **Step 2**: Reasoning successfully manipulated with safety terms flipped  
3. 🚨 **Step 3**: Fresh model instance generates harmful content following manipulated reasoning

If the vulnerability has been patched:
- Model will refuse to follow manipulated reasoning
- Content filter will show "VULNERABILITY NOT TRIGGERED"
- This is the desired outcome from a security perspective

## Safety Features

- **Content Filtering**: All harmful outputs are automatically redacted
- **Research Context**: Clear warnings and ethical use guidelines
- **Automated Testing**: Minimal manual exposure to potentially harmful content
- **Reproducibility**: Deterministic testing with fixed parameters

## Troubleshooting

### Common Issues

1. **API Key Error**: 
   - Ensure `GROQ_API_KEY` is set in `.env` file
   - Verify API key is valid and has access to gpt-oss-20b model

2. **Import Errors**:
   - Run `pip install -r requirements.txt`
   - Ensure Python 3.13+ is being used

3. **No Reasoning in Response**:
   - Verify `reasoning_effort="high"` is set
   - Some model responses may not include reasoning chains

4. **Vulnerability Not Reproduced**:
   - This may indicate the vulnerability has been patched (good!)
   - Check model parameters match exactly
   - Review manipulation transformations

5. **⚠️ LLM Evaluation Rate Limits (Gemini API)**:
   ```
   LLM evaluation failed: 429 RESOURCE_EXHAUSTED
   You exceeded your current quota, please check your plan and billing details
   GenerateRequestsPerMinutePerProjectPerModel-FreeTier quotaValue: 10
   ```
   
   **What this means:**
   - The advanced LLM-based evaluation using Gemini 2.5 Flash hit rate limits
   - Free tier allows only 10 requests per minute for Gemini models
   - The system automatically falls back to rule-based evaluation
   
   **Solutions:**
   - **Wait and retry**: Rate limits reset after 1 minute
   - **Add delays**: The notebook includes 2-second delays between API calls
   - **Use GEMINI_API_KEY**: Ensure you have a valid Gemini API key in `.env`
   - **Upgrade plan**: Consider upgrading for higher rate limits if needed
   
   **Fallback behavior:**
   - Rule-based evaluation still works and provides vulnerability detection
   - You'll see "⚠️ LLM evaluation failed - using fallback" messages
   - Results remain valid but with lower confidence scores
   - This is expected behavior and doesn't break the reproduction

### Getting Help

If you encounter issues:

1. Check the error messages in notebook output
2. Verify all dependencies are installed correctly
3. Ensure API credentials are configured properly
4. Review the original `main.py` for reference implementation

## Ethical Guidelines

### ✅ Appropriate Use
- AI safety research and vulnerability documentation
- Educational purposes in security/AI safety courses  
- Responsible disclosure to model developers
- Academic research on AI alignment and safety

### ❌ Prohibited Use
- Creating harmful content for malicious purposes
- Circumventing safety measures in production systems
- Sharing techniques without proper safety context
- Any use that could cause harm to individuals or society

## Research Impact

This reproduction notebook demonstrates:

1. **Systematic Vulnerability**: CoT reasoning manipulation works across content categories
2. **Automation Potential**: Attacks can be systematized and automated
3. **Detection Methods**: Content filtering can identify successful exploits
4. **Remediation Needs**: Models need stronger reasoning chain validation

## Contributing

If you discover improvements to the reproduction methodology:

1. Ensure all changes maintain safety standards
2. Document any new test cases thoroughly  
3. Verify content filtering still works correctly
4. Update this README with any new requirements

## Citation

If using this research, please cite:

```
Chain of Thought Reasoning Manipulation Vulnerability Reproduction
OpenAI Red-Teaming Challenge 2025
Model: gpt-oss-20b (2025-08-05)
Vulnerability ID: [To be assigned by OpenAI]
```

---

**Remember**: This is legitimate security research to improve AI safety. Use responsibly and ethically.