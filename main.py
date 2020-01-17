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


if __name__ == "__main__":
    main()
