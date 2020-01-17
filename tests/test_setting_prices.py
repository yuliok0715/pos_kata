import unittest

from src.point_of_sale_terminal import PointOfSaleTerminal


class TestSettingPrices(unittest.TestCase):

    def test_set_retail_price(self):
        terminal = PointOfSaleTerminal()
        terminal.set_retail_price("A", 1.0, )
        product = terminal.available_products.get_product("A")

        self.assertEqual(product.retail_price.value, 1.0)

    def test_set_volume_price(self):
        terminal = PointOfSaleTerminal()
        terminal.set_volume_price("A", 1.0, 2)
        product = terminal.available_products.get_product("A")

        self.assertEqual(product.volume_price.value, 1.0)
        self.assertEqual(product.volume_price.quantity, 2)

    def test_set_volume_quantity_one(self):
        terminal = PointOfSaleTerminal()
        terminal.set_volume_price("A", 1.0, 1)
        product = terminal.available_products.get_product("A")

        self.assertEqual(product.volume_price, None)
        self.assertEqual(product.retail_price.value, 1.0)


if __name__ == '__main__':
    unittest.main()
