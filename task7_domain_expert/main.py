import streamlit as st
from domain_expert import load_arxiv_data, summarize_paper

def main():
    st.title("Domain Expert Chatbot")
    df = load_arxiv_data("data/arxiv_sample.json")
    if df is None:
        st.error("Failed to load arXiv dataset.")
        return
    
    query = st.text_input("Enter a topic or paper title:")
    if query:
        matching_papers = df[df['title'].str.contains(query, case=False, na=False)]
        if not matching_papers.empty:
            paper = matching_papers.iloc[0]
            summary = summarize_paper(paper['abstract'])
            st.write(f"Title: {paper['title']}")
            st.write(f"Summary: {summary}")
            with open("outputs/paper_summary.txt", "w", encoding="utf-8") as f:
                f.write(summary)
        else:
            st.write("No matching papers found.")

if __name__ == "__main__":
    main()