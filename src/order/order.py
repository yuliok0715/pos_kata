from src.product.product import Product


class Order:
    def __init__(self):
        self._entities = {}

    def add_product(self, product: Product):
        self._entities[product] = self._entities.get(product, 0) + 1

    def get_total_price(self):
        cost_per_product = {product: product.calculate_cost(quantity=quantity) for product, quantity in
                            self._entities.items()}
        return sum(cost_per_product.values())
