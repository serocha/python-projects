from random import randint
from art import logo
from time import sleep


class App:
    """A class that runs a game of guess the number."""
    def __init__(self):
        self._guesses: int = 10
        self._number: int = 0
        self._prev_guess: int = 0
        self._games_played: int = 0
        self._wins: int = 0
        self._MAX_NUM: int = 100  # default between 1 and 100

    def get_guesses(self) -> int:
        return self._guesses

    def get_number(self) -> int:
        return self._number

    def get_prev_guess(self) -> int:
        return self._prev_guess

    def get_games_played(self) -> int:
        return self._games_played

    def get_wins(self) -> int:
        return self._wins

    def set_guesses(self, guesses: int) -> None:
        self._guesses = guesses

    def set_number(self, number: int) -> None:
        self._number = number

    def set_prev_guess(self, prev_guess: int) -> None:
        self._prev_guess = prev_guess

    def set_games_played(self, games_played: int) -> None:
        self._games_played = games_played

    def set_wins(self, wins: int) -> None:
        self._wins = wins

    def set_game_mode(self) -> None:
        """Determines difficulty."""
        flag = True
        while flag:
            game_mode = input("Choose a difficulty. Enter 'easy' or 'hard': ")
            if game_mode == "easy":
                self.set_guesses(10)
                flag = False
            elif game_mode == "hard":
                self.set_guesses(5)
                flag = False
            else:
                print("I didn't catch that.")
        print("\033c", end='')
        print(f"Game mode set to {'easy' if self.get_guesses() == 10 else 'hard'}.\n")
    
    def gen_number(self) -> None:
        self.set_number(randint(1, self._MAX_NUM))

    def calc_warmth(self, guess: int) -> None:
        """Compares a guess against a previous guess, and prints if the player is getting warmer or colder."""
        distance = abs(guess - self.get_number())
        if distance > abs(self.get_prev_guess() - self.get_number()):
            print("You're getting colder.\n")
        elif distance < abs(self.get_prev_guess() - self.get_number()):
            print("You're getting warmer.\n")

    def eval_guess(self, guess: int) -> bool:
        """Takes a guess and determines if it was correct. Tells the player if it was too high or low."""
        number = self.get_number()

        if guess == number:
            print("You guessed it correctly!\n")
            return True
        
        if guess > number:
            print("Too high.", end=" ")
        elif guess < number:
            print("Too low.", end=" ")
        else:
            print("Still wrong.")

        if self.get_prev_guess() != 0:
            self.calc_warmth(guess)
        else:
            print()

        return False

    def run_game(self) -> None:
        """Plays a round of number guessing."""
        flag = True
        self.gen_number()
        
        print(f"I'm thinking of a number between 1 and {self._MAX_NUM}.\n")
        while flag:
            if self.get_prev_guess() != 0:
                print(f"Your last guess was {self.get_prev_guess()}.", end=" ")
            print(f"You have {self.get_guesses()} guesses remaining.\n\n")
            try:
                guess = int(input("Enter a guess: "))
                print()
                sleep(0.5)
                
                if guess < 1 or guess > self._MAX_NUM:
                    print(f"Please enter a number between 1 and {self._MAX_NUM}.\n")
                elif self.eval_guess(guess):
                    self.set_wins(self.get_wins() + 1)
                    flag = False
                else:
                    self.set_guesses(self.get_guesses() - 1)
                
                sleep(2)
                print("\033c", end='')
                
                
                if self.get_guesses() < 1:
                    print("You're out of guesses. Better luck next time.\n")
                    sleep(2)
                    flag = False

                self.set_prev_guess(guess)
            except TypeError:
                print(f"Please enter a number between 1 and {self._MAX_NUM}.\n")
        self.set_games_played(self.get_games_played() + 1)
        print("\033c", end='')

    def main_menu(self):
        """Starts up the game."""
        flag = True
        while flag:
            print(logo)
            print("Welcome to Guess the Number!\n")
            if self.get_games_played() > 0:
                print(f"Games Played: {self.get_games_played()}\t\tWins: {self.get_wins()}\n")
            user_input = input("Type 'start' to begin or 'quit' to exit: ").lower()

            if user_input.startswith('s'):
                self.set_game_mode()
                self.run_game()
            elif user_input.startswith('q'):
                flag = False
            else:
                print("I'm sorry, I didn't catch that.\n")
        print("Thanks for playing!")