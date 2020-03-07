use std::ops::{Add, Div, Mul, Sub};
use uint::construct_uint;

construct_uint! {
    // uint256 with 256 bits consisting of 4 x 64-bit words
    pub struct uint256(4);
}

// ? [FIXME] - Possible to use just Eq?
#[derive(Eq, PartialEq, Debug)]
pub struct FieldElement {
    pub number: uint256,
    pub prime: uint256,
}

impl FieldElement {
    pub fn new(number: uint256, prime: uint256) -> Result<Self, String> {
        if number < uint256::from(0) || number > prime {
            Err(format!(
                "{el} not in field range 0 to {p}.",
                el = number,
                p = prime - 1
            ))
        } else {
            Ok(Self {
                number: number,
                prime: prime,
            })
        }
    }

    // ? [FIXME] - What's the standard way of dealing with negative exponents?
    //             Maybe use something other than uint256?
    pub fn pow(self, exponent: uint256, is_positive: bool) -> Result<Self, String> {
        match is_positive {
            true => Self::new(self.number.pow(exponent) % self.prime, self.prime),
            false => {
                let modulo = self.prime - uint256::one();
                let n = (modulo - exponent) % modulo;
                Self::new(self.number.pow(n) % self.prime, self.prime)
            }
        }
    }
}

impl Add<FieldElement> for FieldElement {
    type Output = Result<Self, String>;

    fn add(self, other: Self) -> Result<Self, String> {
        if self.prime != other.prime {
            Err(format!("Cannot add two elements in different fields"))
        } else {
            Self::new((self.number + other.number) % self.prime, self.prime)
        }
    }
}

impl Sub<FieldElement> for FieldElement {
    type Output = Result<Self, String>;

    fn sub(self, other: Self) -> Result<Self, String> {
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

    fn mul(self, other: Self) -> Result<Self, String> {
        if self.prime != other.prime {
            Err(format!("Cannot multiply two elements in different fields"))
        } else {
            Self::new((self.number * other.number) % self.prime, self.prime)
        }
    }
}

impl Div<FieldElement> for FieldElement {
    type Output = Result<Self, String>;

    fn div(self, other: Self) -> Result<Self, String> {
        if self.prime != other.prime {
            Err(format!("Cannot multiply two elements in different fields"))
        } else {
            /*
             * Use Fermat's Little Theorem:
             *   (nᵖ⁻¹) % p == 1
             * means:
             *   1/n == nᵖ⁻²
             */
            match other.pow(self.prime - uint256::one() - uint256::one(), true) {
                Err(e) => Err(e),
                Ok(el) => self * el,
            }
        }
    }
}

impl Mul<FieldElement> for i64 {
    type Output = Result<FieldElement, String>;
    fn mul(self, element: FieldElement) -> Result<FieldElement, String> {
        match self >= 0 {
            true => FieldElement::new(
                (element.number * uint256::from(self)) % element.prime,
                element.prime,
            ),
            false => FieldElement::new(
                // -n x FieldElement, is same as:
                //   P -  (n x FieldElement) % P
                //
                // The above value is guaranteed to be positive since:
                //   0 <= (n x FieldElement) % P < P
                element.prime - ((element.number * uint256::from(self.abs())) % element.prime),
                element.prime,
            ),
        }
    }
}

#[cfg(test)]
mod test {
    use super::uint256;
    use super::FieldElement;

    #[test]
    fn range() {
        assert!(FieldElement::new(uint256::from(3), uint256::from(4)).is_ok(),);
        assert!(FieldElement::new(uint256::from(7), uint256::from(3)).is_err(),);
    }

    #[test]
    fn equality() {
        // ? [FIXME] - Possible to use keyword arguments?
        let a = FieldElement::new(uint256::from(2), uint256::from(31));
        let b = FieldElement::new(uint256::from(2), uint256::from(31));
        let c = FieldElement::new(uint256::from(15), uint256::from(31));

        assert_eq!(a, b);
        assert_ne!(a, c);
        assert_eq!(a == b, true);
    }

    #[test]
    fn addition() {
        assert!(
            (FieldElement::new(uint256::from(2), uint256::from(31)).unwrap()
                + FieldElement::new(uint256::from(2), uint256::from(32)).unwrap())
            .is_err()
        );

        assert_eq!(
            (FieldElement::new(uint256::from(2), uint256::from(31)).unwrap()
                + FieldElement::new(uint256::from(15), uint256::from(31)).unwrap()),
            FieldElement::new(uint256::from(17), uint256::from(31))
        );

        assert_eq!(
            (FieldElement::new(uint256::from(17), uint256::from(31)).unwrap()
                + FieldElement::new(uint256::from(21), uint256::from(31)).unwrap()),
            FieldElement::new(uint256::from(7), uint256::from(31))
        );
    }

    #[test]
    fn subtraction() {
        assert!(
            (FieldElement::new(uint256::from(2), uint256::from(31)).unwrap()
                - FieldElement::new(uint256::from(2), uint256::from(32)).unwrap())
            .is_err()
        );

        assert_eq!(
            (FieldElement::new(uint256::from(29), uint256::from(31)).unwrap()
                - FieldElement::new(uint256::from(4), uint256::from(31)).unwrap()),
            FieldElement::new(uint256::from(25), uint256::from(31))
        );

        assert_eq!(
            (FieldElement::new(uint256::from(15), uint256::from(31)).unwrap()
                - FieldElement::new(uint256::from(30), uint256::from(31)).unwrap()),
            FieldElement::new(uint256::from(16), uint256::from(31))
        );
    }

    #[test]
    fn multiplication() {
        assert!(
            (FieldElement::new(uint256::from(2), uint256::from(31)).unwrap()
                * FieldElement::new(uint256::from(2), uint256::from(32)).unwrap())
            .is_err()
        );

        assert_eq!(
            (FieldElement::new(uint256::from(24), uint256::from(31)).unwrap()
                * FieldElement::new(uint256::from(19), uint256::from(31)).unwrap()),
            FieldElement::new(uint256::from(22), uint256::from(31))
        );
    }

    #[test]
    fn exponentiation() {
        assert_eq!(
            FieldElement::new(uint256::from(17), uint256::from(31))
                .unwrap()
                .pow(uint256::from(3), true),
            FieldElement::new(uint256::from(15), uint256::from(31))
        );

        assert_eq!(
            FieldElement::new(uint256::from(5), uint256::from(31))
                .unwrap()
                .pow(uint256::from(5), true),
            FieldElement::new(uint256::from(25), uint256::from(31))
        );

        assert_eq!(
            FieldElement::new(uint256::from(17), uint256::from(31))
                .unwrap()
                .pow(uint256::from(3), false),
            FieldElement::new(uint256::from(29), uint256::from(31))
        );

        assert_eq!(
            FieldElement::new(uint256::from(4), uint256::from(31))
                .unwrap()
                .pow(uint256::from(4), false),
            FieldElement::new(uint256::from(4), uint256::from(31))
        );
    }

    #[test]
    fn division() {
        assert!(
            (FieldElement::new(uint256::from(2), uint256::from(31)).unwrap()
                * FieldElement::new(uint256::from(2), uint256::from(32)).unwrap())
            .is_err()
        );

        assert_eq!(
            (FieldElement::new(uint256::from(3), uint256::from(31)).unwrap()
                / FieldElement::new(uint256::from(24), uint256::from(31)).unwrap()),
            FieldElement::new(uint256::from(4), uint256::from(31))
        );
    }

    #[test]
    fn scalar_multiplication() {
        assert_eq!(
            5 * FieldElement::new(uint256::from(18), uint256::from(31)).unwrap(),
            FieldElement::new(uint256::from(28), uint256::from(31))
        );

        assert_eq!(
            -4 * FieldElement::new(uint256::from(11), uint256::from(31)).unwrap(),
            FieldElement::new(uint256::from(18), uint256::from(31))
        );
    }
}
