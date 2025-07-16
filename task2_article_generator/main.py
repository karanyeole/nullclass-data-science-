import json
import os

# JSON structure for task2_article_generator/notebook.ipynb
notebook_content = {
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Task 2: Article Generator Chatbot\n",
    "\n",
    "Tests three LLMs for article generation and evaluates their performance."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": [
    "from article_generator import generate_article\n",
    "\n",
    "# Load prompt\n",
    "with open('data/sample_prompt.txt', 'r', encoding='utf-8') as f:\n",
    "    prompt = f.read()\n",
    "\n",
    "# Test models\n",
    "models = ['distilgpt2', 'gpt2', 'facebook/bart-large']\n",
    "for model in models:\n",
    "    article = generate_article(prompt, model)\n",
    "    print(f'Model: {model}')\n",
    "    print(f'Article: {article}')\n",
    "    with open(f'outputs/generated_article_{model}.txt', 'w', encoding='utf-8') as f:\n",
    "        f.write(article)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

# Define the path for the notebook
path = os.path.join("task2_article_generator", "notebook.ipynb")

# Write the notebook file
with open(path, "w", encoding="utf-8") as f:
    json.dump(notebook_content, f, indent=1)

print("✅ Task 2 notebook.ipynb created successfully.")
