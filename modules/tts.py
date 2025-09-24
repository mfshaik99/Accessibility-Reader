import os
import time
from TTS.api import TTS

# Load a free TTS model from Hugging Face
_tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")

def speak(text: str, out_dir: str = "static/audio") -> str:
    """
    Convert text to speech using a free Hugging Face TTS model.

    Args:
        text (str): Input text.
        out_dir (str): Directory to save audio file.

    Returns:
        str: Path to generated audio file or None if failed.
    """
    if not text or not text.strip():
        return None

    os.makedirs(out_dir, exist_ok=True)
    filename = f"tts_{int(time.time()*1000)}.wav"
    path = os.path.join(out_dir, filename)

    try:
        _tts.tts_to_file(text=text, file_path=path)
        return filename
    except Exception as e:
        print(f"TTS failed: {e}")
        return None
