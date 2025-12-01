# Imports
from utils.sentimental_analyzer import sentiment_analysis


# Test function
def test_sentiment_analysis():
    text1 = "I love MLOps"
    text2 = "I love AI"
    text3 = "I hate studying quantum computing"

    sentiment1 = sentiment_analysis(text1)
    sentiment2 = sentiment_analysis(text2)
    sentiment3 = sentiment_analysis(text3)

    assert sentiment1[0]["label"] == "POSITIVE"
    assert sentiment2[0]["label"] == "POSITIVE"
    assert sentiment3[0]["label"] == "NEGATIVE"
