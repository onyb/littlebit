from ecc import Point


def test_ne():
    a = Point(x=3, y=-7, a=5, b=7)
    b = Point(x=18, y=77, a=5, b=7)
    assert a != b
    assert not (a != a)


def test_add__x1_equals_x2():
    a = Point(x=None, y=None, a=5, b=7)
    b = Point(x=2, y=5, a=5, b=7)
    c = Point(x=2, y=-5, a=5, b=7)
    assert a + b == b
    assert b + a == b
    assert b + c == a


def test_add__x1_not_equals_x2():
    a = Point(x=3, y=7, a=5, b=7)
    b = Point(x=-1, y=-1, a=5, b=7)
    assert a + b == Point(x=2, y=-5, a=5, b=7)


def test_add__p1_equals_p2():
    a = Point(x=-1, y=1, a=5, b=7)
    assert a + a == Point(x=18, y=-77, a=5, b=7)
