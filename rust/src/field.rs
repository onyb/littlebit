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
            Ok(FieldElement {
                number: number,
                prime: prime,
            })
        }
    }
}

#[cfg(test)]
mod test {
    use super::uint256;
    use super::FieldElement;

    #[test]
    fn range() {
        assert!(
            FieldElement::new(uint256::from(3), uint256::from(4)).is_ok(),
            "number range test failed"
        );

        assert!(
            FieldElement::new(uint256::from(7), uint256::from(3)).is_err(),
            "number range test failed"
        );
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
}
