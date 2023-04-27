from game_data import data
from art import logo
from random import choice
from time import sleep
from os import system


class App:
    def __init__(self):
        self._item_pair = []
        self._correct = 0
        self._data: list = data  # contains dicts

    def get_item_pair(self) -> list:
        return self._item_pair

    def get_correct(self) -> int:
        return self._correct

    def get_data(self) -> list:
        return self._data

    def set_item_pair(self, item_pair: list) -> None:
        self._item_pair = item_pair

    def set_correct(self, correct: int) -> None:
        self._correct = correct

    def add_item(self, item: dict) -> None:
        if len(self.get_item_pair()) < 2:
            self.get_item_pair().append(item)
        else:
            print("Tried to add too many items to item pair.")

    def read_item(self, item: dict) -> str:
        return f"{item['name']} is a {item['description'].lower()} from {item['country']}."

    def clear_item_pair(self) -> None:
        self.set_item_pair([])

    def pick_item_pair(self) -> None:
        while len(self.get_item_pair()) < 2:
            item = choice(self.get_data())
            if not item in self.get_item_pair():
                self.add_item(item)

    def compare_items(self, item_pair: list) -> dict:
        """Returns the dict with more followers from an item pair."""
        if item_pair[0]['follower_count'] > item_pair[1]['follower_count']:
            return item_pair[0]
        else:
            return item_pair[1]

    def play_round(self, item_pair: list) -> bool:
        flag = True
        a = item_pair[0]
        b = item_pair[1]
        
        print(f"A: {self.read_item(a)}")
        print("\n\nVERSUS\n\n")
        print(f"B: {self.read_item(b)}\n\n\n")
        while flag:
            user_input = input(f"Who has more followers, [A] {a['name']} or [B] {b['name']}?\n\nMake your guess: ").lower()
            print()
            if user_input == 'a' or user_input == 'b':
                larger = self.compare_items(item_pair)['name']
                if user_input == 'a' and larger == a['name'] or user_input == 'b' and larger == b['name']:
                    return True
                else:
                    return False                    
            else:
                print("I'm sorry, I didn't catch that.\n")
        
    def run(self) -> None:
        flag = True
        print(logo)
        print()
        
        while flag:
            if self.get_correct() > 0:
                print(f"Your current score is {self.get_correct()}.\n\n")
            self.pick_item_pair()

            if self.play_round(self.get_item_pair()):
                self.set_correct(self.get_correct() + 1)
                self.clear_item_pair()
                system('clear')
                print(logo)
                print(f"\n\nCorrect!")
            else:
                print(f"Ouch, that was incorrect. Your final score was {self.get_correct()}.")
                user_input = input("Play again? [y/n] ").lower()
                check_input = True
                while check_input:
                    if user_input.startswith('y'):
                        self.set_correct(0)
                        self.clear_item_pair()
                        system('clear')
                        print(logo)
                        print("\nStarting over...\n")
                        check_input = False
                    elif user_input.startswith('n'):
                        print("\nThanks for playing!")
                        check_input = False
                        flag = False
                    else:
                        user_input = input("\nPlease enter either [y/n]: ")