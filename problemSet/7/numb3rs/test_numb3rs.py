import pytest

from numb3rs import validate


def test_validate():
    assert validate("0.0.0.0") == True
    assert validate("275.3.6.28") == False
    assert validate("275.300.6.28") == False
    assert validate("27.3.600.28") == False
    assert validate("27.3.6.2800") == False
    assert validate("25.3.6.28.2344.123") == False
    assert validate("25;234;231;231") == False


'''
def test_in_range():
    assert in_range(0) == True
    assert in_range(123) == True
    assert in_range(444) == False
    with pytest.raises(NameError):
        in_range(cat)
'''