from typing import cast

from ..point import Point
from .constants import A, B, Gx, Gy, N, P
from .field import S256FieldElement
from .signature import Signature


class S256Point(Point):
    def __init__(self, x, y, a=None, b=None):
        a, b = S256FieldElement(A), S256FieldElement(B)

        if isinstance(x, int) and isinstance(y, int):
            super().__init__(x=S256FieldElement(x), y=S256FieldElement(y), a=a, b=b)
        else:
            # x and y are either both None, or both instances of S256FieldElement
            super().__init__(x=x, y=y, a=a, b=b)

    def __rmul__(self, coefficient):
        return super().__rmul__(coefficient % N)

    def verify(self, z: int, signature: Signature) -> bool:
        s_inv = pow(signature.s, N - 2, N)
        u = (z * s_inv) % N
        v = (signature.r * s_inv) % N

        total = u * G + v * self
        return total.x.number == signature.r

    def sec(self, compressed: bool = True) -> bytes:
        """
        Returns binary version of the Standards for Efficient Cryptography (SEC)
        format.

        Uncompressed SEC format:
            1. Start with the prefix byte, 0x04
            2. Append the x coordinate in 32 bytes as a big-endian integer
            3. Append the y coordinate in 32 bytes as a big-endian integer

        Compressed SEC format:
            1. Start with the prefix byte.
               If y is even, it's 0x02; otherwise, it's 0x03
            2. Append the x coordinate in 32 bytes as a big-endian integer

        All 256 bit integers are encoded in 32 bytes, big-endian.
        """
        if compressed:
            if self.y.number % 2 == 0:
                return b"\x02" + self.x.number.to_bytes(32, "big")
            else:
                return b"\x03" + self.x.number.to_bytes(32, "big")
        else:
            return (
                b"\x04"
                + self.x.number.to_bytes(32, "big")
                + self.y.number.to_bytes(32, "big")
            )

    @classmethod
    def parse(cls, sec_bin: bytes) -> "S256Point":
        # Handle the case of uncompressed SEC format
        if sec_bin[0] == 4:  # check if prefix byte is b'\x04'
            return cls(
                x=int.from_bytes(sec_bin[1:33], "big"),
                y=int.from_bytes(sec_bin[33:65], "big"),
            )

        is_y_expected_to_be_even = sec_bin[0] == 2  # prefix byte is b'\x02'
        x = S256FieldElement(number=int.from_bytes(sec_bin[1:], "big"))

        # Right side of the equation: y² = x³ + 7
        alpha = x ** 3 + S256FieldElement(number=B)

        # [FIXME] - Dirty hack to indicate mypy about the true type
        alpha = cast(S256FieldElement, alpha)

        y = alpha.sqrt()

        if is_y_expected_to_be_even:
            if y.number % 2 == 0:
                return cls(x=x, y=y)
            else:
                return cls(x=x, y=S256FieldElement(P - y.number))
        else:
            if y.number % 2 == 0:
                return cls(x=x, y=S256FieldElement(P - y.number))
            else:
                return cls(x=x, y=y)


G = S256Point(x=Gx, y=Gy)
