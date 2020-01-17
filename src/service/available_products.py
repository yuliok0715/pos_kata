from src.product.product import Product


class AvailableProducts:
    def __init__(self):
        self._products = {}

    def add_product(self, product_code: str):
        product = Product(product_code)
        self._products[product_code] = product

    def get_product(self, product_code: str) -> Product:
        return self._products.get(product_code)

    def __contains__(self, product_code: str) -> bool:
        return product_code in self._products
