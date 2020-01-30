from typing import Optional

from src.order.discount_card import DiscountCard
from src.product.product import Product


class Order:
    def __init__(self):
        self._entities = {}

    def add_product(self, product: Product):
        self._entities[product] = self._entities.get(product, 0) + 1

    def get_total_price(self, discount_card: Optional[DiscountCard]):
        if discount_card:
            discount_percent = discount_card.discount_percent
        else:
            discount_percent = 0
        cost_per_product = {product: self.__calculate_cost(product, quantity, discount_percent) for product, quantity in
                            self._entities.items()}
        return sum(cost_per_product.values())

    def get_price_without_discounts(self):
        cost_per_product = {product: product.calculate_cost_without_pack_discount(quantity=quantity) for
                            product, quantity in
                            self._entities.items()}
        return sum(cost_per_product.values())

    @staticmethod
    def __calculate_cost(product: Product, quantity: int, discount_percent: int) -> float:
        return product.calculate_cost(quantity=quantity) if product.is_pack_discount_can_be_applied(
            quantity=quantity) else (100 - discount_percent) / 100 * product.calculate_cost(quantity=quantity)
