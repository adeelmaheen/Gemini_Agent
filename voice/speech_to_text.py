# import sounddevice as sd
# import speech_recognition as sr
# import io
# import wave

# def record_and_transcribe(duration=5, samplerate=16000):
#     recognizer = sr.Recognizer()

#     try:
#         # Step 1: Record audio using sounddevice
#         try:
#             audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
#             sd.wait()
#         except Exception as e:
#             return f"🎙️ Recording Error: {e}"

#         # Step 2: Save to BytesIO buffer as WAV
#         try:
#             audio_bytes = io.BytesIO()
#             with wave.open(audio_bytes, 'wb') as wf:
#                 wf.setnchannels(1)
#                 wf.setsampwidth(2)
#                 wf.setframerate(samplerate)
#                 wf.writeframes(audio_data.tobytes())
#             audio_bytes.seek(0)
#         except Exception as e:
#             return f"💾 Audio Saving Error: {e}"

#         # Step 3: Convert to recognizer-readable format
#         try:
#             audio_source = sr.AudioFile(audio_bytes)
#             with audio_source as source:
#                 audio = recognizer.record(source)
#         except Exception as e:
#             return f"📦 Audio Loading Error: {e}"

#         # Step 4: Transcribe using Google Speech API
#         try:
#             return recognizer.recognize_google(audio)
#         except sr.UnknownValueError:
#             return "❓ Could not understand the audio."
#         except sr.RequestError as e:
#             return f"🌐 API Request Error: {e}"
#         except Exception as e:
#             return f"🧠 Transcription Error: {e}"

#     except Exception as e:
#         return f"❗ Unexpected Error: {e}"
