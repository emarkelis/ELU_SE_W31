import unittest
from shopping_cart import CalculateTotal, display_total

class TestShoppingCart(unittest.TestCase):
    def test_calculate_total(self):
        cart = [
            {'name': 'Item A', 'price': 10.99},
            {'name': 'Item B', 'price': 5.99},
            {'name': 'Item C', 'price': 8.49}
        ]
        expected_total = 10.99 + 5.99 + 8.49
        self.assertAlmostEqual(CalculateTotal(cart), expected_total)

    def test_calculate_total_empty_cart(self):
        self.assertEqual(CalculateTotal([]), 0)
    
    
    def test_display_total(self):
        # This is a bit tricky since display_total prints to stdout.
        # You can use unittest.mock to capture the output.
        from io import StringIO
        import sys

        captured_output = StringIO()
        sys.stdout = captured_output
        display_total("25.47")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Total price: 25.47")

    if __name__ == '__main__':
        unittest.main()