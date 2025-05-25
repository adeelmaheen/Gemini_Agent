import streamlit as st
import tempfile
import speech_recognition as sr
import google.generativeai as genai

from agent import process_query
import db
from voice.text_to_speech import speak_text

# --- Configure Google API ---
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

# --- Setup DB ---
db.create_tables()

if "history" not in st.session_state:
    st.session_state.history = db.load_chats()

if "notes" not in st.session_state:
    st.session_state.notes = db.load_notes()

if "last_response" not in st.session_state:
    st.session_state.last_response = ""

# --- Page config ---
st.set_page_config(page_title="Gemini Agent", page_icon="🤖")
st.title("🤖 Gemini Multi-Tool Agent")

# --- Button styles ---
st.markdown("""
    <style>
    .stButton>button {
        background-color: #0066cc;
        color: white;
        border-radius: 10px;
        padding: 0.5em 1em;
        border: none;
    }
    .stButton>button:hover {
        background-color: #004999;
    }
    </style>
""", unsafe_allow_html=True)

# --- Chat Section ---
st.header("💬 Chat with Agent")

with st.form("chat_form"):
    user_input = st.text_input("Type your query (e.g., 'search AI news', 'calculate 5*5'):", key="chat_input")
    submitted = st.form_submit_button("💬 Submit")

if submitted and user_input:
    st.session_state.history.append(("You", user_input))
    db.save_chat("You", user_input)

    response = process_query(user_input)
    st.session_state.history.append(("Gemini", response))
    db.save_chat("Gemini", response)
    st.session_state.last_response = response

    st.balloons()

# Show chat history
for sender, message in st.session_state.history:
    st.markdown(f"**{sender}:** {message}")

# --- Clear History ---
with st.expander("⚙️ Chat Settings"):
    confirm_clear = st.checkbox("✅ Are you sure you want to clear the chat history?", key="confirm_clear")
    if st.button("🗑️ Clear Chat History"):
        if confirm_clear:
            st.session_state.history.clear()
            db.clear_chats()
            st.success("Chat history cleared.")
        else:
            st.warning("Please confirm by checking the box above.")

# --- Voice Input & Output ---
import tempfile
import speech_recognition as sr
import streamlit as st
from agent import process_query
import db

st.subheader("🎤 Voice Assistant")
col1, col2 = st.columns([1, 1])

with col1:
    audio_bytes = st.audio_input("🎧 Record your voice here")

    if audio_bytes is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio_file:
            temp_audio_file.write(audio_bytes.read())  # read bytes from UploadedFile
            temp_audio_path = temp_audio_file.name

        recognizer = sr.Recognizer()
        with sr.AudioFile(temp_audio_path) as source:
            audio = recognizer.record(source)

        try:
            transcribed = recognizer.recognize_google(audio)
            st.success(f"You said: {transcribed}")

            st.session_state.history.append(("You (voice)", transcribed))
            db.save_chat("You (voice)", transcribed)

            response = process_query(transcribed)
            st.session_state.history.append(("Gemini", response))
            db.save_chat("Gemini", response)
            st.session_state.last_response = response
            st.balloons()

        except sr.UnknownValueError:
            st.error("Could not understand the audio.")
        except sr.RequestError as e:
            st.error(f"API error: {e}")

with col2:
    if st.button("🔊 Speak Response"):
        if st.session_state.last_response:
            from voice.text_to_speech import speak_text

            audio_file = speak_text(st.session_state.last_response)
            if audio_file:
                with open(audio_file, 'rb') as f:
                    audio_data = f.read()
                    st.audio(audio_data, format='audio/mp3')
            else:
                st.error("Text-to-Speech failed. Please try again.")
        else:
            st.warning("No response to speak yet.")

# --- Save Chat History ---
st.header("💾 Save Chat History")

if st.session_state.history:
    chat_log = "\n\n".join(f"{sender}: {msg}" for sender, msg in st.session_state.history)
    chat_bytes = chat_log.encode('utf-8')

    st.download_button(
        label="📅 Download Chat History as TXT",
        data=chat_bytes,
        file_name="gemini_chat_history.txt",
        mime="text/plain"
    )
else:
    st.info("No chat history to save yet.")

# --- Notes / To-Do Manager ---
st.header("📝 Notes / To-Do Manager")

with st.form("note_form"):
    new_note = st.text_input("Write a new note or task:")
    submitted = st.form_submit_button("Add Note")
    if submitted and new_note:
        st.session_state.notes.append(new_note)
        db.save_note(new_note)
        st.success("Note added!")

if st.session_state.notes:
    st.subheader("📌 Your Notes:")
    for i, note in enumerate(st.session_state.notes, 1):
        st.write(f"{i}. {note}")

    if st.button("🗑️ Clear All Notes"):
        st.session_state.notes.clear()
        db.clear_notes()
        st.success("All notes cleared!")
else:
    st.info("No notes yet.")

# --- Footer ---
st.markdown("""
    <footer style="text-align: center; margin-top: 20px;">
        <hr>
        <p>Made with ❤️ by Maheen Arif</p>
        <p>Powered by <a href="https://generativeai.google/">Google Generative AI</a></p>
    </footer>
""", unsafe_allow_html=True)
