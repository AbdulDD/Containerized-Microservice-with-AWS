# Imports
from transformers import pipeline

# Named Entity Recognition (NER) Pipeline
ner_pipeline = pipeline("ner", model="dslim/bert-base-NER")


# function
def ner_pipe(text):
    return ner_pipeline(text)
