from um import count


def test_differentcharacters():
    assert count("um...") == 1
    assert count("um.") == 1
    assert count("um?") == 1
    assert count(" um ") == 1
    assert count("um, ") == 1


def test_sentences():
    assert count("hello, um, world") == 1
    assert count("hello, yummy") == 0
    assert count("Um, yummy") == 1


def test_capitalized():
    assert count("Um, thanks") == 1
    assert count("I don't know. Um... thanks!") == 1
    assert count("UM... THANKS") == 1
