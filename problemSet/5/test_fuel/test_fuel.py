import pytest

from fuel import convert, gauge


def test_return_percentage():
    assert convert("1/2") == 50
    assert convert("1/1") == 100
    assert convert("0/2") == 0


def test_not_integer():
    with pytest.raises(ValueError):
        convert("1.3/2")
        convert("1/2.5")
        convert("cat/2")
        convert("cat/dog")


def test_zero():
    assert convert("0/2") == 0
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_round():
    assert convert("1/3") == 33
    assert convert("2/3") == 67
    assert convert("1/102") == 1


def test_x_higher():
    with pytest.raises(ValueError):
        convert("3/2")


def test_full():
    assert gauge(100) == "F"
    assert gauge(99) == "F"


def test_empty():
    assert gauge(1) == "E"
    assert gauge(0) == "E"


def test_percentage():
    assert gauge(89) == "89%"
    assert gauge(50) == "50%"
    assert gauge(2) == "2%"
