class ShoppingItem:
    """Holds information about an item on a ShoppingList."""
    def __init__(self, name: str, cost_per_item: float, quantity: int) -> None:
        self._name = name
        self._cost_per_item = cost_per_item
        self._quantity = quantity

    def set_name(self, name: str) -> None:
        self._name = name

    def set_cost_per_item(self, cost_per_item: float) -> None:
        self._cost_per_item = cost_per_item

    def set_quantity(self, quantity: int) -> None:
        self._quantity = quantity

    def get_name(self) -> str:
        return self._name

    def get_cost_per_item(self) -> float:
        return self._cost_per_item

    def get_quantity(self) -> int:
        return self._quantity

    def get_total_cost(self) -> float:
        return self._cost_per_item * self._quantity

    def __str__(self):
        return "%s, Cost: $%.2f, Qty: %d" % (self.get_name(), self.get_cost_per_item(), self.get_quantity())



