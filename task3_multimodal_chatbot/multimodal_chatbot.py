from transformers import pipeline

def multimodal_response(text_input, image_description=None):
    try:
        generator = pipeline("text-generation", model="distilgpt2")
        input_text = text_input
        if image_description:
            input_text += f" Image description: {image_description}"
        response = generator(input_text, max_length=100, num_return_sequences=1)[0]['generated_text']
        return response
    except Exception as e:
        return f"Error generating response: {str(e)}"