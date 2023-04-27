from random import shuffle  # could use choice instead but I find it fun to simulate
from time import sleep
from Card import Card
from art import logo, card_face, card_back, suits

class Blackjack:
    """A class that instantiates a self-contained game of blackjack."""
    # TODO: timer flow could use adjustment for better feel
    # POSSIBLE: add splitting and insurance
    def __init__(self):
        self._deck = []  # holds Card objects
        self._discard_pile = []
        self._num_decks = 2
        self._table_limit = 10  # minimum bet, maximum is calculated at 10x
        self._bet = 10
        self._is_doubled_down = False
        self._percentage_dealt = 0.4  # a ratio multiplied against the number of cards in the deck
        self._chips = 250
        self._TIMER = 0.65  # delay between actions

    def set_deck(self, deck: list) -> None:
        self._deck = deck

    def set_discard_pile(self, pile: list) -> None:
        self._discard_pile = pile

    def set_num_decks(self, num_decks: int) -> None:
        self._num_decks = num_decks

    def set_table_limit(self, table_limit: int) -> None:
        self._table_limit = table_limit

    def set_bet(self, bet: int) -> None:
        self._bet = bet

    def set_is_doubled_down(self, is_doubled_down: bool) -> None:
        self._is_doubled_down = is_doubled_down

    def set_percentage_dealt(self, percent: float) -> None:  
        self._percentage_dealt = percent  

    def set_chips(self, chips: int) -> None:
        self._chips = chips

    def get_deck(self) -> list:
        return self._deck.copy()

    def get_discard_pile(self) -> list:
        return self._discard_pile.copy()

    def get_num_decks(self) -> int:
        return self._num_decks

    def get_table_limit(self) -> int:
        return self._table_limit

    def get_bet(self) -> int:
        return self._bet

    def is_doubled_down(self) -> bool:
        return self._is_doubled_down

    def get_percentage_dealt(self) -> float:
        return self._percentage_dealt

    def get_chips(self) -> int:
        return self._chips

    def generate_card(self, value: int, suit: str, face_type: str=None) -> Card:
        """Creates a Card object, face_type refers to Ace, King, Queen, or Jack."""
        if face_type != None:
            return Card(value, suit, True, face_type)
        return Card(value, suit)

    def generate_deck(self) -> None:
        num_decks = self.get_num_decks()
        suits = ["hearts", "diamonds", "spades", "clubs"]
        face_cards = ['A', 'K', 'Q', 'J']
        deck = []
        
        for x in range(num_decks):
            for suit in suits:  
                for y in range(2, 10):  # regular cards
                    deck.append(self.generate_card(y, suit))
    
                for card in face_cards:  # face cards
                    if card == 'A':
                        deck.append(self.generate_card(11, suit, card))
                    else:
                        deck.append(self.generate_card(10, suit, card))
        self.set_deck(deck)
    
    def draw_card(self) -> Card:
        '''Returns a card. Permanently removes it from the deck.'''
        deck = self.get_deck()
        card = deck.pop()
        self.set_deck(deck)
        return card

    def discard(self, player_hand: list, dealer_hand: list) -> None:
        '''Moves hands to the discard pile.'''
        discard_pile = self.get_discard_pile()
        discard_pile += player_hand + dealer_hand
        self.set_discard_pile(discard_pile)

    def deal_card(self, hand: list) -> None:
        '''Deals a card to the hand passed as an argument.'''
        card = self.draw_card()
        hand.append(card)

    def shuffle_deck(self) -> None:
        '''Empties the discard pile back into the deck and shuffles the order.'''
        deck = self.get_deck() + self.get_discard_pile()
        shuffle(deck)
        self.set_deck(deck)
        self.set_discard_pile([])

    def get_hand_total(self, hand: list) -> int:
        total = 0
        
        for card in hand:
            total += card.get_val()

        if total > 21:  # handle ace behavior
            num_aces = 0
            
            for card in hand:
                if card.get_face_type() == 'A':
                    num_aces += 1
            for x in range(num_aces):
                total -= 10
                if total < 21:
                    break
        
        return total

    def merge_card_art(self, prev_str: str, next_str: str) -> str:
        """Handles merging of card strings for print_hand() method."""
        return "\n".join([" ".join(elem) for elem in zip(prev_str.split("\n"), next_str.split("\n"))])
    
    def print_hand(self, hand: list) -> None:
        total = self.get_hand_total(hand)
        tmp = []  # used for storing each card's art before stitching them together
        
        for card in hand:
            r = card.get_face_type() if card.is_face_card() else card.get_val()  # TODO: face card support
            s = suits[card.get_suit()]
            tmp.append(card_face.format(rank=r, suit=s))
            
        full_hand = tmp[0]
        for x in range(1, len(tmp)):
            full_hand = self.merge_card_art(full_hand, tmp[x])

        sleep(self._TIMER)
        print(full_hand)
        sleep(self._TIMER)
        print(f"TOTAL: {total}\n\n")

    def print_first_hand(self, dealer: list, player: list) -> None:
        print("Dealer's cards:")  # only show the second card
        sleep(self._TIMER)
        
        if dealer[1].is_face_card():
            tmp = card_face.format(rank=dealer[1].get_face_type(), suit=suits[dealer[1].get_suit()])
        else:
            tmp = card_face.format(rank=dealer[1].get_val(), suit=suits[dealer[1].get_suit()])
        print(self.merge_card_art(card_back, tmp))
        sleep(self._TIMER)
        
        print(f"TOTAL: {dealer[1].get_val()}\n\n")
        sleep(self._TIMER)
        
        print("Your cards:")
        self.print_hand(player)
        sleep(self._TIMER)

    def player_decide(self, hand: list) -> bool:
        """Allows the player to hit, double down, or stand. Returns True if the player busts."""
        flag = True
        has_hit = False
        
        while flag:
            print("Choose:\n")
            print("[h] HIT, " + ("[d] DOUBLE DOWN, " if not has_hit else " ") + "[s] STAND \n")
            
            user_input = input("--> ").lower()
            print()
            
            if user_input.startswith('h') or user_input.startswith('d'):
                if not has_hit:
                    has_hit = True
                if user_input.startswith('d'):
                    print(f"Double down. You add ${self.get_bet()} to your bet.\n")
                    self.set_is_doubled_down(True)
                    self.deal_card(hand)
                    
                    print("Your cards:")
                    self.print_hand(hand)
                    return self.is_bust(hand) 
                else:
                    print("Player hits.\n")
                self.deal_card(hand)
                
                print("Your cards:")
                self.print_hand(hand)
                if self.is_bust(hand):
                    return True
                    
            elif user_input.startswith('s'):
                print("Player stands.")
                return False
            else:
                print("Invalid option.")
            
    def dealer_decide(self, hand: list) -> bool:
        """Returns True if the dealer busts."""
        flag = True
        print("\n-------------------------\n\nDealer's turn.\n")
        self.print_hand(hand)
        while flag:
            total = self.get_hand_total(hand)
            
            if total < 17:  # TODO: aces
                self.deal_card(hand)
                print("Dealer hits.")
                self.print_hand(hand)
                if self.is_bust(hand):
                    return True
            elif total > 16:               
                print("Dealer stands.\n")
                return False
                
    def is_bust(self, hand: list) -> bool:
        return self.get_hand_total(hand) > 21

    def is_blackjack(self, hand: list) -> bool: 
        return self.get_hand_total(hand) == 21   

    def play_round(self) -> None:  # TODO: take a look at cleaning up the code
        """Plays one complete round of blackjack."""
        win = 0
        timer = self._TIMER
        player = []  # hands
        dealer = []
        
        sleep(timer)
        print(f"Buy in for ${self.get_bet()} in chips.\n")
        sleep(timer)
        
        for x in range(2):
            self.deal_card(player)
            self.deal_card(dealer)       

        self.print_first_hand(dealer, player)
        
        # test early end conditions            
        if self.is_blackjack(player) or self.is_blackjack(dealer):
            sleep(timer)
            self.print_hand(dealer)
            self.print_hand(player)
            
            if self.is_blackjack(player) and self.is_blackjack(dealer):
                win = self.get_bet()
                sleep(timer)
                print("Push!")
            elif self.is_blackjack(player):
                win = int(self.get_bet() * 1.5)
                sleep(timer)
                print("Player has Blackjack!\n") 
            else:
                win = -self.get_bet()
                sleep(timer)
                print("Dealer has Blackjack!\n")
            
        elif self.player_decide(player):
            win = -(2 * self.get_bet() if self.is_doubled_down() else self.get_bet())
            sleep(timer)
            print("Player busts!\n")

        elif self.dealer_decide(dealer):
            win = (2 * self.get_bet() if self.is_doubled_down() else self.get_bet())
            sleep(timer)
            print("Dealer busts!\n")

        else:  # determine winner
            sleep(timer)
            print("-------------------------\n")

            sleep(timer)
            print(f"DEALER'S TOTAL: {self.get_hand_total(dealer)}")
            sleep(timer)
            print()
            sleep(timer)
            print(f"YOUR TOTAL: {self.get_hand_total(player)}\n\n")
            sleep(timer)
            print()
            sleep(timer)
            if self.get_hand_total(player) == self.get_hand_total(dealer):
                print("Push!\n")
            elif self.get_hand_total(player) > self.get_hand_total(dealer):
                win = (2 * self.get_bet() if self.is_doubled_down() else self.get_bet())
                print("Player wins!\n")
            else:
                win = -(2 * self.get_bet() if self.is_doubled_down() else self.get_bet())
                print("Dealer wins!\n")

        # perform cleanup
        sleep(timer)
        if self.is_doubled_down:
            self.set_is_doubled_down(False)

        if win > 0:
            print(f"Paid out ${win} in chips!\n")
        elif win == 0:
            print("Your chips are returned to you.\n")
        self.set_chips(self.get_chips() + win)
        
        self.discard(player, dealer)
        discard = self.get_discard_pile()  # determine if a shuffle is needed
        original = self.get_deck() + discard
        
        if len(discard) > self.get_percentage_dealt() * len(original):
            self.shuffle_deck()
            print("Dealer shuffles the deck.\n")
            sleep(timer)  # give the player time to see the notification
        sleep(timer * 2)

    def custom_bet(self) -> None:
        flag = True
        while flag:
            limit = self.get_table_limit()
            print(f"TABLE MIN: ${limit}    TABLE MAX: ${limit * 10}\n\n")
            print("How much would you like to bet?\n")
            user_input = input("--> ")
            print()
            try:
                bet = int(user_input)
                if bet < limit:
                    print("I'm sorry, that's below the table limit.\n")
                elif bet > limit * 10:
                    print("That's above the table limit. May I suggest a higher-stakes table?\n")
                else:
                    self.set_bet(bet)
                    print(f"Bet set to ${bet}.\n")
                    flag = False
            except ValueError:
                print("My apologies. Did you enter a whole number?\n")

    def bet_menu(self) -> None:
        flag = True
        while flag:
            limit = self.get_table_limit()
            print(f"CURRENT BET: {self.get_bet()}    TABLE MIN: ${limit}    TABLE MAX: ${limit * 10}\n\n")
            
            print(f"[m] BET MIN, [b] CUSTOM BET, [x] MAX BET: ${limit * 10}, [q] BACK\n")
            user_input = input("--> ").lower()[0]
            print()
            if user_input == 'm':
                self.set_bet(limit)
            elif user_input == 'b':
                self.custom_bet()
            elif user_input == 'x':
                self.set_bet(limit * 10)
            elif user_input == 'c':
                self.change_limit()
            elif user_input == 'q':
                print("Back to main menu...\n\n")
                return
            else:
                print("I'm sorry. I didn't catch that.\n") 

    def change_decks(self) -> None:
        flag = True
        valid_decks = [1, 2, 4, 8]
        while flag:
            print("Choose", end=" ")
            for x in range(len(valid_decks)-1):
                print(valid_decks[x], end=", ")
                
            print(f"or {valid_decks[-1]} decks:\n")
            try:
                user_input = int(input("--> "))
                print()
                if user_input in valid_decks:
                    self.set_deck([])
                    self.set_discard_pile([])
                    self.set_num_decks(user_input)
                    
                    self.generate_deck()
                    self.shuffle_deck()
                    print(f"Now using {user_input} decks.\n")
                    return
                else:
                    print("Invalid option.\n")
                    break
            except ValueError:
                print("I'm sorry. I didn't catch that.\n")

    def change_limit(self) -> None:
        flag = True
        while flag:
            print("MIN: $5    MAX: $750    MUST BE A MULTIPLE OF $5\n\nWhat would you like to change the limit to?\n\n")
            try:
                limit = int(input("--> "))
                if not limit % 5 == 0:
                    print("Please use a multiple of 5.\n")
                elif limit < 5 or limit > 750:
                    print("Outside limit bounds.\n")
                else:
                    self.set_table_limit(limit)
                    print(f"New limit set to ${limit}.\n")
                    flag = False   
            except ValueError:
                print("Make sure that you entered a whole number.\n")

    def table_menu(self) -> None:
        flag = True
        while flag:
            limit = self.get_table_limit()
            print(f"DECKS USED: {self.get_num_decks()}    TABLE MIN: ${limit}    TABLE MAX: ${limit * 10}\n\n")
            print("[d] CHANGE DECKS, [c] CHANGE LIMIT, [q] BACK\n")
            user_input = input("--> ").lower()[0]
            print()

            if user_input == 'd':
                self.change_decks()
            elif user_input == 'c':
                self.change_limit()
            elif user_input == 'q':
                flag = False
                print("Back to main menu...\n\n")
            else:
                print("I'm sorry. I didn't catch that.\n")
            
    def run(self) -> None:
        flag = True
        self.generate_deck()  # defaults to 1 deck
        self.shuffle_deck()

        while flag:
            print(logo + "\n")
            print(f"BANKROLL: ${self.get_chips()}    CURRENT BET: ${self.get_bet()}    ", end="")
            print(f"TABLE LIMIT: ${self.get_table_limit()}    DECKS USED: {self.get_num_decks()}\n\n")            
    
            print("Please choose from the following:\n")
            print("[d] DEAL CARDS, [m] BET MIN, [b] CHANGE BET, [t] TABLE OPTIONS, [q] QUIT\n")

            user_input = input("--> ").lower()[0]
            print()
    
            if user_input == 'd':
                print("Good luck!\n\n")
                self.play_round()
            elif user_input == 'm':
                self.set_bet(self.get_table_limit())
            elif user_input == 'b':
                self.bet_menu()
            elif user_input == 't':
                self.table_menu()
            elif user_input == 'q':
                flag = False
                chips = self.get_chips()
                sleep(self._TIMER)
                print(f"Cashing out for ${chips}.\n")
                sleep(self._TIMER)
                print("Thanks for playing!\n")
            else:
                print("I'm sorry, I didn't catch that.\n")
        sleep(self._TIMER)
        print("See you next time...")
