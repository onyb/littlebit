# littlebit

[![Build Status](https://travis-ci.org/onyb/littlebit.svg?branch=master)](https://travis-ci.org/onyb/littlebit)
[![codecov](https://codecov.io/gh/onyb/littlebit/branch/master/graph/badge.svg)](https://codecov.io/gh/onyb/littlebit)


LittleBit is a product of my educational pursuit of learning how [Bitcoin](https://bitcoin.org/bitcoin.pdf) _really_ works at a very fundamental level. The objective of this exercise is to implement Bitcoin primitives with a **clean**, **readable**, and **heavily-commented** code, using nothing but the **Python standard library**.

**This software comes sans warranty. Do NOT use this code for anything other than educational purposes.**


### Progress report of features / concepts

> Legend: :green_apple: Done &nbsp; :lemon: In Progress &nbsp; :tomato: TODO

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
              <li>Addition
              <li>Subtraction</li>
              <li>Multiplication</li>
              <li>Exponentation</li>
              <li>Division</li>
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
            Elliptic curve equation
          </li>
          <li>
            Point addition over Finite Fields
          </li>
          <li>
            Scalar Multiplication over Finite Fields
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
          <li>Point and FieldElement definitions for secp256k1</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><a href="littlebit/ecc/secp256k1.py"><code>Signatures</code></a></td>
      <td align="center">:green_apple:</td>
      <td>
        <ul>
          <li><a href="https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm">ECDSA algorithm</a></li>
          <li>Message signing</li>
          <li>Signature verification</li>
          <li>Security of ECDSA signatures</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>Serialization</b></td>
      <td align="center"></td>
      <td></td>
    </tr>
    <tr>
      <td>SEC Format</td>
      <td align="center">:lemon:</td>
      <td>
      </td>
    </tr>
    <tr>
      <td>DER Signatures</td>
      <td align="center">:tomato:</td>
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
      <td>WIF Format</td>
      <td align="center">:tomato:</td>
      <td>
      </td>
    </tr>
  </tbody>
</table>
