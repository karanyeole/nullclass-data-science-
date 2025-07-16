import streamlit as st
from sentiment_chatbot import sentiment_response

def main():
    st.title("Sentiment Analysis Chatbot")
    query = st.text_input("Enter your query:")
    if query:
        response = sentiment_response(query)
        st.write(f"Response: {response}")
        with open("outputs/sentiment_output.txt", "w", encoding="utf-8") as f:
            f.write(response)

if __name__ == "__main__":
    main()