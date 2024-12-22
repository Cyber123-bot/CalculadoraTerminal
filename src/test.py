# Import the necessary modules
import unittest
from io import StringIO
import sys

# Import the Calculator class
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        # Create a Calculator instance before each test
        self.calc = Calculator(text="Result: ")

    def test_factorization(self):
        # Test for a number with prime factorization
        captured_output = StringIO()
        sys.stdout = captured_output
        self.calc.factorization(30)
        sys.stdout = sys.__stdout__
        self.assertIn("2 x 3 x 5", captured_output.getvalue())

    def test_percentage(self):
        # Test for percentage calculation
        captured_output = StringIO()
        sys.stdout = captured_output
        self.calc.percentage(25, 200)
        sys.stdout = sys.__stdout__
        self.assertIn("12.5", captured_output.getvalue())

    def test_add(self):
        # Test addition with multiple numbers
        captured_output = StringIO()
        sys.stdout = captured_output
        self.calc.add([1, 2, 3, 4])
        sys.stdout = sys.__stdout__
        self.assertIn("10", captured_output.getvalue())

    def test_subtract(self):
        # Test subtraction with multiple numbers
        captured_output = StringIO()
        sys.stdout = captured_output
        self.calc.subtract([10, 5, 2])
        sys.stdout = sys.__stdout__
        self.assertIn("3", captured_output.getvalue())

    def test_multiply(self):
        # Test multiplication with multiple numbers
        captured_output = StringIO()
        sys.stdout = captured_output
        self.calc.multiply([2, 3, 4])
        sys.stdout = sys.__stdout__
        self.assertIn("24", captured_output.getvalue())

    def test_divide(self):
        # Test division with two numbers
        captured_output = StringIO()
        sys.stdout = captured_output
        self.calc.divide([10, 2])
        sys.stdout = sys.__stdout__
        self.assertIn("5.0", captured_output.getvalue())

    def test_square_root(self):
        # Test square root calculation
        captured_output = StringIO()
        sys.stdout = captured_output
        self.calc.square_root(16)
        sys.stdout = sys.__stdout__
        self.assertIn("4.0", captured_output.getvalue())

    def test_cube_root(self):
        # Test cube root calculation
        captured_output = StringIO()
        sys.stdout = captured_output
        self.calc.cube_root(27)
        sys.stdout = sys.__stdout__
        self.assertIn("3.0", captured_output.getvalue())

    def test_power(self):
        # Test power calculation
        captured_output = StringIO()
        sys.stdout = captured_output
        self.calc.power(2, 3)
        sys.stdout = sys.__stdout__
        self.assertIn("8", captured_output.getvalue())

    def test_lcm(self):
        # Test LCM calculation
        captured_output = StringIO()
        sys.stdout = captured_output
        self.calc.lcm(6, 8)
        sys.stdout = sys.__stdout__
        self.assertIn("24", captured_output.getvalue())

    def test_gcd(self):
        # Test GCD calculation
        captured_output = StringIO()
        sys.stdout = captured_output
        self.calc.gcd(36, 60)
        sys.stdout = sys.__stdout__
        self.assertIn("12", captured_output.getvalue())

    def test_rest_of_division(self):
        # Test rest of division
        captured_output = StringIO()
        sys.stdout = captured_output
        self.calc.rest_of_division(10, 3)
        sys.stdout = sys.__stdout__
        self.assertIn("1", captured_output.getvalue())

    def test_invalid_input(self):
        # Test invalid input for functions
        captured_output = StringIO()
        sys.stdout = captured_output
        self.calc.add([1, "a", 3])  # Will raise a ValueError
        sys.stdout = sys.__stdout__
        self.assertIn("Invalid input", captured_output.getvalue())

# Run the tests
if __name__ == '__main__':
    unittest.main()
