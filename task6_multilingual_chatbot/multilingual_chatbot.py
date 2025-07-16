from transformers import pipeline
from langdetect import detect

def multilingual_response(query):
    try:
        lang = detect(query)
        translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-es" if lang == "es" else "Helsinki-NLP/opus-mt-en-fr")
        generator = pipeline("text-generation", model="distilgpt2")
        
        if lang != "en":
            query = translator(query, src_lang=lang, tgt_lang="en")[0]['translation_text']
        
        response = generator(query, max_length=100, num_return_sequences=1)[0]['generated_text']
        
        if lang != "en":
            response = translator(response, src_lang="en", tgt_lang=lang)[0]['translation_text']
        
        return response
    except Exception as e:
        return f"Error generating response: {str(e)}"