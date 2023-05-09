# A collection of utility functions related to getting user input

def get_float(message: str = "Enter a float:", error_msg: str = "Please enter a valid number.") -> float:
    """Returns a valid float from user input. Takes an optional message and error message to display to the user.
    Loops until a valid float is entered."""
    flag = True
    while flag:
        try:
            f = float(input(message + " "))
            if f < 0:
                print(error_msg)
                continue
            return f
        except ValueError:
            print(error_msg)
            continue


def get_int(message: str = "Enter an integer:", error_msg: str = "Please enter a valid number.") -> int:
    """Returns a valid int from user input. Takes an optional message and error message to display to the user.
    Loops until a valid int is entered."""
    flag = True
    while flag:
        try:
            i = int(input(message + " "))
            if i < 1:
                print(error_msg)
                continue
            return i
        except ValueError:
            print (error_msg)
            continue


def should_continue(message: str = "Do you want to continue?") -> bool:
    """Tests if the user enters 'yes' or 'no' and returns a bool. Takes an optional input message. Loops until a valid
    input is found."""
    flag = True
    while flag:
        usr_continue = input(message + " [Y/N] ").lower()
        if usr_continue.startswith('y'):
            return True
        elif usr_continue.startswith('n'):
            return False
        else:
            print("I'm sorry, I didn't catch that.")
