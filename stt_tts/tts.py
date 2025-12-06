from gtts import gTTS
import playsound
import tempfile
import os
import time

def speak(text):
    try:
        # Create temp mp3 file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            tts = gTTS(text=text, lang='en')
            tts.save(fp.name)
            temp_path = fp.name

        playsound.playsound(temp_path)
        time.sleep(0.5)  # Allow playback to complete
        os.remove(temp_path)  # Delete after playing

    except Exception as e:
        print(f"TTS Error: {e}")
