class DiscountCard:
    def __init__(self, name: str, balance: int = 0):
        self.name = name
        self.balance = balance
        self.discount_percent = self.calculate_discount_percent()

    def calculate_discount_percent(self) -> int:
        if self.balance < 1000:
            return 0
        elif 1000 <= self.balance < 2000:
            return 1
        elif 2000 <= self.balance < 5000:
            return 3
        elif 5000 <= self.balance < 10000:
            return 5
        else:
            return 7

    def replenish_balance(self, purchase_amount: float):
        self.balance += purchase_amount
        self.discount_percent = self.calculate_discount_percent()

    def __repr__(self) -> str:
        return f"Card: {self.name}, balance: {self.balance}, discount percent: {self.discount_percent}"
