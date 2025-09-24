import os
import time
from gtts import gTTS
import pyttsx3

def speak(text: str, out_dir="static/audio"):
    if not text or not text.strip():
        return None
    os.makedirs(out_dir, exist_ok=True)
    # unique filename
    base = f"tts_{int(time.time()*1000)}.mp3"
    path = os.path.join(out_dir, base)
    try:
        tts = gTTS(text=text, lang='en')
        tts.save(path)
        return base
    except Exception:
        # fallback offline
        try:
            engine = pyttsx3.init()
            engine.save_to_file(text, path)
            engine.runAndWait()
            return base
        except Exception:
            return None
