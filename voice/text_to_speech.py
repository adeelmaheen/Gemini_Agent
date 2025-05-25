from gtts import gTTS
import tempfile

def speak_text(text, lang='en'):
    try:
        tts = gTTS(text=text, lang=lang)
        temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix='.mp3')
        tts.save(temp_audio.name)
        return temp_audio.name
    except Exception as e:
        print(f"[TTS Error] Failed to generate speech: {e}")
        return None
