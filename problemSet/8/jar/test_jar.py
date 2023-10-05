from jar import Jar
import pytest


def test_init():
    with pytest.raises(ValueError):
        jar = Jar(-1)
        jar = Jar(1.5)
        jar = Jar(1 / 9)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.withdraw(12)
    assert str(jar) == ""


def test_deposit():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(13)
        jar.deposit(-1)


def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(2)
    jar.withdraw(10)
    with pytest.raises(ValueError):
        jar.withdraw(100)
        jar.withdraw(-1)
