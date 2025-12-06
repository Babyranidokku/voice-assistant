import speech_recognition as sr

def listen():
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Say something...")
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source, phrase_time_limit=5)

        try:
            text = r.recognize_google(audio)
            return text.lower()
        except:
            return ""

    except Exception as e:
        print(f"Microphone Error: {e}")
        return ""
