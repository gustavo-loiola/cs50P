from plates import is_valid


def test_start_two_letters():
    assert is_valid("XX") == True
    assert is_valid("CS50") == True
    assert is_valid("CSCS50") == True
    assert is_valid("50CS") == False


def test_end_letters():
    assert is_valid("CS50A") == False


def test_zero():
    assert is_valid("CS5000") == True
    assert is_valid("CS05123") == False
    assert is_valid("0CS50") == False


def test_character_invalid():
    assert is_valid("CS50!") == False
    assert is_valid("CS,50") == False
    assert is_valid("C$50") == False
    assert is_valid("CS 50") == False


def test_amount_characters():
    assert is_valid("TW") == True
    assert is_valid("VAL123") == True
    assert is_valid("NOTVALIDTOOBIG") == False
    assert is_valid("S") == False


def test_starts_alphabetical():
    assert is_valid("AA") == True
    assert is_valid("AAAA12") == True
    assert is_valid("123AA") == False
    assert is_valid("0AAAA") == False
    assert is_valid("123") == False


def test_zeroplacement():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False


def test_lower():
    assert is_valid("AAAA12") == True
    assert is_valid("AAAA12") == True