# Checksum Calculator

A simple Python script to calculate the checksum of a file using various hashing algorithms such as SHA-256, MD5, SHA-1, and more.


## Checksum Definition

Checksum is the outcome of running an algorithm, called a cryptographic hash function, on a piece of data, usually a single file.

Comparing the checksum that you generate from your version of the file against the one provided by the source of the file helps ensure that your copy of the file is genuine and error-free.

## Features
- Supports multiple hash algorithms (`md5`, `sha1`, `sha256`, `sha512`, etc.).
- Efficiently processes large files using chunk-based reading.
- Allows users to specify a file and algorithm via command-line arguments.

## Requirements
This script requires Python 3 to run. You can check your Python version with:
```sh
python --version
```

## Installation
Clone this repository or download the script:
```sh
git clone https://github.com/henriquenicolli/checksum-calculator.git
cd checksum-calculator
```

## Usage
### Running the Script
```sh
python checksum_calculator.py <file_path> [algorithm]
```
- `<file_path>`: Path to the file to compute the checksum.
- `[algorithm]` (optional): Hash algorithm (default: `sha256`).

### Examples
Calculate the SHA-256 checksum of a file:
```sh
python checksum_calculator.py example.txt
```

Calculate the MD5 checksum of a file:
```sh
python checksum_calculator.py example.txt md5
```

## Supported Hash Algorithms
The script supports any hash algorithm available in Python's `hashlib` module. Common ones include:
- `md5`
- `sha1`
- `sha256`
- `sha512`

## Author
Henrique Nicolli - [[GitHub](https://github.com/henriquenicolli)]

