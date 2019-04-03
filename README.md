# littlebit
A simple Bitcoin library from scratch with focus on readability

[![Build Status](https://travis-ci.org/onyb/littlebit.svg?branch=master)](https://travis-ci.org/onyb/littlebit)
[![codecov](https://codecov.io/gh/onyb/littlebit/branch/master/graph/badge.svg)](https://codecov.io/gh/onyb/littlebit)


### Progress report

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
      <td><a href="littlebit/ecc/field_element.py"><code>Finite Fields</code></a></td>
      <td align="center">:green_apple:</td>
      <td>
        <ul>
          <li>
            Finite Field definition
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
          <li>
            Fermat's Little Theorem
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
          <li>secp256k1 equation, and parameters</li>
          <li>Point and FieldElement definitions for secp256k1</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><a href="littlebit/ecc/secp256k1.py"><code>Signatures</code></a></td>
      <td align="center">:green_apple:</td>
      <td>
        <ul>
          <li>ECDSA algorithm</li>
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
