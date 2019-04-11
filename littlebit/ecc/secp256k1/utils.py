import hashlib

BASE58_CHARSET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"


def hash160(s):
    """
    sha256 followed by ripemd160
    """
    return hashlib.new("ripemd160", hashlib.sha256(s).digest()).digest()


def hash256(s):
    """
    Two rounds of sha256
    """
    return hashlib.sha256(hashlib.sha256(s).digest()).digest()


def encode_base58(bytestring: bytes) -> str:
    # Count the number of leading zeros in the bytestring
    leading_zeros = 0
    for byte in bytestring:
        if byte == 0x00:  # fancy way of saying zero
            leading_zeros += 1
        else:
            break

    num = int.from_bytes(bytestring, "big")

    # Putting zeros at the start of a number does not increase its size.
    # Ex: 0x12 is the same as 0x0012. Therefore, any zeros at the start of a number
    # would be "lost" in a conversion to base58. To ensure that leading zeros appear
    # in the result, the bitcoin base58 encoding includes an additional step to convert
    # all leading 0x00's to 1's
    prefix = "1" * leading_zeros

    result = ""
    while num > 0:
        num, mod = divmod(num, 58)
        result = BASE58_CHARSET[mod] + result

    return prefix + result


def checksum(bytestring: bytes):
    """
    A Checksum is the first 4 bytes of the hash256 of a bytestring
    """
    return hash256(bytestring)[:4]


def encode_base58_checksum(bytestring: bytes) -> str:
    """
    Base58 Checksum is the combination of a bytestring with its checksum
    encoded into base58.
    """
    return encode_base58(bytestring + checksum(bytestring))
