import unittest
from functools import partial

from src.point_of_sale_terminal import PointOfSaleTerminal


class TestExceprions(unittest.TestCase):

    def test_set_retail_price_for_unavailable_product(self):
        terminal = PointOfSaleTerminal()
        terminal.set_retail_price("A", 1.0)

        self.assertRaises(AttributeError,
                          partial(terminal.scan, "B"))

    def test_set_negative_retail_price(self):
        terminal = PointOfSaleTerminal()
        terminal.set_retail_price("A", 1.0)

        self.assertRaises(AttributeError,
                          partial(terminal.set_retail_price, "A", -1))

    def test_set_negative_volume_price(self):
        terminal = PointOfSaleTerminal()
        terminal.set_retail_price("A", 1.0)

        self.assertRaises(AttributeError,
                          partial(terminal.set_volume_price, "A", -1, 2))

    def test_set_negative_quantity(self):
        terminal = PointOfSaleTerminal()
        terminal.set_retail_price("A", 1.0)

        self.assertRaises(AttributeError,
                          partial(terminal.set_volume_price, "A", 1.0, -2))


if __name__ == '__main__':
    unittest.main()
