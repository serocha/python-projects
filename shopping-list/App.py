# TODO: delete list from save directory
import os
from pathlib import Path
from copy import deepcopy
from ShoppingList import ShoppingList
from ShoppingItem import ShoppingItem
from input_utils import should_continue


class App:
    """Runs the shopping list application. Handles saving, loading, and creating lists."""
    def __init__(self):
        self._DIR: str = os.getcwd() + "\\my-lists\\"
        self._EXT: str = ".list"
        self._list_files: list = []  # file names for saved baskets
        self._current_list: ShoppingList = ShoppingList()

        if not os.path.exists(self._DIR):
            os.mkdir(self._DIR)

        if not os.listdir(self._DIR) is []:
            for file in os.listdir(self._DIR):
                if Path(file).suffix == self._EXT:
                    self._list_files.append(file)

    def get_dir(self) -> str:
        return self._DIR

    def get_ext(self) -> str:
        return self._EXT

    def get_list_files(self) -> list:
        return deepcopy(self._list_files)

    def get_current_list(self) -> ShoppingList:
        return self._current_list

    def set_list_files(self, list_files: list) -> None:
        self._list_files = list_files

    def set_current_list(self, shopping_list: ShoppingList) -> None:
        self._current_list = shopping_list

    def add_list_file(self, list_name: str) -> None:
        self._list_files.append(list_name)

    def rm_list_file(self, list_name: str) -> None:
        self._list_files.remove(list_name)

    def start_new_list(self) -> None:
        if len(self.get_current_list().get_items()) > 0:
            if should_continue("Save current list?"):
                self.save_current_list()
        new_list = ShoppingList()
        if new_list.change_name():
            print("New list " + new_list.get_list_name() + " created.")
            self.set_current_list(new_list)

    def change_list_name(self) -> None:
        self.get_current_list().change_name()

    def add_item(self) -> None:
        self.get_current_list().create_an_item()

    def edit_item(self) -> None:
        self.get_current_list().edit_an_item()

    def delete_item(self) -> None:
        self.get_current_list().delete_an_item()

    def print_total(self) -> None:
        self.get_current_list().print_list()

    def save_operation(self, filename: str) -> None:
        """Handles the writing of the current list to file."""
        file = open(self.get_dir() + filename, 'w')
        file.write(self.get_current_list().get_list_name() + "\n")
        for item in self.get_current_list().get_items():
            file.writelines(item.get_name() + "\n")
            file.writelines(str(item.get_cost_per_item()) + "\n")
            file.writelines(str(item.get_quantity()) + "\n")
        file.close()

    def save_current_list(self) -> None:
        """Determines filename of the current list and saves."""
        filename = self.get_current_list().stringify_name() + self.get_ext()
        if filename in self.get_list_files():
            if should_continue("Overwrite file?"):
                self.save_operation(filename)
                self.add_list_file(filename)
            else:
                print("Save cancelled.")
        else:
            self.save_operation(filename)
            self.add_list_file(filename)

    def load_operation(self, filename) -> None:
        """Handles the reading of a list from file."""
        if not filename.endswith(".list"):
            filename += ".list"
        try:
            file = open(self.get_dir() + filename, 'r')
        except IOError:
            print("Error opening file.")
            return
        loaded_list = ShoppingList()
        loaded_list.set_list_name(file.readline().strip())

        x = 0
        item_name: str = ""
        cost_per: float = 0
        quantity: int = 0
        for line in file:
            if x == 0:
                item_name = line.strip()
            elif x == 1:
                cost_per = float(line.strip())
            elif x == 2:
                quantity = int(line.strip())
            x += 1
            if x > 2:
                item = ShoppingItem(item_name, cost_per, quantity)
                loaded_list.add_item(item)
                x = 0
        loaded_list.update_total()
        loaded_list.print_list()
        self.set_current_list(loaded_list)
        file.close()

    def load_saved_list(self) -> None:
        """Loads a saved list from user input."""
        print("SAVED LISTS\n")
        for list_file in self.get_list_files():
            print(list_file)
        print()

        filename = input("Which file do you want to open? ")
        if filename in self.get_list_files() or filename + ".list" in self.get_list_files():
            try:
                self.load_operation(filename)
            except IOError:
                print("There was an error loading the file. File may be corrupted.")
        else:
            print("File not found. Please check your spelling.")
            if should_continue("Try again?"):
                self.load_saved_list()

    def pause(self, message: str = "") -> None:
        """Prints a message to the user before 'pausing' continuation. Requires pressing enter to continue."""
        # consider moving to input_utils
        print(message)
        input("Press enter to continue. ")

    def run(self) -> None:
        """Main menu presented to the user."""
        flag = True
        options = """
Options:
1 --> Start New List
2 --> Add Item
3 --> Edit Item
4 --> Delete Item
5 --> Rename List
6 --> Save List
7 --> Open List
8 --> Print Current List
0 --> Exit
"""

        # TODO: consider making options dynamic as opposed to if/else
        print("Welcome to the Shopping List Utility!")
        while flag:
            list_name = self.get_current_list().get_list_name()
            print(f"Current list: {list_name if list_name != '' else 'untitled'}")
            print(options)
            try:
                choice = int(input("> "))
            except ValueError:
                print("Please enter a valid option.")
                continue
            print()

            if choice == 1:
                self.start_new_list()
            elif choice == 2:
                self.add_item()
                self.pause("")
            elif choice == 3:
                if len(self.get_current_list().get_items()) > 0:
                    self.edit_item()
                    self.pause("")
                else:
                    self.pause("Current list is empty.")
            elif choice == 4:
                if len(self.get_current_list().get_items()) > 0:
                    self.delete_item()
                    self.pause("")
                else:
                    self.pause("Current list is empty.")
            elif choice == 5:
                self.change_list_name()
                self.pause("")
            elif choice == 6:
                if self.get_current_list().get_list_name() != "":
                    self.save_current_list()
                    print(f"{self.get_current_list().get_list_name()} has been saved.\n")
                else:
                    self.pause("Please create a list first.")
            elif choice == 7:
                if len(self.get_list_files()) > 0:
                    self.load_saved_list()
                    self.pause(f"{self.get_current_list().get_list_name()} has been loaded.\n")
                else:
                    self.pause("No saved lists.")
            elif choice == 8:
                self.get_current_list().print_list()
                self.pause()
            elif choice == 0:
                if should_continue("Would you like to save your current list before exiting?"):
                    self.save_current_list()
                    print("Closing application...")
                flag = False
                break
            else:
                self.pause("Invalid command.")
            os.system('cls' if os.name == 'nt' else 'clear')
        print("Exited...")




