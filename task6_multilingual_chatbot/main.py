from multilingual_chatbot import multilingual_response

def main():
    try:
        with open("data/sample_queries.txt", "r", encoding="utf-8") as f:
            queries = f.read().splitlines()
    except FileNotFoundError:
        print("Error: sample_queries.txt not found.")
        return
    
    for query in queries:
        response = multilingual_response(query)
        with open("outputs/responses.txt", "a", encoding="utf-8") as f:
            f.write(f"Query: {query}\nResponse: {response}\n\n")
        print(f"Query: {query}")
        print(f"Response: {response}\n")

if __name__ == "__main__":
    main()