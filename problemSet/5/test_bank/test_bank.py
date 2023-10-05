from bank import value


def test_hello():
    assert value("Hello") == 0


def test_hey():
    assert value("Hey") == 20


def test_whats():
    assert value("What's up") == 100


def test_uppercases():
    assert value("HELLO") == 0
    assert value("HEY") == 20
    assert value("WHATS") == 100


def test_lowercases():
    assert value("hello") == 0
    assert value("hey") == 20
    assert value("whats") == 100


def test_space():
    assert value("            Hello!") == 0


def test_space_end():
    assert value("Hello!             ") == 0
