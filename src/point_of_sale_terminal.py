from typing import Optional

from src.order.discount_card import DiscountCard
from src.order.order import Order
from src.service.available_products import AvailableProducts
from src.service.registered_discount_cards import RegisteredDiscountCards
from src.util.get_random_name import get_random_card_name


class PointOfSaleTerminal:
    def __init__(self):
        self.available_products = AvailableProducts()
        self.registered_discount_cards = RegisteredDiscountCards()
        self._current_order = Order()
        self._discount_card: Optional[DiscountCard]= None

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

    def scan_discount_card(self, card_name: str):
        if card_name not in self.registered_discount_cards:
            raise AttributeError("There aren't such card in our service")
        else:
            card = self.registered_discount_cards.get_card(card_name)
            self._discount_card = card

    def calculate_total(self) -> float:
        return self._current_order.get_total_price(self._discount_card)

    def finish_order(self):
        total_price = self.calculate_total()
        price_without_discounts = self._current_order.get_price_without_discounts()
        if self._discount_card:
            self._discount_card.replenish_balance(price_without_discounts)
            print(f"Now your card balance is {self._discount_card.balance}")
        else:
            card_name = get_random_card_name()
            self.registered_discount_cards.register_card(card_name, price_without_discounts)
            self._discount_card = self.registered_discount_cards.get_card(card_name)
            print(f"Now you get your own discount card: card_name: {card_name}, balance: {price_without_discounts}")
        return total_price, self._discount_card

    def create_new_order(self):
        self._current_order = Order()
