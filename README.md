# littlebit

[![Build Status](https://travis-ci.org/onyb/littlebit.svg?branch=master)](https://travis-ci.org/onyb/littlebit)
[![codecov](https://codecov.io/gh/onyb/littlebit/branch/master/graph/badge.svg)](https://codecov.io/gh/onyb/littlebit)


LittleBit is a product of my educational pursuit of learning how [Bitcoin](https://bitcoin.org/bitcoin.pdf) _really_ works at a very fundamental level. The objective of this exercise is to implement Bitcoin primitives with a **clean**, **readable**, and **heavily-commented** code, using nothing but the **Python standard library**.

**This software comes sans warranty. Do NOT use this code for anything other than educational purposes.**


### Progress report of features / concepts

> Legend: :green_apple: Done &nbsp; :lemon: In Progress &nbsp; :tomato: TODO

> Links to code in the repository are indicated [`like this`](). External links look [like this]().

<table>
  <tbody>
    <tr>
      <th>Component</th>
      <th align="center">Status</th>
      <th align="center">Concepts</th>
    </tr>
    <tr>
      <td><b>Elliptic Curve Cryptography (ECC)</b></td>
      <td align="center"></td>
      <td></td>
    </tr>
    <tr>
      <td><a href="littlebit/ecc/field.py"><code>Finite Fields</code></a></td>
      <td align="center">:green_apple:</td>
      <td>
        <ul>
          <li>
            Finite Field definition
          </li>
          <li>
            <a href="https://brilliant.org/wiki/fermats-little-theorem/">Fermat's Little Theorem</a>
          </li>
          <li>
            Finite Field operations
            <ul>
              <li><a href="littlebit/ecc/field.py#L19-L25"><code>Addition</code></li>
              <li><a href="littlebit/ecc/field.py#L27-L33"><code>Subtraction</code></li>
              <li><a href="littlebit/ecc/field.py#L35-L41"><code>Multiplication</code></li>
              <li><a href="littlebit/ecc/field.py#L43-L67"><code>Exponentation</code></li>
              <li><a href="littlebit/ecc/field.py#L69-L82"><code>Division</code></li>
              <li><a href="littlebit/ecc/field.py#L84-L90"><code>Scalar Multiplication</code></li>
            </ul>
          </li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><a href="littlebit/ecc/point.py"><code>Elliptic Curve</code></a></td>
      <td align="center">:green_apple:</td>
      <td>
        <ul>
          <li>
            <a href="littlebit/ecc/point.py#L22"><code>Elliptic curve equation</code></a>
          </li>
          <li>
            <a href="littlebit/ecc/point.py#L34-L104"><code>Point Addition over Finite Fields</code></a>
          </li>
          <li>
            <a href="littlebit/ecc/point.py#L106-L123"><code>Scalar Multiplication over Finite Fields</code></a>
          </li>
          <li>
            Finite cyclic groups
          </li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><a href="littlebit/ecc/secp256k1.py"><code>secp256k1</code></a></td>
      <td align="center">:green_apple:</td>
      <td>
        <ul>
          <li><a href="https://en.bitcoin.it/wiki/Secp256k1">secp256k1 equation, and parameters</a></li>
          <li><a href="littlebit/ecc/secp256k1.py#L19"><code>Point</code></a> and <a href="littlebit/ecc/secp256k1.py#L57"><code>FieldElement</code></a> definitions for secp256k1</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Signatures</td>
      <td align="center">:green_apple:</td>
      <td>
        <ul>
          <li><a href="https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm">ECDSA algorithm</a></li>
          <li><a href="littlebit/ecc/secp256k1.py#L159-L167"><code>Message signing</code></a></li>
          <li><a href="littlebit/ecc/secp256k1.py#L70-L76"><code>Signature verification</code></a></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>Serialization</b></td>
      <td align="center"></td>
      <td></td>
    </tr>
    <tr>
      <td>Standards for Efficient Cryptography (SEC) Format</td>
      <td align="center">:green_apple:</td>
      <td>
        <ul>
          <li><a href="littlebit/ecc/secp256k1.py#L78-L103"><code>Uncompressed and Compressed formats</code></a></li>
          <li><a href="littlebit/ecc/secp256k1.py#L26-L45"><code>Square root of a S256FieldElement</code></a></li>
          <li><a href="littlebit/ecc/secp256k1.py#L105-L134"><code>Deserialization</code></a></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Distinguished Encoding Rules (DER) Signature format</td>
      <td align="center">:lemon:</td>
      <td>
      </td>
    </tr>
    <tr>
      <td>Base58 encoding</td>
      <td align="center">:tomato:</td>
      <td>
      </td>
    </tr>
    <tr>
      <td>Address Format</td>
      <td align="center">:tomato:</td>
      <td>
      </td>
    </tr>
    <tr>
      <td>Wallet Import Format (WIF)</td>
      <td align="center">:tomato:</td>
      <td>
      </td>
    </tr>
  </tbody>
</table>



### Contributing

You can contribute to the project by:
- Reading the codebase, and asking questions (by [creating issues](https://github.com/onyb/littlebit/issues/new)).
- Improving test coverage.
- Adding type annotations.
- Adding code comments and explanations of theoretical concepts.
