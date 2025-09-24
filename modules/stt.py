from transformers import pipeline

stt_model = pipeline("automatic-speech-recognition", model="openai/whisper-small")

def transcribe_file(file_path):
    try:
        result = stt_model(file_path)
        return result['text']
    except Exception as e:
        return f"⚠️ Transcription failed: {e}"
