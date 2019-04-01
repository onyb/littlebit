import pytest

from littlebit.ecc import FieldElement


def test_number_range():
    with pytest.raises(ValueError):
        FieldElement(number=7, prime=3)


def test_ne():
    a = FieldElement(2, 31)
    b = FieldElement(2, 31)
    c = FieldElement(15, 31)
    assert a == b
    assert a != c
    assert not (a != b)


def test_add():
    a = FieldElement(2, 31)
    b = FieldElement(15, 31)
    assert a + b == FieldElement(17, 31)

    a = FieldElement(17, 31)
    b = FieldElement(21, 31)
    assert a + b == FieldElement(7, 31)


def test_sub():
    a = FieldElement(29, 31)
    b = FieldElement(4, 31)
    assert a - b == FieldElement(25, 31)

    a = FieldElement(15, 31)
    b = FieldElement(30, 31)
    assert a - b == FieldElement(16, 31)


def test_mul():
    a = FieldElement(24, 31)
    b = FieldElement(19, 31)
    assert a * b == FieldElement(22, 31)


def test_pow():
    a = FieldElement(17, 31)
    assert a ** 3 == FieldElement(15, 31)

    a = FieldElement(5, 31)
    b = FieldElement(18, 31)
    assert a ** 5 * b == FieldElement(16, 31)


def test_div():
    a = FieldElement(3, 31)
    b = FieldElement(24, 31)
    assert a / b == FieldElement(4, 31)

    a = FieldElement(17, 31)
    assert a ** -3 == FieldElement(29, 31)

    a = FieldElement(4, 31)
    b = FieldElement(11, 31)
    assert a ** -4 * b == FieldElement(13, 31)
