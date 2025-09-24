from textblob import TextBlob

def enhance(text):
    if not text or not text.strip():
        return "⚠️ No text provided."
    blob = TextBlob(text)
    corrected = str(blob.correct())  # correct spelling
    return corrected
