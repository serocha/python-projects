# A short little choose-your-own-adventure game that contains a basic map and inventory system
# TODO: refactor location handling (Location and Exit should handle internally)
# TODO: add final locations
from Location import Location
from world_map import map

class TreasureIsland:

  def __init__(self):
    self._map = map  # from world_map.py
    self._inventory = []
    self._loc = "splash"  # placeholder

  def get_map(self):
    return self._map  # careful since mutable

  def get_inventory(self):
    return self._inventory

  def get_loc(self):
    return self._loc

  def set_loc(self, loc: str):
    self._loc = loc

  def get_from_map(self, loc: str):
    for location in self.get_map():
      if location.get_name() == loc:
        return location
  
  def add_item(self, item: str):
    self._inventory.append(item)

  def check_item(self, item: str):
    for entry in self._inventory:
      if entry == item:
        return True
    return False

  def rm_item(self, item: str):
    if self.check_item(item):
      self._inventory.remove(item)


  def validate_choice(self, choice: str, location: Location):
    for exit in location.get_exits():
      if exit.get_verb() == choice:
        return True
    return False

  def display_loc(self, current_location: Location):
    print(current_location.get_desc())
    if current_location.get_item() != None:
        self.add_item(current_location.take_item())
        print("\n" + current_location.get_item_desc())
    print("\nAvailable exits: ", end="")
    for exit in current_location.get_exits():
      print(f'\"{exit.get_verb()}\", ', end="")
    print('"quit"')

  def goto(self, exits: list, choice: str):
    for exit in exits:
      if exit.get_verb() == choice:
        if exit.get_req_item() != None or exit.get_loc_name() == None:
          if exit.get_req_item() in self.get_inventory():
            loc_name = exit.get_loc_name()
            break
          else:
            print("\n" + exit.get_fail_str())
            return None
        else:
          loc_name = exit.get_loc_name()
          break
          
    print("\n" + exit.get_travel_str() + "\n")
    return loc_name
          
  def run(self):
    flag = True
    while flag:
      current_location = self.get_from_map(self.get_loc())
      print(".........\n")
      self.display_loc(current_location)
      
      choice = input("\n")
      if choice == 'quit':
        break
      elif not self.validate_choice(choice, current_location):
        print("Not a valid option.\n")
      else:
        new_location = self.goto(current_location.get_exits(), choice)
        if new_location == 'quit':
          print("Exiting to the menu...")
          flag = False
        elif new_location != None:
          self.set_loc(new_location)
        else:
          print("\nGame Over\n.........\n")
          flag = False

  def start_menu(self):  # TODO: move the art into another file
    print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

    #Write your code below this line 👇
    flag = True
    while flag:
      choice = input('Welcome to Treasure Island!\n\nYour mission is to find the treasure. Type "start" to begin the hunt or "quit" to exit.\n\n')
      if choice == "start":
        self.set_loc('crossroads')
        self.run()
      elif choice == "quit" or choice == "exit":
        flag = False
      else:
        print("I didn't catch that.")  
        
    print("Thanks for playing!")

game = TreasureIsland()
game.start_menu()