# gk.py
import os
from dotenv import load_dotenv
import openai

# Load environment variables
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(PROJECT_ROOT, ".env"))

OPENAI_KEY = os.getenv("OPENAI_API_KEY")

# gk.py
import openai

def ask_openai(text, api_key):
    if not api_key:
        return "Provide OpenAI API key to answer."
    openai.api_key = api_key
    try:
        response = openai.Completion.create(
            engine="textdavinci-003",
            prompt=text,
            max_tokens=100
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error in GK API: {e}"
