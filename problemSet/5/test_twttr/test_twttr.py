import sys

sys.path.append("/workspaces/62484725/problemSet2/twttr")
from twttr import shorten


def test_lower_vowel():
    vowels = ["a", "e", "i", "o", "u"]
    for vowel in vowels:
        assert shorten(vowel) == ""


def test_upper_vowel():
    vowels = ["A", "E", "I", "O", "U"]
    for vowel in vowels:
        assert shorten(vowel) == ""


def test_number():
    assert shorten("Te5t") == "T5t"
    assert shorten("Th15 is 4 t3st") == "Th15 s 4 t3st"


def test_punctuation():
    assert shorten("What's your name?") == "Wht's yr nm?"
