import pytest

from littlebit.cryptography import Point


def test_ne():
    a = Point(x=3, y=-7, a=5, b=7)
    b = Point(x=18, y=77, a=5, b=7)
    assert a != b
    assert not (a != a)


def test_add_different_curves():
    with pytest.raises(TypeError):
        a = Point(x=2, y=5, a=5, b=7)
        b = Point(x=3, y=0, a=-9, b=0)
        a + b


def test_add__additive_inverse():
    a = Point(x=None, y=None, a=5, b=7)
    b = Point(x=2, y=5, a=5, b=7)
    c = Point(x=2, y=-5, a=5, b=7)
    assert a + b == b
    assert b + a == b
    assert b + c == a


def test_add__line_with_slope():
    a = Point(x=3, y=7, a=5, b=7)
    b = Point(x=-1, y=-1, a=5, b=7)
    assert a + b == Point(x=2, y=-5, a=5, b=7)


def test_add__tangent_with_slope():
    a = Point(x=-1, y=1, a=5, b=7)
    assert a + a == Point(x=18, y=-77, a=5, b=7)


def test_add__vertical_tangent():
    a = Point(x=3, y=0, a=-9, b=0)
    assert a + a == Point(x=None, y=None, a=-9, b=0)
