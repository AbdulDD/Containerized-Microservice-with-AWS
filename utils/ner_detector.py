# Imports
from transformers import pipeline

# Named Entity Recognition (NER) Pipeline - identifies people, organizations, locations, etc.
ner_pipeline = pipeline("ner", model="dslim/bert-base-NER")

def ner_pipe(text):
    return ner_pipeline(text)
