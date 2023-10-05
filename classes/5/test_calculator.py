import sys
sys.path.append("/workspaces/62484725/class/0")

from calculator import square

import pytest

#instead of coding all the assert with try and except
#I'm gonna code a function for each case, in which is going to have some asserts
#and now, instead of using python PROGRAM.py to run the program (that doesn't have trys and excepts)
#I'm gonna use the extension 'pytest' (after installing it using: pip install pytest)
#and run the program as 'pytest PROGRAM.py'

def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_positive():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0


def test_str():
    with pytest.raises(TypeError):
        square("cat")