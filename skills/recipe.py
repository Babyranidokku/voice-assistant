import os, requests
from dotenv import load_dotenv
load_dotenv()
SPOON_KEY = os.getenv("SPOONACULAR_API")
def get_recipe_steps(text):
    dish = extract_dish(text)
    if not dish: return ["Please specify a dish"]
    if SPOON_KEY:
        try:
            url = f"https://api.spoonacular.com/recipes/complexSearch?query={dish}&number=1&apiKey={SPOON_KEY}"
            r = requests.get(url).json()
            if not r["results"]: return [f"No recipe found for {dish}"]
            return [f"Recipe steps for {dish} available via Spoonacular API"]
        except: return ["Recipe API error"]
    fallback = {"tea":["Boil water","Add tea leaves","Serve hot"]}
    return fallback.get(dish.lower(), [f"No recipe found for {dish}"])
def extract_dish(text):
    text = text.lower()
    triggers = ["recipe for", "make", "cook", "how to make"]
    for t in triggers:
        if t in text:
            return text.split(t)[-1].replace("please", "").strip()
    return ""
