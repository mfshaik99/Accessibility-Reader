import os
import speech_recognition as sr
from pydub import AudioSegment

def _convert_to_wav(in_path, out_path):
    # pydub handles many formats; requires ffmpeg installed
    audio = AudioSegment.from_file(in_path)
    audio.export(out_path, format="wav")

def transcribe_file(path):
    # Accepts many formats; convert to wav if necessary
    base, ext = os.path.splitext(path)
    wav_path = base + ".wav"
    if ext.lower() != ".wav":
        try:
            _convert_to_wav(path, wav_path)
        except Exception as e:
            return f"⚠️ Audio conversion failed: {e}"
    else:
        wav_path = path

    r = sr.Recognizer()
    try:
        with sr.AudioFile(wav_path) as source:
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.record(source)
        # Use Google Web Speech API (free for small usage)
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "⚠️ Could not understand audio."
    except sr.RequestError as e:
        return f"⚠️ Speech service error: {e}"
    except Exception as e:
        return f"⚠️ Transcription failed: {e}"
