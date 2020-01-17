from src.order.order import Order
from src.service.available_products import AvailableProducts


class PointOfSaleTerminal:
    def __init__(self):
        self.available_products = AvailableProducts()
        self._current_order = Order()

    def set_retail_price(self, product_code: str, price: float):
        if product_code not in self.available_products:
            self.available_products.add_product(product_code)
        product = self.available_products.get_product(product_code)
        product.set_retail_price(price)

    def set_volume_price(self, product_code: str, price: float, quantity: int):
        if product_code not in self.available_products:
            self.available_products.add_product(product_code)
        product = self.available_products.get_product(product_code)
        product.set_volume_price(price, quantity)

    def scan(self, product_code: str):
        if product_code not in self.available_products:
            raise AttributeError("There aren't such product in our service")
        else:
            product = self.available_products.get_product(product_code)
            self._current_order.add_product(product)

    def calculate_total(self) -> float:
        return self._current_order.get_total_price()

    def create_new_order(self):
        self._current_order = Order()
