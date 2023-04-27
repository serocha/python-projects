# A quick game of hangman!
#
# TODO (one day):
# - add a difficulty option for different wordlists
from random import choice
from hangman_words import word_list
from hangman_art import stages, logo

class Hangman():
  def __init__(self):
    self._word_list = word_list
    self._word = ""
    self._prev_guesses = []  # track all guesses
    self._display = []  # track correct guesses
    self._chances = 6  # how many guesses the user gets

  # getters and setters
  def get_word_list(self):
    return self._word_list

  def get_word(self):
    return self._word

  def get_prev_guesses(self):
    return self._prev_guesses

  def get_display(self):
    return self._display

  def get_chances(self):
    return self._chances

  def set_word_list(self, word_list: list):
    self._word_list = word_list

  def set_word(self, word: str):
    self._word = word

  def set_prev_guesses(self, guess_list: list):
    self._prev_guesses = guess_list

  def set_display(self, display: list):
    self._display = display

  def set_chances(self, chances: int):
    self._chances = chances

  # utility methods
  def load(self):
    word = choice(self.get_word_list())  # pick a word
    display = []
    for letter in word:
      display.append("_")
    self.set_chances(6)  # default chances, consider a CONST or something
    self.set_word(word)
    self.set_display(display)
    self.set_prev_guesses([])

  # checks if the letter is in the chosen word
  def has_letter(self, guess: str):
    word = self.get_word()
    if word.find(guess) == -1:
      return False
    else:
      return True 

  # evaluates the user's guess
  def handle_guess(self, guess: str):    
    flag = True
    prev_guesses = "".join(self.get_prev_guesses())
    while flag:
      if not guess.isalpha():  # validation
        guess = input("Try again: ")
      elif prev_guesses.find(guess) != -1:
        guess = input(f"You already guessed {guess}, try again: ")
      else:
        self.get_prev_guesses().append(guess)
        flag = False
    
    if self.has_letter(guess):
      word = self.get_word()
      display = self.get_display()
      index = 0
      
      for letter in word:
        if guess == letter:
          display[index] = letter
        index += 1
      return True
    return False

  # tests if the game should end
  def check_game_over(self):
    if "".join(self.get_display()) == self.get_word():
      self.game_window()
      print(f"\nHey, you're pretty good at this... it was {self.get_word()}!\n\nYOU WON!")
      return True
    elif self.get_chances() < 1:
      self.game_window()
      print(f"\nOuch, looks like you're out of guesses... The word was {self.get_word()}.\n\nYOU LOST.")
      return True
    else:
      return False

  # gives the user feedback by drawing the hangman and correctly-guessed letters
  def game_window(self):
    prev_guesses = self.get_prev_guesses()
    if len(prev_guesses) > 0:
      print(f"Guesses: {', '.join(prev_guesses)}")
    print("\nWord: " + " ".join(self.get_display()) + "\n")
    print(stages[self.get_chances()])
    
  # game logic
  def run(self):
    menu_flag = True
    print(f"Welcome to\n\n{logo}\n\n")
    
    while menu_flag:  # starts the game anew
      self.load()
      game_flag = True
  
      while game_flag:  # current game loop
        self.game_window()
        guess = input("Guess a letter: ")
        if self.handle_guess(guess):
          print("\nGood guess!\n\n")
        else:
          self.set_chances(self.get_chances() - 1)
          print("\nWrong.\n\n")
        if self.check_game_over():
          game_flag = False

      again_flag = True
      run_again = input("\n\nWant to play again? [y/n] ").lower()
      
      while again_flag:  # check if user wants to play again
        if run_again.startswith('y'):
          again_flag = False
          print("\nGreat! Starting over...\n\n")
        elif run_again.startswith('n'):
          again_flag = False
          menu_flag = False
          
    print("\n\nCatch you next time...")
    
game = Hangman()
game.run()
