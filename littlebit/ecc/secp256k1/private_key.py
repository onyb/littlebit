import hmac
from dataclasses import dataclass, field
from hashlib import sha256

from .constants import Gx, Gy, N
from .point import S256Point
from .signature import Signature

G = S256Point(x=Gx, y=Gy)


@dataclass
class PrivateKey:
    secret: int
    point: int = field(init=False)  # public key

    def __post_init__(self):
        self.point = self.secret * G

    @property
    def hex(self) -> str:
        return f"{self.secret:x}".zfill(64)

    def sign(self, z: int) -> Signature:
        k = self.deterministic_k(z)  # or, randint(0, N)
        R = k * G
        r = R.x.number
        k_inv = pow(k, N - 2, N)
        s = ((z + r * self.secret) * k_inv) % N
        if s > N / 2:
            s = N - s
        return Signature(r, s)

    def deterministic_k(self, z: int) -> int:
        """
        Directly based on RFC 6979:
            Deterministic Usage of the Digital Signature Algorithm (DSA) and
            Elliptic Curve Digital Signature Algorithm (ECDSA)

        All 256 bit integers are encoded in 32 bytes, big-endian.

        [TODO] - Explain me
        """
        k = b"\x00" * 32
        v = b"\x01" * 32
        if z > N:
            z -= N
        z_bytes = z.to_bytes(32, "big")
        secret_bytes = self.secret.to_bytes(32, "big")
        k = hmac.new(k, v + b"\x00" + secret_bytes + z_bytes, sha256).digest()
        v = hmac.new(k, v, sha256).digest()
        k = hmac.new(k, v + b"\x01" + secret_bytes + z_bytes, sha256).digest()
        v = hmac.new(k, v, sha256).digest()
        while True:
            v = hmac.new(k, v, sha256).digest()
            candidate = int.from_bytes(v, "big")
            if 1 <= candidate < N:
                return candidate
            k = hmac.new(k, v + b"\x00", sha256).digest()
            v = hmac.new(k, v, sha256).digest()
