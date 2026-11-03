# AI Resume Critiquer

A Streamlit application that accepts a resume in PDF or TXT format and uses an LLM to generate structured feedback. A target job role can be supplied to make the critique more relevant.

## Features

- PDF and plain-text resume input.
- Optional target-role context.
- AI-generated feedback on clarity, skills presentation and experience descriptions.
- Suggestions for improving the resume for a chosen role.

## Technology

- Python 3.11+
- Streamlit
- Groq API (Llama-family model)
- PyPDF2
- python-dotenv

## Setup

```bash
git clone https://github.com/HiiAliasgar/AI-Resume-Critiquer.git
cd AI-Resume-Critiquer

# Install dependencies
uv sync
# Or: pip install -r requirements.txt

# Create local environment configuration
cp .env.example .env
```

Add your Groq key to `.env`:

```env
GROQ_API_KEY=your_groq_api_key
```

Run the application:

```bash
streamlit run main.py
```

The local interface opens at `http://localhost:8501`.

## Usage

1. Upload a PDF or TXT resume.
2. Enter a target role if you want role-specific feedback.
3. Submit the resume for analysis.
4. Review the generated critique and decide which suggestions are appropriate.

## Responsible use

The application provides AI-generated suggestions, not hiring decisions or guarantees of interview success. Review all recommendations for factual accuracy; do not add skills or experience that you do not have. Avoid uploading sensitive personal information unless you understand how the configured model provider processes it.

## Source

[GitHub repository](https://github.com/HiiAliasgar/AI-Resume-Critiquer)
