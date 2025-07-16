from sentence_transformers import SentenceTransformer
import numpy as np

def update_knowledge_base(new_info, knowledge_file="data/sample_knowledge.txt"):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    try:
        with open(knowledge_file, "r", encoding="utf-8") as f:
            existing = f.read().splitlines()
        existing.append(new_info)
        embeddings = model.encode(existing)
        np.save("outputs/knowledge_embeddings.npy", embeddings)
        with open("outputs/updated_knowledge.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(existing))
        return "Knowledge base updated."
    except Exception as e:
        return f"Error updating knowledge base: {str(e)}"