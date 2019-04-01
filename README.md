# littlebit
A simple Bitcoin library from scratch with focus on readability

[![Build Status](https://travis-ci.org/onyb/littlebit.svg?branch=master)](https://travis-ci.org/onyb/littlebit)
[![codecov](https://codecov.io/gh/onyb/littlebit/branch/master/graph/badge.svg)](https://codecov.io/gh/onyb/littlebit)


### Progress report

> Legend: :green_apple: Done &nbsp; :lemon: In Progress &nbsp; :tomato: TODO

| Component                                                    | Status        | Description |
| ------------------------------------------------------------ | :-----------: | :---------: |
| **Elliptic Curve Cryptography (ECC)**                                                      |
| [`Finite Field operations`](littlebit/ecc/field_element.py)  | :green_apple: |             |
| [`Point operations`](littlebit/ecc/point.py)                 | :green_apple: |             |
| secp256k1                                                    | :lemon:       |             |
| Signatures                                                   | :tomato:      |             |
| **Serialization**                                                                          |
| SEC Format                                                   | :tomato:      |             |
| DER Signatures                                               | :tomato:      |             |
| Base58                                                       | :tomato:      |             |
| Big and Little Endian Redux                                  | :tomato:      |             |
| **Transactions**                                                                           |
| Versions                                                     | :tomato:      |             |
| Inputs                                                       | :tomato:      |             |
| Outputs                                                      | :tomato:      |             |
| Locktime                                                     | :tomato:      |             |
| Transaction Fee                                              | :tomato:      |             |
| Transaction Creation                                         | :tomato:      |             |
| Transaction Validation                                       | :tomato:      |             |
| Multisig Transactions (p2sh)                                 | :tomato:      |             |
| **Script**                                                                                 |
| Parsing                                                      | :tomato:      |             |
| p2pk                                                         | :tomato:      |             |
| p2pkh                                                        | :tomato:      |             |
| **Blocks**                                                                                 |
| Coinbase transactions                                        | :tomato:      |             |
| Block headers                                                | :tomato:      |             |
| Proof-of-Work                                                | :tomato:      |             |
| **Network**                                                                                |
| Network Messages                                             | :tomato:      |             |
| Network Handshake                                            | :tomato:      |             |
| Getting Block Headers                                        | :tomato:      |             |
| **Simplified Payment Verification**                                                        |
| Merkle Tree                                                  | :tomato:      |             |
| Merkle Block                                                 | :tomato:      |             |
| **Bloom Filters**                                                                          |
| BIP0037                                                      | :tomato:      |             |
| Getting Merkel Blocks                                        | :tomato:      |             |
| Getting Transactions of Interest                             | :tomato:      |             |
| **Segwit**                                                                                 |
| p2wpkh                                                       | :tomato:      |             |
| p2sh-p2wpkh                                                  | :tomato:      |             |
| p2sh-p2wsh                                                   | :tomato:      |             |
