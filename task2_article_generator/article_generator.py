from transformers import pipeline

def generate_article(prompt, model_name="distilgpt2"):
    try:
        generator = pipeline("text-generation", model=model_name)
        article = generator(prompt, max_length=200, num_return_sequences=1)[0]['generated_text']
        return article
    except Exception as e:
        return f"Error generating article: {str(e)}"