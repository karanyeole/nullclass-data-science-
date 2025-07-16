import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_medquad_data(file_path):
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        return None

def extract_entities(query):
    keywords = ['symptom', 'disease', 'treatment']
    entities = [kw for kw in keywords if kw in query.lower()]
    return entities

def retrieve_answer(query, df):
    try:
        vectorizer = TfidfVectorizer()
        question_vectors = vectorizer.fit_transform(df['question'].tolist() + [query])
        similarities = cosine_similarity(question_vectors[-1], question_vectors[:-1])
        best_match_idx = similarities.argmax()
        return df.iloc[best_match_idx]['answer']
    except Exception as e:
        return f"Error retrieving answer: {str(e)}"