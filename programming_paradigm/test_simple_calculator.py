import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        # Test basic addition
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-2, -3), -5)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(1000, 2500), 3500)

    def test_subtraction(self):
        """Test the subtraction method."""
        # Test basic subtraction
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(1000, 2500), -1500)

    def test_multiplication(self):
        """Test the multiplication method."""
        # Test basic multiplication
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(1000, 2500), 2500000)

    def test_division(self):
        """Test the division method."""
        # Test basic division
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(6, -3), -2)
        self.assertEqual(self.calc.divide(-6, -3), 2)
        self.assertEqual(self.calc.divide(10, 2), 5)

        # Test division by zero
        self.assertIsNone(self.calc.divide(5, 0))  # Should return None for division by zero
        self.assertIsNone(self.calc.divide(-10, 0))  # Should return None for division by zero

    def test_edge_cases(self):
        """Test edge cases and large numbers."""
        # Large number division
        self.assertEqual(self.calc.divide(1e6, 2), 500000.0)