from src.order.discount_card import DiscountCard


class RegisteredDiscountCards:
    def __init__(self):
        self._cards = {}

    def register_card(self, card_name: str, card_balance: int = 0):
        card = DiscountCard(card_name, card_balance)
        self._cards[card_name] = card

    def get_card(self, card_name: str) -> DiscountCard:
        return self._cards.get(card_name)

    def __contains__(self, card_name: str) -> bool:
        return card_name in self._cards
