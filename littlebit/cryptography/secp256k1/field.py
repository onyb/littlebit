from ..field import FieldElement
from .constants import P


class S256FieldElement(FieldElement):
    def __init__(self, number, prime=None):
        super().__init__(number=number, prime=P)

    def sqrt(self):
        ###############################################################################
        # Lemma 1: the prime p used in secp256k1 is such that p % 4 == 3              #
        # Lemma 2: nᵖ⁻¹ % p == 1 (Fermat's Little Theorem)                            #
        ###############################################################################

        # Let's denote self as w² for brevity. We want to find w.
        #
        #    w² = w² x 1
        #       = w² x wᵖ⁻¹                                         [... using Lemma 2]
        #       = wᵖ⁺¹
        # => w  = w⁽ᵖ⁺¹⁾ᐟ²
        #       = w²⁽ᵖ⁺¹⁾ᐟ⁴
        #       = (w²)⁽ᵖ⁺¹⁾ᐟ⁴
        #
        # The power (p+1)/4 is an integer, since p % 4 == 3         [... using Lemma 1]
        #
        # Hence, if w² = v and p % 4 == 3, then w = v⁽ᵖ⁺¹⁾ᐟ⁴

        return self ** ((self.prime + 1) // 4)
