"""Test cases for the shopping_cart.py module."""
import sys
import unittest
from io import StringIO
from shopping_cart import CalculateTotal, display_total

class TestShoppingCart(unittest.TestCase):
    """Test cases for the shopping_cart.py module."""
    def test_calculate_total(self):
        """Test that CalculateTotal correctly sums the prices of items in the cart."""
        cart = [
            {'name': 'Item A', 'price': 10.99},
            {'name': 'Item B', 'price': 5.99},
            {'name': 'Item C', 'price': 8.49}
        ]
        expected_total = 10.99 + 5.99 + 8.49
        self.assertAlmostEqual(CalculateTotal(cart), expected_total)

    def test_calculate_total_empty_cart(self):
        """Test that CalculateTotal returns 0 for an empty cart."""
        self.assertEqual(CalculateTotal([]), 0)

    def test_display_total(self):
        """Test that display_total correctly prints the total price."""

        captured_output = StringIO()
        sys.stdout = captured_output
        display_total("25.47")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Total price: 25.47")

    if __name__ == '__main__':
        unittest.main()
