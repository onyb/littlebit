# LittleBit

[![Build Status](https://travis-ci.org/onyb/littlebit.svg?branch=master)](https://travis-ci.org/onyb/littlebit)
[![codecov](https://codecov.io/gh/onyb/littlebit/branch/master/graph/badge.svg)](https://codecov.io/gh/onyb/littlebit)
[![python](https://img.shields.io/badge/Made%20with-Python%203.8-1f425f.svg)](https://www.python.org/)
[![rust](https://img.shields.io/badge/Made%20with-Rust%202018-7C482C.svg)](https://www.rust-lang.org)


LittleBit is an educational library of [Bitcoin](https://bitcoin.org/bitcoin.pdf) primitives, with implementations in Python and Rust.

##### Objectives:
- Help the reader understand how Bitcoin _really_ works at a fundamental level.
- Focus on **readability** in the Python implementation; on **correctness**, and **performance** in the Rust implementation.
- Zero (ish) dependency on third-party packages.

**DISCLAIMER:** This software comes **sans warranty**. Do **NOT** use this code for anything other than educational purposes. I beg you.


### Progress report

> Legend: 🍏 Done &nbsp; 🍋 In Progress &nbsp; 🍅 TODO &nbsp; 🐍 Python &nbsp; 🦀 Rust

> Internal links to code inside the repository are indicated <a href="https://github.com/onyb/littlebit">`like this`</a>. External links look <a href="https://github.com/onyb/littlebit">like this</a>.

<table>
  <tbody>
    <tr>
      <th>Component</th>
      <th align="center">Status</th>
    </tr>
    <tr>
      <td><b>Elliptic Curve Cryptography (ECC)</b></td>
      <td/>
    </tr>
    <tr>
      <td>
        <code>Finite Field</code>
      </td>
      <td align="center">
        🐍 ➞ 🍏
        <br />
        🦀 ➞ 🍋
      </td>
    </tr>
    <tr>
      <td><code>Elliptic Curve</code></td>
      <td align="center">
        🐍 ➞ 🍏
        <br />
        🦀 ➞ 🍅
      </td>
    </tr>
    <tr>
      <td><code>secp256k1</code></td>
      <td align="center">
        🐍 ➞ 🍏
        <br />
        🦀 ➞ 🍅
      </td>
    </tr>
    <tr>
      <td><code>Signatures</code></td>
      <td align="center">
        🐍 ➞ 🍏
        <br />
        🦀 ➞ 🍅
      </td>
    </tr>
    <tr>
      <td><b>Serialization</b></td>
      <td />
    </tr>
    <tr>
      <td><code>SEC Format</code></td>
      <td align="center">
        🐍 ➞ 🍏
        <br />
        🦀 ➞ 🍅
      </td>
    </tr>
    <tr>
      <td><code>DER Format</code></td>
      <td align="center">
        🐍 ➞ 🍏
        <br />
        🦀 ➞ 🍅
      </td>
    </tr>
    <tr>
      <td><code>Base58</code></td>
      <td align="center">
        🐍 ➞ 🍏
        <br />
        🦀 ➞ 🍅
      </td>
    </tr>
    <tr>
      <td><code>Bitcoin Address Format</code></td>
      <td align="center">
        🐍 ➞ 🍏
        <br />
        🦀 ➞ 🍅
      </td>
    </tr>
    <tr>
      <td><code>Wallet Import Format (WIF)</code></td>
      <td align="center">
        🐍 ➞ 🍏
        <br />
        🦀 ➞ 🍅
      </td>
    </tr>
    <tr>
      <td><b>Transactions</b></td>
      <td />
    </tr>
  </tbody>
</table>

<sub><b>Note:</b> This table is not complete.</sub>


### Contributing

This is an educational project. You can help out by:

- 🔬 Auditing the codebase, asking questions, reporting bugs (please [create issues](https://github.com/onyb/littlebit/issues/new)).
- 💯 Improving coverage of unit tests.
- <b>λ</b> &nbsp; Adding (clever) type annotations, especially with the Rust part.
- 💬 Adding code comments and explanations.
