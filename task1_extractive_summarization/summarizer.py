import nltk
from summa import summarizer
nltk.download('punkt')

def extractive_summary(text, ratio=0.3):
    try:
        summary = summarizer.summarize(text, ratio=ratio)
        if not summary:
            return "Summary could not be generated. Input may be too short or invalid."
        return summary
    except Exception as e:
        return f"Error generating summary: {str(e)}"