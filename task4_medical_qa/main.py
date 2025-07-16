import streamlit as st
from medical_qa import load_medquad_data, extract_entities, retrieve_answer

def main():
    st.title("Medical Q&A Chatbot")
    df = load_medquad_data("data/medquad.csv")
    if df is None:
        st.error("Failed to load MedQuAD dataset.")
        return
    
    query = st.text_input("Enter your medical question:")
    if query:
        entities = extract_entities(query)
        answer = retrieve_answer(query, df)
        st.write(f"Entities detected: {entities}")
        st.write(f"Answer: {answer}")

if __name__ == "__main__":
    main()