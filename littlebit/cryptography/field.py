from dataclasses import dataclass


@dataclass
class FieldElement:
    number: int
    prime: int

    def __post_init__(self):
        if not (0 <= self.number < self.prime):
            raise ValueError(f"{self.number} not in field range 0 to {self.prime - 1}.")

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, FieldElement):
            raise NotImplementedError

        return self.number == other.number and self.prime == other.prime

    def __add__(self, other: "FieldElement") -> "FieldElement":
        if self.prime != other.prime:
            raise TypeError("Cannot add two numbers in different Fields")

        return self.__class__(
            number=(self.number + other.number) % self.prime, prime=self.prime
        )

    def __sub__(self, other: "FieldElement") -> "FieldElement":
        if self.prime != other.prime:
            raise TypeError("Cannot subtract two numbers in different Fields")

        return self.__class__(
            number=(self.number - other.number) % self.prime, prime=self.prime
        )

    def __mul__(self, other: "FieldElement") -> "FieldElement":
        if self.prime != other.prime:
            raise TypeError("Cannot multiply two numbers in different Fields")

        return self.__class__(
            number=(self.number * other.number) % self.prime, prime=self.prime
        )

    def __pow__(self, exponent: int) -> "FieldElement":
        # Dealing with negative exponents:
        # Ex: a⁻³
        #         = a⁻³ x aᵖ⁻¹   .. [using Fermat's Little Theorem]
        #         = aᵖ⁻⁴
        #         = aᵖ⁻⁴ x aᵖ⁻¹  .. [using Fermat's Little Theorem]
        #         = a²ᵖ⁻⁵
        #
        # We're adding p-1 to the exp in a**exp, at each round. We repeat this
        # until exp is positive. Code snippet below:
        #     n = exponent
        #     while n < 0:
        #         n += p-1
        #
        # The above is equivalent to doing exp % p-1, which also ensures that the
        # result is positive. [TODO] - Explain me
        #
        # pow() in Python 3.8 can compute suitable power of the modular inverse.
        # Refs:
        #   - https://twitter.com/raymondh/status/1141290218407940097
        #   - https://bugs.python.org/issue36027

        return self.__class__(
            number=pow(
                self.number,
                exponent,
                self.prime,
            ),
            prime=self.prime,
        )

    def __truediv__(self, other: "FieldElement") -> "FieldElement":
        if self.prime != other.prime:
            raise TypeError("Cannot divide two numbers in different Fields")

        # Use Fermat's Little Theorem:
        #     (nᵖ⁻¹) % p == 1
        # means:
        #     1/n == nᵖ⁻²

        other_inverse = other ** (self.prime - 2)

        return self.__class__(
            number=(self.number * other_inverse.number) % self.prime, prime=self.prime
        )

    def __rmul__(self, coefficient: int) -> "FieldElement":
        """
        Scalar multiplication
        """
        return type(self)(
            number=(self.number * coefficient) % self.prime, prime=self.prime
        )
