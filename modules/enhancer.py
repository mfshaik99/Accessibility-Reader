from textblob import TextBlob

def enhance(text):
    if not text.strip():
        return "⚠️ No text provided."
    corrected = str(TextBlob(text).correct())
    return corrected
