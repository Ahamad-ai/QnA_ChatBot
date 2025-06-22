
# QnA Chatbot with OpenAI

This project is a Question and Answer chatbot web application built using **Streamlit** and **LangChain** with OpenAI models. It also includes a standalone **HTML + JavaScript frontend** for direct API interaction. Users can interact with an AI assistant by asking questions and receiving helpful responses.

---

## 🚀 Features

- Web-based chat interface using Streamlit (Python backend)  
- Alternative HTML + JavaScript frontend (no backend required)  
- Supports multiple OpenAI models (e.g., `gpt-4.1`, `gpt-4o`)  
- Adjustable response parameters (temperature, max tokens)  
- Secure API key input (sidebar in Streamlit, masked in HTML)  
- Uses LangChain for prompt management and output parsing (Streamlit)  
- Environment variable management with `python-dotenv`  
- LangSmith tracing enabled for experiment tracking  
- Demo videos included  
- Custom CSS for a modern UI  

---

## 📁 File Structure

```
app.py                      # Main Streamlit application (Python)
requirements.txt            # Python dependencies
script.js                   # JavaScript logic for HTML frontend
index.html                  # Standalone HTML chatbot UI
style.css                   # Custom styles for HTML UI
static/bg.png               # Background image for HTML UI
demo/QnA_demo.mp4           # Demo video
demo/QnA_demo_new.mp4       # Demo video
.env                        # Environment variables (not committed)
.gitignore                  # Ignores .env and virtual environment
```

---

## ⚙️ Setup Instructions (Streamlit App)

1. Clone the repository  
2. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root with your OpenAI and LangSmith keys:  
   ```
   OPENAI_API_KEY=your_openai_api_key
   LANGCHAIN_API_KEY=your_langsmith_api_key
   ```

4. Run the app  
   ```bash
   streamlit run app.py
   ```

---

## 💬 Usage

### Streamlit App

- Enter your OpenAI API key in the sidebar  
- Select the desired OpenAI model  
- Adjust temperature and max tokens as needed  
- Type your question and get instant answers  

### HTML + JavaScript Frontend

- Open `index.html` in your browser (no server required)  
- Enter your OpenAI API key, select model, adjust parameters, and chat  
- All requests are sent directly to OpenAI API from your browser  
- **Note:** Your API key is never sent to any server except OpenAI  

---

## 📹 Demo

Demo videos are available in the `demo/` folder:

- `QnA_demo.mp4`  
- `QnA_demo_new.mp4`

---

## 📌 Requirements

- Python 3.10+ (for Streamlit app)  
- OpenAI API key  
- LangSmith API key (optional, for tracing)
