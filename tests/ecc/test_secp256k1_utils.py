from littlebit.ecc.secp256k1.utils import encode_base58


def test_base58():
    cases = (
        # hex, base58
        (
            "7c076ff316692a3d7eb3c3bb0f8b1488cf72e1afcd929e29307032997a838a3d",
            "9MA8fRQrT4u8Zj8ZRd6MAiiyaxb2Y1CMpvVkHQu5hVM6",
        ),
        (
            "eff69ef2b1bd93a66ed5219add4fb51e11a840f404876325a1e8ffe0529a2c",
            "4fE3H2E6XMp4SsxtwinF7w9a34ooUrwWe4WsW1458Pd",
        ),
        (
            "c7207fee197d27c618aea621406f6bf5ef6fca38681d82b2f06fddbdce6feab6",
            "EQJsjkd6JaGwxrjEhfeqPenqHwrBmPQZjJGNSCHBkcF7",
        ),
    )

    for hex_string, base58 in cases:
        assert encode_base58(bytes.fromhex(hex_string)) == base58
