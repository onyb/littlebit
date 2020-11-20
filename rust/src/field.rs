use std::ops::{Add, Div, Mul, Sub};
use uint::construct_uint;

construct_uint! {
    // uint256 with 256 bits consisting of 4 x 64-bit words
    pub struct uint256(4);
}

#[derive(Eq, PartialEq, Debug, Copy, Clone)]
pub struct FieldElement {
    pub number: uint256,
    pub prime: uint256,
}

impl FieldElement {
    pub fn new(number: uint256, prime: uint256) -> Result<Self, String> {
        if number > prime {
            Err(format!(
                "{el} not in field range 0 to {p}.",
                el = number,
                p = prime - 1
            ))
        } else {
            Ok(Self {
                number,
                prime,
            })
        }
    }

    // ? [FIXME] - What's the standard way of dealing with negative exponents?
    //             Maybe use something other than uint256?
    pub fn pow(self, exponent: uint256) -> Result<Self, String> {
        Self::new(self.number.pow(exponent) % self.prime, self.prime)
    }

    pub fn neg_pow(self, exponent: uint256) -> Result<Self, String> {
        let modulo = self.prime - uint256::one();
        let n = (modulo - exponent) % modulo;
        self.pow(n)
    }
}

impl Add<FieldElement> for FieldElement {
    type Output = Result<Self, String>;

    fn add(self, other: Self) -> Self::Output {
        if self.prime != other.prime {
            Err(format!("Cannot add two elements in different fields"))
        } else {
            Self::new((self.number + other.number) % self.prime, self.prime)
        }
    }
}

impl Sub<FieldElement> for FieldElement {
    type Output = Result<Self, String>;

    fn sub(self, other: Self) -> Self::Output {
        if self.prime != other.prime {
            Err(format!("Cannot subtract two elements in different fields"))
        } else {
            Self::new(
                // Add self.prime to avoid uint256 overflow,
                // when self.number < other.number
                (self.number + self.prime - other.number) % self.prime,
                self.prime,
            )
        }
    }
}

impl Mul<FieldElement> for FieldElement {
    type Output = Result<Self, String>;

    fn mul(self, other: Self) -> Self::Output {
        if self.prime != other.prime {
            Err(format!("Cannot multiply two elements in different fields"))
        } else {
            Self::new((self.number * other.number) % self.prime, self.prime)
        }
    }
}

impl Div<FieldElement> for FieldElement {
    type Output = Result<Self, String>;

    fn div(self, other: Self) -> Self::Output {
        if self.prime != other.prime {
            Err(format!("Cannot multiply two elements in different fields"))
        } else {
            /*
             * Use Fermat's Little Theorem:
             *   (nᵖ⁻¹) % p == 1
             * means:
             *   1/n == nᵖ⁻²
             */
            other.pow(self.prime - uint256::one() - uint256::one())
                .map(|el| -> self * el)
        }
    }
}

impl Mul<FieldElement> for i64 {
    type Output = Result<FieldElement, String>;
    fn mul(self, element: FieldElement) -> Self::Output {
        if self >= 0 {
            FieldElement::new(
                (element.number * uint256::from(self)) % element.prime,
                element.prime,
            )
        } else {
            FieldElement::new(
                // -n x FieldElement, is same as:
                //   P -  (n x FieldElement) % P
                //
                // The above value is guaranteed to be positive since:
                //   0 <= (n x FieldElement) % P < P
                element.prime - ((element.number * uint256::from(self.abs())) % element.prime),
                element.prime,
            )
        }
    }
}

#[cfg(test)]
mod test {
    use super::uint256;
    use super::FieldElement;

    #[test]
    fn constructor_when_number_smaller_than_prime_should_work() -> Result<FieldElement, String> {
        FieldElement::new(uint256::from(3), uint256::from(4))
    }

    #[test]
    fn constructor_when_number_bigger_than_prime_should_not_work() -> Result<FieldElement, String> {
        FieldElement::new(uint256::from(7), uint256::from(3))
    }

    #[test]
    fn equality_when_numbers_and_primes_are_equal_should_be_true() {
        let field_a = FieldElement::new(uint256::from(2), uint256::from(31));
        let field_b = FieldElement::new(uint256::from(2), uint256::from(31));

        assert_eq!(field_a, field_b);
    }

    #[test]
    fn equality_when_numbers_and_primes_are_equal_should_be_true() {
        let field_a = FieldElement::new(uint256::from(2), uint256::from(31));
        let field_c = FieldElement::new(uint256::from(15), uint256::from(31));

        assert_ne!(field_a, field_c);
    }

    #[test]
    fn addition_when_fields_have_different_primes_should_not_work() -> Result<FieldElement, Err> {
        let field_a = FieldElement::new(uint256::from(2), uint256::from(31)).unwrap();
        let field_b = FieldElement::new(uint256::from(2), uint256::from(32)).unwrap();
        field_a + field_b
    }

    #[test]
    fn addition_when_fields_have_same_primes_should_add_numbers() {
        let field_a = FieldElement::new(uint256::from(2), uint256::from(31)).unwrap();
        let field_b = FieldElement::new(uint256::from(15), uint256::from(31)).unwrap();
        let field_c = FieldElement::new(uint256::from(13), uint256::from(31)).unwrap();
        let expected = FieldElement::new(uint256::from(17), uint256::from(31));
        assert_eq!(field_a + field_b, expected);
    }

    #[test]
    fn addition_when_fields_have_same_primes_but_result_bigger_than_prime_should_add_numbers_modulo_prime() {
        let field_a = FieldElement::new(uint256::from(17), uint256::from(31)).unwrap();
        let field_b = FieldElement::new(uint256::from(21), uint256::from(31)).unwrap();
        let expected = FieldElement::new(uint256::from(7), uint256::from(31));
        assert_eq!(field_a + field_b, expected);
    }

    #[test]
    fn subtraction_when_fields_have_different_primes_should_not_work() -> Result<FieldElement, String> {
        let field_a = FieldElement::new(uint256::from(2), uint256::from(31)).unwrap();
        let field_b = FieldElement::new(uint256::from(2), uint256::from(32)).unwrap();
        field_a - field_b
    }

    #[test]
    fn subtraction_when_fields_have_same_primes_should_subtract_numbers() {
        let field_a = FieldElement::new(uint256::from(29), uint256::from(31)).unwrap();
        let field_b = FieldElement::new(uint256::from(4), uint256::from(31)).unwrap();
        let expected = FieldElement::new(uint256::from(25), uint256::from(31));
        assert_eq!(field_a - field_b, expected);
    }

    #[test]
    fn subtraction_when_fields_have_same_primes_should_subtract_numbers_modulo_prime() {
        let field_a = FieldElement::new(uint256::from(15), uint256::from(31)).unwrap();
        let field_b = FieldElement::new(uint256::from(30), uint256::from(31)).unwrap();
        let expected = FieldElement::new(uint256::from(16), uint256::from(31));
        assert_eq!((field_a - field_b), expected);
    }

    #[test]
    fn multiplication_when_fields_have_different_primes_should_not_work() -> Result<FieldElement, String> {
        let field_a = FieldElement::new(uint256::from(2), uint256::from(31)).unwrap();
        let field_b = FieldElement::new(uint256::from(2), uint256::from(32)).unwrap();
        field_a * field_b
    }

    #[test]
    fn multiplication_when_fields_have_same_primes_should_multiply_numbers_modulo_prime() {
        let field_a = FieldElement::new(uint256::from(24), uint256::from(31)).unwrap();
        let field_b = FieldElement::new(uint256::from(19), uint256::from(31)).unwrap();
        let expected = FieldElement::new(uint256::from(22), uint256::from(31));
        assert_eq!(field_a * field_b, expected);
    }

    #[test]
    fn exponentiation_when_fields_have_same_primes_should_raise_number_to_exponent_modulo_prime() {
        let field_a = FieldElement::new(uint256::from(17), uint256::from(31)).unwrap();
        let expected = FieldElement::new(uint256::from(15), uint256::from(31));
        assert_eq!(field_a.pow(uint256::from(3)), expected);

        let field_a = FieldElement::new(uint256::from(5), uint256::from(31)).unwrap();
        let expected = FieldElement::new(uint256::from(25), uint256::from(31));
        assert_eq!(field_a.pow(uint256::from(5)), expected);

        let expected = FieldElement::new(uint256::from(29), uint256::from(31));
        assert_eq!(field_a.neg_pow(uint256::from(3)), expected);

        let field_a = FieldElement::new(uint256::from(4), uint256::from(31)).unwrap();
        let expected = FieldElement::new(uint256::from(4), uint256::from(31));
        assert_eq!(field_a.neg_pow(uint256::from(4)), expected);
    }

    #[test]
    fn division_when_fields_have_different_primes_should_not_work() -> Result<FieldElement, String> {
        let field_a = FieldElement::new(uint256::from(2), uint256::from(31)).unwrap();
        let field_b = FieldElement::new(uint256::from(2), uint256::from(32)).unwrap();
        field_a / field_b
    }

    #[test]
    fn division_when_fields_have_same_primes_should_divide_numbers_modulo_prime() {
        let field_a = FieldElement::new(uint256::from(3), uint256::from(31)).unwrap();
        let field_b = FieldElement::new(uint256::from(24), uint256::from(31)).unwrap();
        let expected = FieldElement::new(uint256::from(4), uint256::from(31));
        assert_eq!(field_a / field_b, expected);
    }

    #[test]
    fn scalar_multiplication_with_positive_scalar_should_multiple_number_to_scalar_modulo_prime() {
        let field_a = FieldElement::new(uint256::from(18), uint256::from(31)).unwrap();
        let expected = FieldElement::new(uint256::from(28), uint256::from(31));
        assert_eq!(5 * field_a, expected);
    }

    #[test]
    fn scalar_multiplication_with_negative_scalar_should_multiple_number_to_scalar_modulo_prime() {
        let field_a = FieldElement::new(uint256::from(11), uint256::from(31)).unwrap();
        let expected = FieldElement::new(uint256::from(18), uint256::from(31));
        assert_eq!(-4 * field_a, expected);
    }
}
