import pytest

from littlebit.ecc import FieldElement, Point


def test_on_curve():
    prime = 223
    a = FieldElement(0, prime)
    b = FieldElement(7, prime)
    valid_points = ((192, 105), (17, 56), (1, 193))
    invalid_points = ((200, 119), (42, 99))
    for x_raw, y_raw in valid_points:
        x = FieldElement(x_raw, prime)
        y = FieldElement(y_raw, prime)
        Point(x, y, a, b)
    for x_raw, y_raw in invalid_points:
        x = FieldElement(x_raw, prime)
        y = FieldElement(y_raw, prime)
        with pytest.raises(ValueError):
            Point(x, y, a, b)


def test_add():
    # tests the following additions on curve y^2=x^3-7 over F_223:

    prime = 223
    a = FieldElement(0, prime)
    b = FieldElement(7, prime)

    additions = (
        # (x1, y1, x2, y2, x3, y3)
        (192, 105, 17, 56, 170, 142),
        (47, 71, 117, 141, 60, 139),
        (143, 98, 76, 66, 47, 71),
    )

    for x1, y1, x2, y2, x3, y3 in additions:
        p1 = Point(x=FieldElement(x1, prime), y=FieldElement(y1, prime), a=a, b=b)
        p2 = Point(x=FieldElement(x2, prime), y=FieldElement(y2, prime), a=a, b=b)
        p3 = Point(x=FieldElement(x3, prime), y=FieldElement(y3, prime), a=a, b=b)

        assert p1 + p2 == p3


@pytest.mark.parametrize(
    "scalar, x, y, expected_x, expected_y",
    [
        (2, 192, 105, 49, 71),
        (2, 143, 98, 64, 168),
        (2, 47, 71, 36, 111),
        (4, 47, 71, 194, 51),
        (8, 47, 71, 116, 55),
        (21, 47, 71, None, None),
    ],
)
def test_scalar_mul_using_addition(scalar, x, y, expected_x, expected_y):
    a = FieldElement(0, 223)
    b = FieldElement(7, 223)

    x1 = FieldElement(x, 223)
    y1 = FieldElement(y, 223)

    x2 = expected_x and FieldElement(expected_x, 223)
    y2 = expected_y and FieldElement(expected_y, 223)

    p = Point(x1, y1, a, b)

    res = Point(x=None, y=None, a=a, b=b)
    for _ in range(scalar):
        res = res + p

    assert res == Point(x2, y2, a, b)

