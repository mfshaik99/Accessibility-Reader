from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

_summarizer = TextRankSummarizer()

def summarize(text, sentences_count=3):
    if not text or len(text.split()) < 5:
        return text
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summary = _summarizer(parser.document, sentences_count)
    return ' '.join(str(s) for s in summary)
