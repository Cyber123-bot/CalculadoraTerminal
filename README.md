# Calculator Project

This project is a simple Python calculator that performs various mathematical operations such as addition, subtraction, multiplication, division, square root, power, LCM, GCD, percentage, cube root, prime factorization and rest of the division.

## Features
- **Addition**: Adds two numbers.
- **Subtraction**: Subtracts one number from another.
- **Multiplication**: Multiplies two numbers.
- **Division**: Divides one number by another (with error handling for division by zero).
- **Rest of the Division**: Computes the remainder of the division (modulus operation).
- **Square Root**: Calculates the square root of a number.
- **Cube Root**: Calculates the cube root of a number.
- **Power**: Calculates the power of a number (x^y).
- **LCM (Least Common Multiple)**: Finds the least common multiple of two numbers.
- **GCD (Greatest Common Divisor)**: Finds the greatest common divisor of two numbers.
- **Percentage**: Calculates the percentage of a number relative to another.
- **Prime Factorization**: Decomposes a number into its prime factors.

## Usage

1. Clone the repository:
   ```bash
   https://github.com/Cyber123-bot/TerminalCalculator.git
   ```

2. Run the program:
   ```bash
   python calculator.py
   ```

## Requirements
- Python 3.x
- os library (usually pre-installed with Python)
- unittest (for running unit tests)
- io (for handling string input/output, including StringIO)
- sys (for interacting with the system and handling standard input/output)
- style module (must be in the same directory as `calculator.py`)

## Code Structure

- `Calculator`: Main class that handles the calculator's functionality.
  - `__init__`: Initializes the calculator with optional text and question prompts.
  - `factorization`: Calculates and prints the prime factorization of a number.
  - `percentage`: Calculates and prints the percentage of one number relative to another.
  - `add`: Adds a list of numbers and prints the result.
  - `subtract`: Subtracts a list of numbers sequentially and prints the result.
  - `divide`: Divides the first number by subsequent numbers and prints the result.
  - `multiply`: Multiplies a list of numbers and prints the result.
  - `square_root`: Calculates and prints the square root of a number using Newton's method.
  - `cube_root`: Calculates and prints the cube root of a number.
  - `power`: Raises a base to an exponent and prints the result.
  - `lcm`: Calculates and prints the least common multiple of two numbers.
  - `gcd`: Calculates and prints the greatest common divisor of two numbers using the Euclidean algorithm.
  - `rest_of_division`: Calculates and prints the remainder of the division of two numbers.
  - `start_program`: Starts the calculator program, displays a menu of operations, and prompts the user for input.
