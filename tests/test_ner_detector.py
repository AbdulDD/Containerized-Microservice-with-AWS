# Imports
from utils.ner_detector import ner_pipe


# Test function
def test_ner_detector():
    # test samples
    text1 = "Microsoft is a good company"
    text2 = "John is looking cool"

    # Inferences
    ner1 = ner_pipe(text1)
    ner2 = ner_pipe(text2)

    # assert the outptus
    assert ner1[0]["entity"] == "B-ORG"
    assert ner2[0]["entity"] == "B-PER"
