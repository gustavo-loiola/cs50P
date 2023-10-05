import pytest

from seasons import convert

def test_formats():
    assert convert("2022-08-02") == "Five hundred twenty-five thousand, six hundred minutes"
    with pytest.raises(SystemExit):
        convert("2022/08/02")
        convert("2022,08,02")
        convert("2022_08_02")
        convert("2022-08/02")
        convert("2022/08-02")
        convert("2022/8/2")
        convert("20/08/2022")
        convert("January 1, 1999")

def test_dates():
    with pytest.raises(SystemExit):
        convert("2000/31/12")
        convert("2000/12/40")
        convert("2000/00/20")
        convert("2000/10/00")
        convert("0000/01/01")
