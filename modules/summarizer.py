from transformers import pipeline

# Initialize the summarization pipeline (Hugging Face, free)
_summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize(text: str, max_length: int = 100, min_length: int = 30) -> str:
    """
    Summarize the given text using a free Hugging Face model.

    Args:
        text (str): The input text to summarize.
        max_length (int): Maximum length of the summary.
        min_length (int): Minimum length of the summary.

    Returns:
        str: The summarized text or an error message.
    """
    if not text or not text.strip():
        return "⚠️ No text provided."

    try:
        summary = _summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        return f"⚠️ Summarization failed: {e}"
