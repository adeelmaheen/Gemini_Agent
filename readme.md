# 🤖 Gemini Multi-Tool Agent

This is a powerful AI agent built with [Google Gemini API](https://ai.google.dev/), enhanced with voice support, memory, and multi-functional tools like web search, calculator, and summarizer. It offers both **text and voice-based interaction**, a persistent **chat history**, and a **to-do/notes manager**.

---

## 🚀 Features

- 💬 **Text Chat** – Ask questions, generate content, or use commands like `search`, `calculate`, or `summarize`.
- 🎙️ **Voice Input** – Speak your queries using your microphone.
- 🔊 **Text-to-Speech** – Listen to AI-generated responses.
- 💾 **Persistent Chat History** – All conversations are stored locally and can be downloaded.
- 📝 **Notes / To-Do Manager** – Save reminders or task lists during the session.
- 🧠 **Session Memory** – Uses `st.session_state` and SQLite to remember context.
- 🛠️ **Modular Tool Support** – Easily plug in tools like `web_search`, `calculator`, and `text summarizer`.

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Google Generative AI (Gemini 1.5 Flash)**
- **SQLite** (for saving chat and notes)
- **SpeechRecognition + pyttsx3** (for voice input/output)

---

## 📁 Folder Structure

# 🤖 Gemini Multi-Tool Agent

This is a powerful AI agent built with [Google Gemini API](https://ai.google.dev/), enhanced with voice support, memory, and multi-functional tools like web search, calculator, and summarizer. It offers both **text and voice-based interaction**, a persistent **chat history**, and a **to-do/notes manager**.

---

## 🚀 Features

- 💬 **Text Chat** – Ask questions, generate content, or use commands like `search`, `calculate`, or `summarize`.
- 🎙️ **Voice Input** – Speak your queries using your microphone.
- 🔊 **Text-to-Speech** – Listen to AI-generated responses.
- 💾 **Persistent Chat History** – All conversations are stored locally and can be downloaded.
- 📝 **Notes / To-Do Manager** – Save reminders or task lists during the session.
- 🧠 **Session Memory** – Uses `st.session_state` and SQLite to remember context.
- 🛠️ **Modular Tool Support** – Easily plug in tools like `web_search`, `calculator`, and `text summarizer`.

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Google Generative AI (Gemini 1.5 Flash)**
- **SQLite** (for saving chat and notes)
- **SpeechRecognition + pyttsx3** (for voice input/output)

---

## 📁 Folder Structure

.
├── app.py
├── agent.py
├── db.py
├── .streamlit/
│ └── secrets.toml
├── tools/
│ ├── calculator.py
│ ├── summarizer.py
│ └── web_search.py
├── voice/
│ ├── speech_to_text.py
│ └── text_to_speech.py
└── requirements.txt


---

## 🔐 Setup Secrets

Create a `.streamlit/secrets.toml` file to store your API key securely:

```toml
GOOGLE_API_KEY = "your_google_api_key_here"


## 📦 Installation
- Clone the repo

git clone https://github.com/yourusername/gemini-agent.git

cd gemini-agent

Install dependencies
(Recommended: Use a virtual environment)

pip install -r requirements.txt

Run the app

streamlit run app.py 


## 🧠 Commands You Can Use
- search latest AI news

- calculate 5 * (3 + 2)

- summarize This is a long paragraph...

- Or just have a conversation with the agent! ```

---

## 🧩 Tools
- You can easily extend the system by editing or adding new tools inside the tools/ directory.



## 🧑‍💻 Author

**Maheen Arif**  
🌐 [Email] (adeelmaheen602@gmail.com)  
🐱 [GitHub](https://github.com/adeelmaheen)  
💼 [LinkedIn](https://www.linkedin.com/in//maheen-arif-a929412b6/)
