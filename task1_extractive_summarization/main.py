from summarizer import extractive_summary
from evaluate import evaluate_summary

def main():
    try:
        with open("data/sample_document.txt", "r", encoding="utf-8") as f:
            document = f.read()
    except FileNotFoundError:
        print("Error: sample_document.txt not found.")
        return
    summary = extractive_summary(document, ratio=0.3)
    with open("outputs/summary_output.txt", "w", encoding="utf-8") as f:
        f.write(summary)
    try:
        with open("data/reference_summary.txt", "r", encoding="utf-8") as f:
            reference_summary = f.read()
        metrics = evaluate_summary(summary, reference_summary)
        print("Evaluation Metrics:")
        print(f"Precision: {metrics.get('precision', 0):.2f}")
        print(f"Recall: {metrics.get('recall', 0):.2f}")
        print(f"F1-Score: {metrics.get('f1_score', 0):.2f}")
    except FileNotFoundError:
        print("Error: reference_summary.txt not found.")
    except Exception as e:
        print(f"Evaluation error: {str(e)}")
    print("\nGenerated Summary:")
    print(summary)

if __name__ == "__main__":
    main()