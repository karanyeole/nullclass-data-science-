import pandas as pd
from summa import summarizer

def load_arxiv_data(file_path):
    try:
        return pd.read_json(file_path, lines=True)
    except Exception as e:
        return None

def summarize_paper(abstract):
    try:
        return summarizer.summarize(abstract, ratio=0.3)
    except Exception as e:
        return f"Error summarizing paper: {str(e)}"