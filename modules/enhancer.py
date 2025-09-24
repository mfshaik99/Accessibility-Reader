from transformers import pipeline

# Load summarization model (free Hugging Face)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize(text):
    if not text.strip():
        return "⚠️ No text provided."
    summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
    return summary[0]['summary_text']

# Text enhancement can be done via GPT-3.5 free tier or Hugging Face T5 paraphrase model
paraphraser = pipeline("text2text-generation", model="Vamsi/T5_Paraphrase_Paws")

def enhance(text):
    if not text.strip():
        return "⚠️ No text provided."
    result = paraphraser(f"paraphrase: {text}", max_length=200)
    return result[0]['generated_text']
