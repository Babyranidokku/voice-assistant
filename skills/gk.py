import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_API_KEY")
def ask_openai(text):
    if not OPENAI_KEY: return "Provide OpenAI API key to answer."
    import openai
    openai.api_key = OPENAI_KEY
    try:
        response = openai.Completion.create(engine="textdavinci-003",prompt=text,max_tokens=100)
        return response.choices[0].text.strip()
    except: return "Error in GK API"