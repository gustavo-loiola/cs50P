import pytest
from working import convert


def test_verify_time():
    '''
    assert verify_time(["11", "59", "AM"]) == True
    assert verify_time(["0", "0", "PM"]) == True
    assert verify_time(["12", "0", "AM"]) == True
    assert verify_time(["12", "1", "AM"]) == True
    assert verify_time(["17", "47", "PM"]) == False
    assert verify_time(["10", "78", "AM"]) == False
    assert verify_time(["3", "60", "AM"]) == False
    '''
    
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:30 PM") == "09:00 to 17:30"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    with pytest.raises(ValueError):
        convert("12:60 AM to 10 PM")
        convert("13 PM to 5 AM")
        convert("3 AM to 13 AM")
        convert("2AM to 3PM")

    with pytest.raises(ValueError):
        convert("9 AM  5 PM")
        convert("9 AM - 5 PM")
        convert("9 AM, 5 PM")
        convert("9 - 5")

    with pytest.raises(ValueError):
        convert("12:60 AM to 10 PM")
        convert("13 PM to 5 AM")
        convert("3 AM to 13 AM")

'''
def test_formats():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:30 PM") == "09:00 to 17:30"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    with pytest.raises(ValueError):
        convert("12:60 AM to 10 PM")
        convert("13 PM to 5 AM")
        convert("3 AM to 13 AM")
        convert("2AM to 3PM")

def test_omitting():
    with pytest.raises(ValueError):
        convert("9 AM  5 PM")
        convert("9 AM - 5 PM")
        convert("9 AM, 5 PM")
        convert("9 - 5")

def test_outofrange():
    with pytest.raises(ValueError):
        convert("12:60 AM to 10 PM")
        convert("13 PM to 5 AM")
        convert("3 AM to 13 AM")
'''
