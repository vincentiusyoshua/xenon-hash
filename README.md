# Xenon-Hash
Xenon Hash is a high-security, efficient hashing algorithm designed for robust data integrity.

## Features

1. Unpredictable Bit Mixing: Uses bit rotation and XOR with the PHI constant to create secure, non-reversible hashes.
2. Multi-layered Data Processing: Compresses 512-bit blocks in parallel, making it efficient for large datasets.
3. Consistent 512-bit Output: Ideal for applications needing strong collision resistance.
4. Optimized Finalization: Multi-round finalization ensures consistent and secure output.
5. Efficient Padding System: Includes message length for added security.

Potential Usage: Secure file verification, digital signatures, and data integrity checks.

## Installation

You can install the package via pip:

```bash
pip install git+https://github.com/vincentiusyoshua/xenon-hash.git
```

## Quick Start

Here’s a quick example to get you started:

```python
from xenon_hash import xenon_hash

# Contoh penggunaan
message = "Hello, World!"
hash_value = xenon_hash(message)
print(f"Input: {message}")
print(f"Hash: {hash_value}")

# Contoh lain
texts = [
    "Python is awesome of course man",
    "Testing Xenon Hash",
    "1234567890",
    "Special chars: !@#$%^&*()"
]

for text in texts:
    hash_result = xenon_hash(text)
    print(f"\nInput: {text}")
    print(f"Hash: {hash_result}")
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

