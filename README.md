# AI Resume Critiquer 📃

An interactive Streamlit web app that uses AI to provide personalized feedback on resumes. Upload your resume (PDF or TXT format), optionally specify a job role, and receive detailed, constructive critique focused on content clarity, skills presentation, experience descriptions, and tailored suggestions for your targeted job role.

## Features

- 📄 **PDF & TXT Support** — Upload resumes in PDF or plain text format
- 🎯 **Job-Specific Feedback** — Optionally target a specific role for tailored advice
- 🤖 **AI-Powered Analysis** — Uses Groq's LLM API for intelligent resume critique
- ⚡ **Fast Results** — Get comprehensive feedback in seconds

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/HiiAliasgar/AI-Resume-Critiquer.git
cd AI-Resume-Critiquer
```

### 2. Install dependencies

```bash
# Using uv (recommended)
uv sync

# Or using pip
pip install -r requirements.txt
```

### 3. Set up environment variables

Create a `.env` file in the project root:

```bash
cp .env.example .env
```

Then edit `.env` and add your Groq API key:

```
GROQ_API_KEY=your_groq_api_key_here
```

Get a free API key at [console.groq.com](https://console.groq.com/)

### 4. Run the app

```bash
streamlit run main.py
```

The app will open in your browser at `http://localhost:8501`.

## Usage

1. Upload your resume (PDF or TXT)
2. Optionally enter the job role you're targeting
3. Click **"Analyze Resume"**
4. Review the AI-generated feedback

## Tech Stack

- **Python 3.11+**
- **Streamlit** — Web UI framework
- **Groq API** — LLM inference (Llama 3.1)
- **PyPDF2** — PDF text extraction
- **python-dotenv** — Environment variable management

## License

MIT License — see [LICENSE](LICENSE) for details.
