# hold a 'secret' auction: swap between bidders, hiding bids
# a short program to practice with dicts
from replit import clear
from art import title, logo


def find_winner(bidders: dict) -> list:
    highest_bid = 0
    highest_bidder = ""
    for bidder in bidders:
        if bidders[bidder] > highest_bid:
            highest_bidder = bidder
            highest_bid = bidders[bidder]
    clear()
    print(title)
    return [highest_bidder, highest_bid]

def create_bidder(bidders: dict) -> None:
    name = input("Enter your name: ")
    flag = True

    print("Enter your bid: ", end="")
    while flag:
        try:
            bid = float(input())
            flag = False
        except TypeError:
            print("Please enter a valid number: ", end="")
        
    print("Your bid has been entered.")
    bidders[name] = bid

def quit() -> bool:
    flag = True
    while flag:
        should_continue = input("Enter a new bidder? [yes/no] ").lower()
        if should_continue.startswith('n') or should_continue.startswith('q'):
            return True
        elif should_continue.startswith('y'):
            clear()
            print(title)
            return False
        else:
            print("I didn't recognize that command.")

def silent_auction() -> None:
    flag = True
    bidders = {}
    
    print(title)
    print(logo)
    while flag:
        create_bidder(bidders)
        if quit():
            flag = False

    winner = find_winner(bidders)
    print(f"{winner[0]} won the auction with a bid of ${winner[1]:.2f}.")


silent_auction()