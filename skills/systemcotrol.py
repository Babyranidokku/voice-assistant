import webbrowser

def open_target(text):
   if "youtube" in text: webbrowser.open("https://youtube.com"); return"Opening YouTube"
   elif "google" in text: webbrowser.open("https://google.com"); return"Opening Google"
   return "Cannot open specified app/site"