from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from transformers import pipeline

def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(text)
    if scores['compound'] >= 0.05:
        return "positive"
    elif scores['compound'] <= -0.05:
        return "negative"
    else:
        return "neutral"

def sentiment_response(query):
    try:
        sentiment = analyze_sentiment(query)
        generator = pipeline("text-generation", model="distilgpt2")
        response = generator(query, max_length=100, num_return_sequences=1)[0]['generated_text']
        response += f" (Sentiment: {sentiment})"
        return response
    except Exception as e:
        return f"Error generating response: {str(e)}"