from copy import deepcopy
from ShoppingItem import ShoppingItem
from input_utils import *


class ShoppingList:
    """Handles a list of ShoppingItems. Provides methods to create, find, delete, and print ShoppingItems."""
    def __init__(self, list_name: str="", items=None, total: float=0) -> None:
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

    def __str__(self) -> str:
        shopping_list = self.get_list_name()
        for item in self.get_items():
            shopping_list += str(item)
        return shopping_list

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
        """Allows the user to change the name of the current list. Returns True once finished."""
        flag = True
        disallowed = """!()-[]{};:'"\,<>./?@#$%^&*_~"""

        while flag:  # consider not looping and just returning True/False
            is_illegal = False
            new_name = input("Enter a name for this shopping list: ")
            for char in new_name:
                if char in disallowed:
                    is_illegal = True
                    print("No special characters allowed. Try again.")
                    break
            if not is_illegal:
                self.set_list_name(new_name)
                flag = False
        return True

    def stringify_name(self) -> str:
        """Formats the list name as a valid filename."""
        return self.get_list_name().replace(" ", "-")

    def create_an_item(self) -> None:
        """Takes user input to create a new ShoppingItem."""
        print("Creating a new entry...")
        item_name = input("Enter a name for the item: ")
        if self.find_item(item_name) is not None:
            print("Item already exists.")
            return
        item_cost = get_float("Enter the cost per item: $")
        item_qty = get_int("Enter how many items to get: ", "Please enter a valid quantity.")
        self.add_item(ShoppingItem(item_name, item_cost, item_qty))
        self.update_total()
        print(f"{item_name} has been added to {self.get_list_name()}.")

    def edit_an_item(self) -> None:
        """Edits an existing item."""
        print("Editing exiting item...")
        self.print_list()
        item_name = input("Enter the name of the item you want to edit: ")
        item = self.find_item(item_name)
        if item is not None:
            if should_continue(f"Edit the name of {item.get_name()}?"):
                new_name = input("Enter the new name: ")
                item.set_name(new_name)

            print("Current unit cost is $%.2f." % item.get_cost_per_item(), end=" ")
            if should_continue("Edit unit cost?"):
                new_cost = get_float("Enter cost per unit: $")
                item.set_cost_per_item(new_cost)

            print("Quantity is currently %d." % item.get_quantity(), end=" ")
            if should_continue("Edit quantity?"):
                new_qty = get_int("Enter new quantity: ")
                item.set_quantity(new_qty)

            print(f"{item.get_name()} successfully updated.")
        else:
            print(f"{item_name} not found.")

    def delete_an_item(self) -> None:
        """Searches from user-input to delete an existing item."""
        print("Deleting an item...")
        item_name = input("Enter the name of the item you want to delete: ")
        item = self.find_item(item_name)
        if item is not None:
            self.rm_item(item)
            self.update_total()
            print(f"{item_name} has been removed from {self.get_list_name()}.")
        else:
            print(f"{item_name} does not exist.")

    def print_list(self) -> None:
        print(f"\n{self.get_list_name()}\n")
        for item in self.get_items():
            print(item)
        print()
        print("TOTAL: $%.2f" % self.get_total())


