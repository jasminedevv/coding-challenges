#! set encoding utf-8
import pytest
from censor import censor

text = "REPORT: The entity was clearly feline in nature and very friendly. It made adorable and very loud purring noises."
censored = ["feline", "very", "adorable", "purring"]

def test_censor():
    assert censor(text, censored) == "REPORT: The entity was clearly [REDACTED] in nature and [REDACTED] friendly. It made [REDACTED] and [REDACTED] loud [REDACTED] noises."