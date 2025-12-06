from dialog.manager import match_intent
from skills.weather import get_weather
from skills.recipe import get_recipe_steps
from skills.time import get_time, get_date
from skills.system_control import open_target
from skills.music import play_random
from skills.jokes import tell_joke
from skills.calculator import safe_eval
from skills.gk import ask_openai
from stt_tts.stt import listen
from stt_tts.tts import speak

def handle_intent(tag, text):
    if tag == "weather":
        return get_weather(text)
    elif tag == "recipe":
        return "\n".join(get_recipe_steps(text))
    elif tag == "time":
        return f"{get_time()} | {get_date()}"
    elif tag == "open":
        return open_target(text)
    elif tag == "music":
        return play_random()
    elif tag == "joke":
        return tell_joke()
    elif tag == "calculator":
        return safe_eval(text)
    elif tag == "gk":
        return ask_openai(text)
    elif tag == "exit":
        return "exit"
    return "I did not understand that."

def main():
    speak("Hello! I am your assistant. How can I help you today?")
    while True:
        print("Listening...")
        query = listen()
        if not query:
            continue
        tag, text = match_intent(query)
        print(f"Intent: {tag}, Text: {text}")
        response = handle_intent(tag, text)
        if response == "exit":
            speak("Goodbye!")
            break
        print(f"Assistant: {response}")
        speak(response)

if __name__ == "__main__":
    main()
