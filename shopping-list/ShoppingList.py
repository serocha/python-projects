from copy import deepcopy
from ShoppingItem import ShoppingItem
from input_utils import *


class ShoppingList:
    """Handles a list of ShoppingItems. Provides methods to create, find, delete, and print ShoppingItems."""
    def __init__(self, list_name: str = "", items = None, total: float = 0) -> None:
        if items is None:
            items = []
        self._list_name: str = list_name
        self._items: list = items
        self._total: float = total  # consider using ints for dollars and cents

    def get_list_name(self) -> str:
        return self._list_name

    def get_items(self) -> list:
        return deepcopy(self._items)

    def get_total(self) -> float:
        return self._total

    def set_list_name(self, basket_name: str) -> None:
        self._list_name = basket_name

    def set_items(self, basket: list) -> None:
        self._items = basket

    def set_total(self, basket_total: float) -> None:
        self._total = basket_total

    def find_item(self, item_name: str) -> ShoppingItem | None:
        """Searches for an item within the list of ShoppingItems based on name. Returns the object or None."""
        for item in self._items:
            if item.get_name() == item_name:
                return item
        return None

    def add_item(self, item: ShoppingItem) -> None:
        self._items.append(item)

    def rm_item(self, item: ShoppingItem) -> None:
        self._items.remove(item)

    def update_total(self) -> None:
        total = 0
        for item in self.get_items():
            total += item.get_total_cost()
        self.set_total(total)

    def change_name(self) -> bool:
        """Allows the user to change the name of the current list. Returns true if the name was changed."""
        new_name = input("Enter a new name for this shopping list: ")
        invalid_chars = ['.', '']

    def create_an_item(self) -> None:
        """Takes user input to create a new ShoppingItem."""
        item_name = input("Enter a name for the item: ")
        if self.find_item(item_name) is not None:
            print("Item already exists.")
            return
        item_cost = get_float("Enter the cost per item: $")
        item_qty = get_int("Enter how many items to get: ", "Please enter a valid quantity.")
        self.add_item(ShoppingItem(item_name, item_cost, item_qty))
        self.update_total()
        print(f"{item_name} has been added to the list.")

    def delete_an_item(self) -> None:
        """Searches from user-input to delete an existing item."""
        item_name = input("Enter the name of the item you want to delete: ")
        item = self.find_item(item_name)
        if item is not None:
            self.rm_item(item)
            self.update_total()
            print(f"{item_name} has been removed from the list.")
        else:
            print(f"{item_name} does not exist.")

    def print_list(self) -> None:
        print(f"{self.get_list_name()}:")
        for item in self.get_items():
            print(item)
        print("Total: $%.2f" % self.get_total())


