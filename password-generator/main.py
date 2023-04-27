#Password Generator Project
from random import choice, shuffle
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#My approach is to put all of the chars into one array, then mix
#I originally coded using random indicies, but realized choice and shuffle exist
def get_list(base_list: list, num_chars: int):
  list = []
  for x in range(num_chars):
    list.append(choice(base_list))
  return list

def create_password():
  pw = get_list(letters, nr_letters) + get_list(numbers, nr_numbers) + get_list(symbols, nr_symbols)
  shuffle(pw)  # consider making a shuffle function to return list
  return "".join(pw)

print(create_password())
  