import os
from pathlib import Path
from copy import deepcopy
from ShoppingList import ShoppingList


class ShoppingListApp:
    """Runs the shopping list application. Handles saving, loading, and creating lists."""
    def __init__(self):
        self._DIR: str = os.getcwd() + "\\my-lists\\"
        self._EXT: str = ".list"
        self._my_lists: list = []  # file names for saved baskets
        self._current_list: ShoppingList = ShoppingList()

        if not os.path.exists(self._DIR):
            os.mkdir(self._DIR)

        if not os.listdir(self._DIR) is []:
            for file in os.listdir(self._DIR):
                if Path(file).suffix == self._EXT:
                    self._my_lists.append(file)

    def get_dir(self) -> str:
        return self._DIR

    def get_ext(self) -> str:
        return self._EXT

    def get_my_lists(self) -> list:
        return deepcopy(self._my_lists)

    def set_my_lists(self, my_lists: list) -> None:
        self._my_lists = my_lists

    def set_current_list(self, shopping_list: ShoppingList) -> None:
        self._current_list = shopping_list

    def add_list(self, list_name: str) -> None:
        self._my_lists.append(list_name)

    def rm_list(self, list_name: str) -> None:
        self._my_lists.remove(list_name)

    def create_new_list(self) -> None:
        self._current_list = ShoppingList()



