import random
import string


def get_random_card_name() -> str:
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(10))
