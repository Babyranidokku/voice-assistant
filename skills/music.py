import os, random
from dotenv import load_dotenv
from playsound import playsound
load_dotenv()
MUSIC_FOLDER = os.getenv("MUSIC_FOLDER","./music")
def play_random():
    if not os.path.exists(MUSIC_FOLDER): return "No music folder found"
    files = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith(".mp3")]
    if not files: return "No music found"
    track = random.choice(files)
    playsound(os.path.join(MUSIC_FOLDER, track))
    return f"Playing {track}"