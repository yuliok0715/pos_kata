from src.product.price import RetailPrice, VolumePrice


class Product:
    def __init__(self, product_code: str):
        self.product_code = product_code
        self.retail_price = None
        self.volume_price = None

    def calculate_cost(self, quantity: int) -> float:
        if not self.retail_price:
            raise AttributeError("You haven't set retail price for product yet!")
        else:
            if self.volume_price:
                cost = (quantity // self.volume_price.quantity) * self.volume_price.value + \
                       (quantity % self.volume_price.quantity) * self.retail_price.value
            else:
                cost = quantity * self.retail_price.value
            return cost

    def calculate_cost_without_pack_discount(self, quantity: int) -> float:
        if not self.retail_price:
            raise AttributeError("You haven't set retail price for product yet!")
        else:
            cost = quantity * self.retail_price.value
            return cost

    def set_retail_price(self, new_price: float):
        if new_price < 0:
            raise AttributeError("Price can't be less than zero!")
        else:
            price = RetailPrice(value=new_price)
            self.retail_price = price

    def set_volume_price(self, new_price: float, quantity: int):
        if new_price < 0:
            raise AttributeError("Price can't be less than zero!")
        elif quantity <= 0:
            raise AttributeError("Quantity can't be less or equal zero!")
        elif quantity == 1:
            price = RetailPrice(value=new_price)
            self.retail_price = price
        else:
            price = VolumePrice(value=new_price, quantity=quantity)
            self.volume_price = price

    def is_pack_discount_can_be_applied(self, quantity: int) -> bool:
        return self.volume_price and quantity >= self.volume_price.quantity
