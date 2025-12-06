import json
from pathlib import Path
INTENTS_FILE = Path(__file__).parent / "intents.json"

with open(INTENTS_FILE, "r") as f:
    intents = json.load(f)
def match_intent(text):
    if not text:
        return ("none", None)

    text = text.lower()

    # Priority matching: more specific intents first
    priority_order = ["open", "recipe", "weather", "music", "joke", "calculator", "time"]

    # FIRST: check important intents
    for tag in priority_order:
        for intent in intents["intents"]:
            if intent["tag"] == tag:
                for pattern in intent["patterns"]:
                    if pattern in text:
                        return (tag, text)

    # Greeting should NOT override commands
    for intent in intents["intents"]:
        if intent["tag"] == "greeting":
            for pattern in intent["patterns"]:
                if text.startswith(pattern):  # greeting only if at start
                    return ("greeting", text)

    # Otherwise treat it as general knowledge
    return ("gk", text)
