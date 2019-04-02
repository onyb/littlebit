import attr


@attr.s
class FieldElement:
    number = attr.ib()
    prime = attr.ib()

    @number.validator
    def _check_number(self, attribute, value):
        if not (0 <= value < self.prime):
            raise ValueError(f"{value} not in field range 0 to {self.prime - 1}.")

    def __eq__(self, other: "FieldElement") -> bool:
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime

    def __ne__(self, other: "FieldElement") -> bool:
        return not (self == other)

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
        # Ex: a**-3
        #           == a**-3 * a**p-1   .. [using FLT]
        #           == a**p-4
        #           == a**p-4 * a**p-1  .. [using FLT]
        #           == a**2p-5
        #
        # We're adding p-1 to the exp in a**exp, at each round. We repeat this
        # until exp is positive. Code snippet below:
        #     n = exponent
        #     while n < 0:
        #         n += p-1
        #
        # The above is equivalent to doing exp % p-1, which also ensures that the
        # result is positive. [TODO] - Why?

        return self.__class__(
            number=pow(
                self.number,
                exponent % (self.prime - 1),  # handle negative exponents
                self.prime,
            ),
            prime=self.prime,
        )

    def __truediv__(self, other: "FieldElement") -> "FieldElement":
        if self.prime != other.prime:
            raise TypeError("Cannot divide two numbers in different Fields")

        # Use Fermat's Little Theorem:
        #     (n**p-1) % p == 1
        # means:
        #     1/n == n**p-2

        other_inverse = other ** (self.prime - 2)

        return self.__class__(
            number=(self.number * other_inverse.number) % self.prime, prime=self.prime
        )

    def __rmul__(self, coefficient):
        """
        Support operations like 3 * <FieldElement>
        """
        return type(self)(
            number=(self.number * coefficient) % self.prime, prime=self.prime
        )
