from multimodal_chatbot import multimodal_response

def main():
    try:
        with open("data/sample_text.txt", "r", encoding="utf-8") as f:
            text_input = f.read()
    except FileNotFoundError:
        print("Error: sample_text.txt not found.")
        return
    
    image_description = "A medical chart showing patient data."
    response = multimodal_response(text_input, image_description)
    
    with open("outputs/generated_response.txt", "w", encoding="utf-8") as f:
        f.write(response)
    
    print("Generated Response:")
    print(response)

if __name__ == "__main__":
    main()