from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int
    a: int
    b: int

    @property
    def is_identity(self):
        return self.x is None and self.y is None

    def __post_init__(self):
        # Skip curve validation is point is at infinity, denoted by x=None and y=None.
        if self.is_identity:
            return

        # Check if the params satisfy the elliptic curve equation: y² = x³ + ax + b
        if self.y ** 2 != self.x ** 3 + self.a * self.x + self.b:
            raise ValueError(f"({self.x}, {self.y}) is not on the elliptic curve")

    def __repr__(self):
        # Special represenation for the Identity point
        if self.is_identity:
            return "I"

        return super().__repr__()

    def __eq__(self, other):
        return (
            self.x == other.x
            and self.y == other.y
            and self.a == other.a
            and self.b == other.b
        )

    def __add__(self, other):
        if self.a != other.a or self.b != other.b:
            raise TypeError(f"Points {self} and {other} are not on the same curve")

        ###############################################################################
        # Point Addition for X₁ or X₂ = I   (identity)                                #
        #                                                                             #
        # Formula:                                                                    #
        #     P + I = P                                                               #
        #     I + P = P                                                               #
        ###############################################################################
        if self.is_identity:
            return other

        if other.is_identity:
            return self

        ###############################################################################
        # Point Addition for X₁ = X₂   (additive inverse)                             #
        #                                                                             #
        # Formula:                                                                    #
        #     P + (-P) = I                                                            #
        #     (-P) + P = I                                                            #
        ###############################################################################
        if self.x == other.x and self.y != other.y:
            return type(self)(x=None, y=None, a=self.a, b=self.b)

        ###############################################################################
        # Point Addition for X₁ ≠ X₂   (line with slope)                              #
        #                                                                             #
        # Formula:                                                                    #
        #     S = (Y₂ - Y₁) / (X₂ - X₁)                                               #
        #     X₃ = S² - X₁ - X₂                                                       #
        #     Y₃ = S(X₁ - X₃) - Y₁                                                    #
        ###############################################################################
        if self.x != other.x:
            x1, x2 = self.x, other.x
            y1, y2 = self.y, other.y

            s = (y2 - y1) / (x2 - x1)
            x3 = s ** 2 - x1 - x2
            y3 = s * (x1 - x3) - y1

            return type(self)(x=x3, y=y3, a=self.a, b=self.b)

        ###############################################################################
        # Point Addition for P₁ = P₂   (vertical tangent)                             #
        #                                                                             #
        # Formula:                                                                    #
        #     S = ∞                                                                   #
        #     (X₃, Y₃) = I                                                            #
        ###############################################################################
        if self == other and self.y == 0 * self.x:  # 0 * self.x = I
            return type(self)(x=None, y=None, a=self.a, b=self.b)

        ###############################################################################
        # Point Addition for P₁ = P₂   (tangent with slope)                           #
        #                                                                             #
        # Formula:                                                                    #
        #     S = (3X₁² + a) / 2Y₁                         .. ∂(Y²) = ∂(X² + aX + b)  #
        #     X₃ = S² - 2X₁                                                           #
        #     Y₃ = S(X₁ - X₃) - Y₁                                                    #
        ###############################################################################
        if self == other:
            x1, y1, a = self.x, self.y, self.a

            s = (3 * x1 ** 2 + a) / (2 * y1)
            x3 = s ** 2 - 2 * x1
            y3 = s * (x1 - x3) - y1

            return type(self)(x=x3, y=y3, a=self.a, b=self.b)

    def __rmul__(self, coefficient):
        # Naive approach:
        #     result = type(self)(x=None, y=None, a=self.a, b=self.b)
        #     for _ in range(coefficient):
        #         result += self
        #     return result

        # Optimized approach using binary expansion
        # [TODO] - Add an explanation on how this works
        coef = coefficient
        current = self
        result = type(self)(x=None, y=None, a=self.a, b=self.b)
        while coef:
            if coef & 1:
                result += current
            current += current
            coef >>= 1
        return result
