import google.generativeai as genai
import streamlit as st

from tools.web_search import search_web
from tools.calculator import calculate
from tools.summarizer import summarize_text

# Configure API key from Streamlit secrets
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

def process_query(user_input):
    input_lower = user_input.lower()

    if "search" in input_lower:
        query = user_input.replace("search", "").strip()
        return f"🔍 Web Search:\n{search_web(query)}"

    elif "calculate" in input_lower:
        expression = user_input.replace("calculate", "").strip()
        return f"🧮 Result:\n{calculate(expression)}"

    elif "summarize" in input_lower:
        text = user_input.replace("summarize", "").strip()
        return f"📝 Summary:\n{summarize_text(text)}"

    else:
        response = model.generate_content(user_input)
        return response.text
