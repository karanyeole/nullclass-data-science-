from sklearn.metrics import precision_score, recall_score, f1_score
from nltk.tokenize import sent_tokenize

def evaluate_article(generated_article, reference_article):
    try:
        gen_sentences = sent_tokenize(generated_article)
        ref_sentences = sent_tokenize(reference_article)
        all_sentences = list(set(gen_sentences + ref_sentences))
        y_true = [1 if sent in ref_sentences else 0 for sent in all_sentences]
        y_pred = [1 if sent in gen_sentences else 0 for sent in all_sentences]
        precision = precision_score(y_true, y_pred, zero_division=0)
        recall = recall_score(y_true, y_pred, zero_division=0)
        f1 = f1_score(y_true, y_pred, zero_division=0)
        return {
            "precision": precision,
            "recall": recall,
            "f1_score": f1
        }
    except Exception as e:
        return {"error": f"Evaluation failed: {str(e)}"}