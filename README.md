# QnA Chatbot with OpenAI

This project is a simple Question and Answer chatbot web application built using [Streamlit](https://streamlit.io/) and [LangChain](https://python.langchain.com/) with OpenAI models. It allows users to interact with an AI assistant by asking questions and receiving helpful responses.

## Features
- Web-based chat interface using Streamlit
- Supports multiple OpenAI models (e.g., gpt-4.1, gpt-4o)
- Adjustable response parameters (temperature, max tokens)
- Secure API key input via sidebar
- Uses LangChain for prompt management and output parsing
- Environment variable management with python-dotenv
- LangSmith tracing enabled for experiment tracking

## Setup Instructions

1. **Clone the repository**
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Create a `.env` file** in the project root with your OpenAI and LangSmith keys:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   LANGCHAIN_API_KEY=your_langsmith_api_key
   ```
4. **Run the app**:
   ```bash
   streamlit run app.py
   ```

## File Structure
- `app.py` — Main Streamlit application
- `requirements.txt` — Python dependencies
- `.env` — Environment variables (not committed)
- `.gitignore` — Ignores `.env` and virtual environment

## Requirements
- Python 3.10+
- OpenAI API key
- LangSmith API key (for tracing, optional)

## Usage
- Enter your OpenAI API key in the sidebar
- Select the desired OpenAI model
- Adjust temperature and max tokens as needed
- Type your question and get instant answers!

---

*This project is for educational/demo purposes. Please keep your API keys secure.*
