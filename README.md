# GramMate – AI-Powered Grammar Corrector ✨

GramMate is a beginner-friendly Generative AI application that helps users improve their writing by correcting grammar, spelling, and punctuation errors using Google's Gemini Large Language Model (LLM).

The application provides multiple writing styles and optional grammar explanations to make writing clearer, more accurate, and professional.

## 🚀 Features

- **AI-Powered Grammar Correction:** Corrects grammar, spelling, and punctuation errors.
- **Multiple Writing Styles:** Choose from:
  - Basic Grammar Correction
  - Professional English
  - Simple English
  - Academic English
- **Grammar Explanations:** Understand the mistakes and learn why corrections are needed.
- **Meaning Preservation:** Maintains the original meaning of the user's text.
- **Interactive Interface:** Simple and user-friendly interface built with Streamlit.
- **Real-Time Processing:** Generates corrected text using the Gemini API.

## 🛠️ Tech Stack

- **Programming Language:** Python
- **Frontend:** Streamlit
- **AI Model:** Google Gemini 2.5 Flash
- **API Integration:** Google GenAI SDK
- **Environment Management:** python-dotenv
- **Concepts:** Generative AI, Large Language Models (LLMs), Prompt Engineering, API Integration

## 📂 Project Structure

```text
GramMate/
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/GramMate-AI-Grammar-Corrector.git
```

### 2. Navigate to the Project Folder

```bash
cd GramMate-AI-Grammar-Corrector
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Gemini API Key

Get your API key from [Google AI Studio](https://aistudio.google.com/apikey).

Create a `.env` file in the project root directory:

```env
GEMINI_API_KEY=your_gemini_api_key
```

**Important:** Never upload your `.env` file or API key to GitHub.

### 5. Run the Application

```bash
python -m streamlit run app.py
```

The application will open in your browser.

## 🧠 How It Works

1. The user enters text that needs correction.
2. The user selects a preferred writing style.
3. The application creates a customized prompt using prompt engineering techniques.
4. The prompt is sent to Google's Gemini 2.5 Flash model through the Gemini API.
5. Gemini analyzes the input and generates corrected text.
6. The application displays the corrected output and, optionally, explanations of grammatical mistakes.

## 💡 Prompt Engineering

GramMate uses prompt engineering to guide the LLM's responses.

The prompt defines:
- **Role:** Act as an expert English grammar correction assistant.
- **Task:** Correct grammar, spelling, and punctuation.
- **Constraints:** Preserve the original meaning and avoid adding unrelated information.
- **Writing Style:** Adapt the output to the user's selected style.
- **Output Format:** Return corrected text with optional explanations.

## 🔮 Future Enhancements

- Text-to-speech functionality.
- Support for multiple languages.
- Chrome browser extension.
- Voice-based text input.
- Download corrected text as a document.
- Writing quality and readability suggestions.

## 🎯 Learning Outcomes

Through this project, I explored:

- Fundamentals of Generative AI.
- Understanding Large Language Models (LLMs).
- Integrating Gemini API with Python.
- Writing effective prompts using prompt engineering.
- Building interactive applications using Streamlit.
- Managing API keys securely using environment variables.

## 👩‍💻 Author

Developed as a beginner-level Generative AI project to explore LLM integration and practical prompt engineering.

---

**GramMate – Write Better. Communicate Smarter. ✨**

