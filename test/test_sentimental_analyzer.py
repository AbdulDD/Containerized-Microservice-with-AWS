# Imports
from utils.sentimental_analyzer import sentiment_analysis

text1 = "I love MLOps"
text2 = "I love AI"
text3 = "I hate studing quantum computing"


# Inferences
sentiment1 = sentiment_analysis(text1)
sentiment2 = sentiment_analysis(text2)
sentiment3 = sentiment_analysis(text3)

# print them
print(sentiment1)
print(sentiment2)
print(sentiment3)