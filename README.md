Data Science Internship Project
This repository contains implementations for all eight tasks assigned by NullClass for the Data Science Internship (March 17, 2025 - July 17, 2025). Each task is organized in its own subfolder with code, data, and documentation.
Setup Instructions

Clone the Repository:
git clone <your-repo-url>
cd data_science_internship


Create and Activate Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:
pip install -r requirements.txt

For task-specific dependencies, navigate to each task folder and run:
pip install -r <task_folder>/requirements.txt


Run a Task:

Navigate to the task folder (e.g., cd task1_extractive_summarization).
Run the main script:python main.py


For tasks with Streamlit (Tasks 4, 7, 8):streamlit run main.py


Check outputs/ for results and notebook.ipynb for experimentation.


Datasets:

Task 4: Download MedQuAD dataset from https://github.com/abachaa/MedQuAD and place in task4_medical_qa/data/.
Task 7: Download arXiv dataset from https://www.kaggle.com/datasets/Cornell-University/arxiv and place a sample in task7_domain_expert/data/.
If files are large, they are linked in task-specific README.md files (Google Drive).



Submission

GitHub: Push this repository to GitHub and share the URL with training@nullclass.com.
Large Files: If datasets or models are large, they are uploaded to Google Drive with links in task-specific README.md.
Internship Report: Included in each task folder as report.docx (to be created by you).
Daily Report: Submit daily progress at https://dailyreport.nullclass.com/.

Task Overview

Task 1: Extractive Summarization - Summarizes documents using TextRank.
Task 2: Article Generator Chatbot - Uses three open-source LLMs to generate articles.
Task 3: Multi-Modal Chatbot - Handles text and image inputs (simulated with text-based responses).
Task 4: Medical Q&A Chatbot - Uses MedQuAD dataset with Streamlit UI.
Task 5: Dynamic Knowledge Base - Updates chatbot knowledge periodically.
Task 6: Multilingual Chatbot - Supports three additional languages.
Task 7: Domain Expert Chatbot - Uses arXiv dataset for computer science queries with Streamlit UI.
Task 8: Sentiment Analysis Chatbot - Detects and responds to user emotions with Streamlit UI.

Contact
For queries, email training@nullclass.com.