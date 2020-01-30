from src.point_of_sale_terminal import PointOfSaleTerminal
from src.util.set_pricing import set_pricing


def main():
    terminal = PointOfSaleTerminal()
    set_pricing(terminal)
    cases = ["ABCDABA", "CCCCCCC", "ABCD"]
    for case in cases:
        terminal.create_new_order()
        for code in case:
            terminal.scan(code)
        result = terminal.calculate_total()
        print(f"Case: {case}\nResult: {result}\n\n")

    case = "BBBAAA"
    terminal.registered_discount_cards.register_card("special_card", 1500)
    terminal.create_new_order()
    for code in case:
        terminal.scan(code)
    terminal.scan_discount_card("special_card")

    result, card = terminal.finish_order()
    print(f"Case: {case}\nResult: {result}\n{card}\n")


if __name__ == "__main__":
    main()
