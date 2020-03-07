import pytest

from littlebit.cryptography.field import FieldElement


def test_number_range():
    with pytest.raises(ValueError):
        FieldElement(number=7, prime=3)


def test_ne():
    with pytest.raises(NotImplementedError):
        FieldElement(number=2, prime=31) == 0

    a = FieldElement(2, 31)
    b = FieldElement(2, 31)
    c = FieldElement(15, 31)
    assert a == b
    assert a != c
    assert not (a != b)


def test_add():
    with pytest.raises(TypeError):
        a = FieldElement(number=2, prime=31)
        b = FieldElement(number=2, prime=32)
        a + b

    a = FieldElement(2, 31)
    b = FieldElement(15, 31)
    assert a + b == FieldElement(17, 31)

    a = FieldElement(17, 31)
    b = FieldElement(21, 31)
    assert a + b == FieldElement(7, 31)


def test_sub():
    with pytest.raises(TypeError):
        a = FieldElement(number=2, prime=31)
        b = FieldElement(number=2, prime=32)
        a - b

    a = FieldElement(29, 31)
    b = FieldElement(4, 31)
    assert a - b == FieldElement(25, 31)

    a = FieldElement(15, 31)
    b = FieldElement(30, 31)
    assert a - b == FieldElement(16, 31)


def test_mul():
    with pytest.raises(TypeError):
        a = FieldElement(number=2, prime=31)
        b = FieldElement(number=2, prime=32)
        a * b

    a = FieldElement(24, 31)
    b = FieldElement(19, 31)
    assert a * b == FieldElement(22, 31)


def test_pow():
    a = FieldElement(17, 31)
    assert a ** 3 == FieldElement(15, 31)

    a = FieldElement(5, 31)
    assert a ** 5 == FieldElement(25, 31)

    a = FieldElement(17, 31)
    assert a ** -3 == FieldElement(29, 31)

    a = FieldElement(4, 31)
    assert a ** -4 == FieldElement(4, 31)


def test_div():
    with pytest.raises(TypeError):
        a = FieldElement(number=2, prime=31)
        b = FieldElement(number=2, prime=32)
        a / b

    a = FieldElement(3, 31)
    b = FieldElement(24, 31)
    assert a / b == FieldElement(4, 31)


def test_rmul():
    assert 5 * FieldElement(number=18, prime=31) == FieldElement(number=28, prime=31)
    assert -4 * FieldElement(number=11, prime=31) == FieldElement(number=18, prime=31)
