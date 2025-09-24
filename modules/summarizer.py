from transformers import pipeline

# NOTE: model is downloaded on first run. Requires internet for first run.
_summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=-1)

def summarize(text: str, min_length=30, max_length=150):
    if not text or not text.strip():
        return "⚠️ No text provided."
    words = text.split()
    if len(words) < 30:
        # For short text, give a short rewrite instead of failing
        return "⚠️ Text is short — summarization may not change it significantly.\n\n" + text
    try:
        out = _summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
        return out[0]['summary_text']
    except Exception as e:
        return f"⚠️ Summarization failed: {e}"
