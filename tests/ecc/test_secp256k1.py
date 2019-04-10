from random import randint

from littlebit.ecc.secp256k1 import G, N, PrivateKey, S256Point, Signature


def test_order():
    point = N * G
    assert point.x is None


def test_pubpoint():
    # write a test that tests the public point for the following
    points = (
        # secret, x, y
        (
            7,
            0x5CBDF0646E5DB4EAA398F365F2EA7A0E3D419B7E0330E39CE92BDDEDCAC4F9BC,
            0x6AEBCA40BA255960A3178D6D861A54DBA813D0B813FDE7B5A5082628087264DA,
        ),
        (
            1485,
            0xC982196A7466FBBBB0E27A940B6AF926C1A74D5AD07128C82824A11B5398AFDA,
            0x7A91F9EAE64438AFB9CE6448A1C133DB2D8FB9254E4546B6F001637D50901F55,
        ),
        (
            2 ** 128,
            0x8F68B9D2F63B5F339239C1AD981F162EE88C5678723EA3351B7B444C9EC4C0DA,
            0x662A9F2DBA063986DE1D90C2B6BE215DBBEA2CFE95510BFDF23CBF79501FFF82,
        ),
        (
            2 ** 240 + 2 ** 31,
            0x9577FF57C8234558F293DF502CA4F09CBC65A6572C842B39B366F21717945116,
            0x10B49C67FA9365AD7B90DAB070BE339A1DAF9052373EC30FFAE4F72D5E66D053,
        ),
    )

    # iterate over points
    for secret, x, y in points:
        # initialize the secp256k1 point (S256Point)
        point = S256Point(x, y)
        # check that the secret*G is the same as the point
        assert secret * G == point


def test_verify():
    point = S256Point(
        0x887387E452B8EACC4ACFDE10D9AAF7F6D9A0F975AABB10D006E4DA568744D06C,
        0x61DE6D95231CD89026E286DF3B6AE4A894A3378E393E93A0F45B666329A0AE34,
    )
    z = 0xEC208BAA0FC1C19F708A9CA96FDEFF3AC3F230BB4A7BA4AEDE4942AD003C0F60
    r = 0xAC8D1C87E51D0D441BE8B3DD5B05C8795B48875DFFE00B7FFCFAC23010D3A395
    s = 0x68342CEFF8935EDEDD102DD876FFD6BA72D6A427A3EDB13D26EB0781CB423C4
    assert point.verify(z, Signature(r, s))
    z = 0x7C076FF316692A3D7EB3C3BB0F8B1488CF72E1AFCD929E29307032997A838A3D
    r = 0xEFF69EF2B1BD93A66ED5219ADD4FB51E11A840F404876325A1E8FFE0529A2C
    s = 0xC7207FEE197D27C618AEA621406F6BF5EF6FCA38681D82B2F06FDDBDCE6FEAB6
    assert point.verify(z, Signature(r, s))


def test_sign():
    pk = PrivateKey(randint(0, N))
    z = randint(0, 2 ** 256)
    sig = pk.sign(z)
    assert pk.point.verify(z, sig)


def test_sec():
    inputs = (
        # coefficient, uncompressed sec, compressed sec
        (
            999 ** 3,
            "049d5ca49670cbe4c3bfa84c96a8c87df086c6ea6a24ba6b809c9de234496808d56fa15cc7f3d38cda98dee2419f415b7513dde1301f8643cd9245aea7f3f911f9",
            "039d5ca49670cbe4c3bfa84c96a8c87df086c6ea6a24ba6b809c9de234496808d5",
        ),
        (
            123,
            "04a598a8030da6d86c6bc7f2f5144ea549d28211ea58faa70ebf4c1e665c1fe9b5204b5d6f84822c307e4b4a7140737aec23fc63b65b35f86a10026dbd2d864e6b",
            "03a598a8030da6d86c6bc7f2f5144ea549d28211ea58faa70ebf4c1e665c1fe9b5",
        ),
        (
            42424242,
            "04aee2e7d843f7430097859e2bc603abcc3274ff8169c1a469fee0f20614066f8e21ec53f40efac47ac1c5211b2123527e0e9b57ede790c4da1e72c91fb7da54a3",
            "03aee2e7d843f7430097859e2bc603abcc3274ff8169c1a469fee0f20614066f8e",
        ),
        (
            5001,
            "0457a4f368868a8a6d572991e484e664810ff14c05c0fa023275251151fe0e53d10d6cc87c5bc29b83368e17869e964f2f53d52ea3aa3e5a9efa1fa578123a0c6d",
            "0357a4f368868a8a6d572991e484e664810ff14c05c0fa023275251151fe0e53d1",
        ),
        (
            2019 ** 5,
            "04933ec2d2b111b92737ec12f1c5d20f3233a0ad21cd8b36d0bca7a0cfa5cb870196cbbfdd572f75ace44d0aa59fbab6326cb9f909385dcd066ea27affef5a488c",
            "02933ec2d2b111b92737ec12f1c5d20f3233a0ad21cd8b36d0bca7a0cfa5cb8701",
        ),
        (
            0xDEADBEEF54321,
            "0496be5b1292f6c856b3c5654e886fc13511462059089cdf9c479623bfcbe7769032555d1b027c25c2828ba96a176d78419cd1236f71558f6187aec09611325eb6",
            "0296be5b1292f6c856b3c5654e886fc13511462059089cdf9c479623bfcbe77690",
        ),
    )

    for coefficient, uncompressed, compressed in inputs:
        point = coefficient * G

        # Test serialization to SEC format
        assert point.sec(compressed=False) == bytes.fromhex(uncompressed)
        assert point.sec(compressed=True) == bytes.fromhex(compressed)

        # Test deserialization from SEC format
        assert S256Point.parse(bytes.fromhex(uncompressed)) == point
        assert S256Point.parse(bytes.fromhex(compressed)) == point


def test_der():
    testcases = (
        # r, s
        (1, 2),
        (randint(0, 2 ** 256), randint(0, 2 ** 255)),
        (randint(0, 2 ** 256), randint(0, 2 ** 255)),
        (
            0x37206A0610995C58074999CB9767B87AF4C4978DB68C06E8E6E81D282047A7C6,
            0x8CA63759C1157EBEAEC0D03CECCA119FC9A75BF8E6D0FA65C841C8E2738CDAEC,
        ),
    )
    for r, s in testcases:
        sig = Signature(r, s)
        der = sig.der()
        sig2 = Signature.parse(der)
        assert sig2.r == r
        assert sig2.s == s
