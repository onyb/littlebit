from dataclasses import dataclass


@dataclass
class Signature:
    r: int
    s: int

    def __repr__(self):
        return f"Signature(r={self.r:x}, s={self.s:x})"

    def der(self) -> bytes:
        # 1. Start with the 0x30 byte.
        # 2. Append the length of the rest of the signature.
        # 3. Append the marker byte, 0x02.
        # 4. Encode r as a big-endian integer, but prepend it with the 0x00 byte if r's
        #    first byte >= 0x80. Prepend the resulting length to r. Add this to the
        #    result.
        # 5. Append the marker byte, 0x02.
        # 6. Encode s as a big-endian integer, but prepend it with the 0x00 byte if s's
        #    first byte >= 0x80. Prepend the resulting length to s. Add this to the
        #    result.

        PREFIX = 0x30
        MARKER = 0x02
        NULL_BYTE = b"\x00"

        # Serialze 256-bit integer to bytes with big-endian byteorder, and strip leading
        # null bytes
        rbin = self.r.to_bytes(32, byteorder="big").lstrip(NULL_BYTE)

        # We check if rbin is negative, by verifying if the first bit of rbin is 1.
        # This is brought about by doing a bitwise AND between the first bit of rbin
        # and (10000000)₂ or (0x80)₁₆.
        if rbin[0] & 0x80:
            rbin = NULL_BYTE + rbin

        result = bytes([MARKER, len(rbin)]) + rbin

        # Serialze 256-bit integer to bytes with big-endian byteorder, and strip leading
        # null bytes
        sbin = self.s.to_bytes(32, byteorder="big").lstrip(NULL_BYTE)

        # We check if sbin is negative, by verifying if the first bit of sbin is 1.
        # This is brought about by doing a bitwise AND between the first bit of sbin
        # and (10000000)₂ or (0x80)₁₆.
        if sbin[0] & 0x80:
            sbin = NULL_BYTE + sbin
        result += bytes([MARKER, len(sbin)]) + sbin

        return bytes([PREFIX, len(result)]) + result

    @classmethod
    def parse(cls, signature_bin: bytes) -> "Signature":
        sig = signature_bin  # store a copy of the binary data

        prefix = sig[0]
        if prefix != 0x30:
            raise ValueError("Invalid Signature prefix")
        sig = sig[1:]  # remove the prifix byte

        length = sig[0]
        if len(signature_bin) != length + 2:
            raise ValueError("Bad Signature length")
        sig = sig[1:]  # remove the signature length byte

        marker = sig[0]
        if marker != 0x02:
            raise ValueError("Bad Signature")
        sig = sig[1:]  # remove the marker byte

        rlen = sig[0]
        sig = sig[1:]  # remove the rlen byte

        r = int.from_bytes(sig[:rlen], byteorder="big")
        sig = sig[rlen:]  # remove r

        marker = sig[0]
        if marker != 0x02:
            raise ValueError("Bad Signature")
        sig = sig[1:]  # remove the marker byte

        slen = sig[0]
        sig = sig[1:]  # remove the slen byte

        s = int.from_bytes(sig[:slen], byteorder="big")
        sig = sig[slen:]  # remove s

        if sig:
            raise ValueError("Signature too long")

        return cls(r, s)
