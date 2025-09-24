from transformers import pipeline

# Load free Whisper ASR model from Hugging Face
_stt_model = pipeline("automatic-speech-recognition", model="openai/whisper-small")

def transcribe_file(file_path: str) -> str:
    """
    Convert audio file to text using Hugging Face Whisper model.

    Args:
        file_path (str): Path to the audio file.

    Returns:
        str: Transcribed text or error message.
    """
    if not file_path:
        return "⚠️ No audio file provided."

    try:
        result = _stt_model(file_path)
        return result['text']
    except Exception as e:
        return f"⚠️ Transcription failed: {e}"
