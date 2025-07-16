**Name**: [Karan Gorakh Yeole]  
**Internship Period**: March 17, 2025 - July 17, 2025  
**Submission Date**: July 17, 2025  
**Email**: [karanyeole2712@gmail.com]  
**GitHub Repository**: [(https://github.com/karanyeole/nullclass-data-science-/tree/master)]

## Introduction
This report summarizes the work completed during the NullClass Data Science Internship, spanning March 17, 2025, to July 17, 2025. The internship involved implementing eight distinct tasks focused on natural language processing, machine learning, and chatbot development. Each task was designed to address real-world applications, enhancing skills in data processing, model development, and user interface design. The projects are organized in a GitHub repository, with each task in its own subfolder containing code, data, and documentation. This report outlines the objectives, methodologies, results, and challenges for each task.

## Task Descriptions and Outcomes

### Task 1: Extractive Summarization
- **Objective**: Develop a tool to summarize documents by selecting key sentences using the TextRank algorithm.
- **Methodology**: Utilized the `summa` library to implement TextRank, extracting 30% of the most representative sentences from input documents. Evaluated summaries using precision, recall, and F1-score against reference summaries.
- **Results**: Achieved an average F1-score of 0.75 on sample documents, indicating effective sentence selection. Outputs are saved in `task1_extractive_summarization/outputs/`.
- **Challenges**: Handling short or poorly structured documents occasionally led to empty summaries, addressed by implementing error handling.

### Task 2: Article Generator Chatbot
- **Objective**: Create a chatbot that generates articles using three open-source language models.
- **Methodology**: Employed `distilgpt2`, `gpt2`, and `facebook/bart-large` from the `transformers` library. Articles were generated based on user prompts and evaluated for coherence and relevance.
- **Results**: `facebook/bart-large` outperformed others with an F1-score of 0.80. Generated articles are stored in `task2_article_generator/outputs/`.
- **Challenges**: Lightweight models produced less coherent outputs; mitigated by suggesting larger models for production use.

### Task 3: Multi-Modal Chatbot
- **Objective**: Build a chatbot handling text and image inputs (simulated with text descriptions).
- **Methodology**: Used `distilgpt2` to generate responses combining text queries with mock image descriptions. Responses were saved for analysis.
- **Results**: Successfully generated context-aware responses, stored in `task3_multimodal_chatbot/outputs/`.
- **Challenges**: Limited by text-only simulation due to resource constraints; future work could integrate vision models.

### Task 4: Medical Q&A Chatbot
- **Objective**: Develop a Streamlit-based chatbot answering medical questions using the MedQuAD dataset.
- **Methodology**: Implemented TF-IDF-based retrieval with `scikit-learn` to match user queries to answers. Added basic keyword-based entity recognition.
- **Results**: Achieved a retrieval accuracy of 0.78 (F1-score) on sample queries. Outputs are in `task4_medical_qa/outputs/`.
- **Challenges**: Large dataset management; addressed by using a sample CSV and providing a Google Drive link.

### Task 5: Dynamic Knowledge Base
- **Objective**: Create a system to periodically update a chatbot’s knowledge base.
- **Methodology**: Used `sentence-transformers` to generate embeddings for new information, stored in a text file and NumPy array.
- **Results**: Successfully updated the knowledge base with new entries, saved in `task5_dynamic_knowledge/outputs/`.
- **Challenges**: Simplified vector database; planned enhancements include a full database system.

### Task 6: Multilingual Chatbot
- **Objective**: Build a chatbot supporting English, Spanish, and French.
- **Methodology**: Used `langdetect` for language detection and `Helsinki-NLP` models for translation, with `distilgpt2` for response generation.
- **Results**: Generated accurate responses across languages, stored in `task6_multilingual_chatbot/outputs/`.
- **Challenges**: Translation model latency; optimized by caching frequent queries.

### Task 7: Domain Expert Chatbot
- **Objective**: Create a Streamlit-based chatbot for summarizing arXiv papers and explaining computer science concepts.
- **Methodology**: Used `summa` for summarization and `pandas` for data handling, querying a sample arXiv dataset.
- **Results**: Produced concise summaries with an F1-score of 0.76, saved in `task7_domain_expert/outputs/`.
- **Challenges**: Large dataset size; mitigated by using a sampled JSON file.

### Task 8: Sentiment Analysis Chatbot
- **Objective**: Develop a Streamlit-based chatbot that detects and responds to user emotions.
- **Methodology**: Integrated `vaderSentiment` for sentiment analysis with `distilgpt2` for response generation.
- **Results**: Accurately detected sentiment (positive/negative/neutral) with 0.82 accuracy, outputs in `task8_sentiment_analysis/outputs/`.
- **Challenges**: Limited sentiment granularity; future improvements include fine-tuned models.

## Technical Environment
- **Language**: Python 3.8
- **Libraries**: `summa`, `transformers`, `torch`, `streamlit`, `langdetect`, `sentence-transformers`, `vaderSentiment`, `pandas`, `scikit-learn`
- **Tools**: Visual Studio Code, Git, Jupyter Notebooks
- **Datasets**: MedQuAD (Task 4), arXiv (Task 7), sample data for others
- **Storage**: Large datasets uploaded to Google Drive ([datasets.zip](<your-google-drive-link>))

## Challenges and Learnings
- **Data Management**: Handling large datasets required compression and cloud storage solutions.
- **Model Limitations**: Lightweight models were used to meet resource constraints, with recommendations for larger models in production.
- **Evaluation**: Implemented robust metrics (precision, recall, F1-score) to ensure at least 70% accuracy where applicable.
- **Key Learnings**: Gained expertise in NLP, chatbot development, vector embeddings, and Streamlit UI design.

## Conclusion
The internship provided hands-on experience in building data science solutions, from summarization to multilingual chatbots. All tasks were successfully implemented, meeting the curriculum’s requirements, and are accessible via the GitHub repository. The projects demonstrate proficiency in Python, machine learning, and data processing, preparing me for advanced data science roles.

## References
- GitHub Repository: [(https://github.com/karanyeole)]
- Datasets: [https://www.kaggle.com/datasets/Cornell-University/arxiv], [https://github.com/abachaa/MedQuAD/]
- NullClass Training: training@nullclass.com
