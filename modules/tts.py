from TTS.api import TTS

# Choose a free model
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")

def speak(text, out_dir="static/audio"):
    if not text.strip():
        return None
    os.makedirs(out_dir, exist_ok=True)
    filename = f"{out_dir}/tts_{int(time.time()*1000)}.wav"
    tts.tts_to_file(text=text, file_path=filename)
    return filename
