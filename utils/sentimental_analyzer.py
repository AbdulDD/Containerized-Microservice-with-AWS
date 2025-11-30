# Imports
from transformers import pipeline

# Sentiment Analysis Pipeline
sentiment_analysis_pipeline = pipeline(
    "sentiment-analysis", 
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
    )

# Inference
def sentiment_analysis(text):
    return sentiment_analysis_pipeline(text)
