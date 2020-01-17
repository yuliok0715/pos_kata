import unittest

from src.point_of_sale_terminal import PointOfSaleTerminal
from src.util.set_pricing import set_pricing


class TestCalculating(unittest.TestCase):

    def test_retail_price(self):
        terminal = PointOfSaleTerminal()
        set_pricing(terminal)
        for code in "ABCD":
            terminal.scan(code)
        result = terminal.calculate_total()
        self.assertEqual(result, 7.25)

    def test_volume_price(self):
        terminal = PointOfSaleTerminal()
        set_pricing(terminal)
        for code in "CCCCCC":
            terminal.scan(code)
        result = terminal.calculate_total()
        self.assertEqual(result, 5)

    def test_both_prices(self):
        terminal = PointOfSaleTerminal()
        set_pricing(terminal)
        for code in "CCCCCCC":
            terminal.scan(code)
        result = terminal.calculate_total()
        self.assertEqual(result, 6)

    def test_retail_volume_price_different_products(self):
        terminal = PointOfSaleTerminal()
        set_pricing(terminal)
        for code in "ABCDABA":
            terminal.scan(code)
        result = terminal.calculate_total()
        self.assertEqual(result, 13.25)


if __name__ == '__main__':
    unittest.main()
