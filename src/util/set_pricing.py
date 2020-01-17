from src.point_of_sale_terminal import PointOfSaleTerminal


def set_pricing(terminal: PointOfSaleTerminal):
    terminal.set_retail_price("A", 1.25)
    terminal.set_volume_price("A", 3.0, 3)
    terminal.set_retail_price("B", 4.25)
    terminal.set_retail_price("C", 1.0)
    terminal.set_volume_price("C", 5.0, 6)
    terminal.set_retail_price("D", 0.75)
