import pytest
from utils.ner_detector import ner_pipe


def test_ner_detector():
    # test samples
    text1 = "Microsoft"
    text2 = "John"

    # Inferences
    ner1 = ner_pipe(text1)
    ner2 = ner_pipe(text2)

    # assert the outptus
    assert ner1[0]['entity'] == 'B-ORG'
    assert ner2[0]['entity'] == 'B-'
