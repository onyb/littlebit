def little_endian_to_int(bytestring: bytes):
    """
    Takes byte sequence as a little-endian number, and returns an integer
    """
    return int.from_bytes(bytestring, "little")


def int_to_little_endian(n, length):
    """
    Takes an integer and returns the little-endian byte sequence of length
    """
    return n.to_bytes(length, "little")
