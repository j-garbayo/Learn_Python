#BLACKJACK GAME

#TODO Add Double-Downs.
#TODO Add Card Splits.

import random
import collections
import os

'''
OBJECTS DEFINITION CODE
'''

class deck(object):

    cards = []      #List representing the deck of cards

    def __init__(self):
        self.reset_deck()

    def __str__(self):

        return str(self.cards)        

    def reset_deck(self):
        #SUIT: Hearts, Diamons, Club, Spade
        suits = ['H', 'D', 'C', 'S']
        values = ['A'] + [v for v in range (2,11)] + ['J', 'Q', 'K']
        #HIGHLIGHT - NESTED FORs in List Comprehensions
        self.cards = [(value, suit) for suit in suits for value in values]

    def get_card(self):
       
        index = random.randint(0,len(self.cards)-1)        
        card = self.cards[index]
        self.cards.pop(index)
        return card

class blackjack_person(object):

    def __init__(self):
        self.hand = []
        self.hand_value = 0


    def update_hand_value(self):
        #HIGHLIGHT - Function Doc Strings!
        '''
        Calculates the value of the hand of the player and stores it in the attribute hand_value
        '''
        #HIGHLIGHT use of collections.Counter (imported) to count elements within a list of tuples
        #HIGHLIGHT use of sum
        #Generates a dictionary with
            #Keys equal to the cards name or value
            #Values equal to the number of occurrences of the card
        hand_count = collections.Counter(elem[0] for elem in self.hand)

        #Counts the nimber of aces.
        n_aces = hand_count["A"]

        #Counts the number of Js, Ks, Qs
        #HIGHLIGHT - Count the number of occurrences of an element in a list.
        n_specials = hand_count["K"] + hand_count["J"] + hand_count["Q"]
        self.hand_value = n_specials*10
        
        #First, the value without aces is calculated:
        for card in self.hand:
            card_value = card[0]
            if type(card_value) == int:
                self.hand_value += card_value

        #Finally, if there are aces present, their value is calculated:
        if n_aces <> 0:
            margin = 21 - self.hand_value
            if margin < 11:
                self.hand_value += n_aces
            elif margin == 11 and n_aces == 1:
                self.hand_value += 11
            elif margin == 11 and n_aces > 1:
                self.hand_value += n_aces
            elif margin > 11 and margin - 11 - (n_aces-1) >= 0:
                self.hand_value += 11 + (n_aces-1)
            else:
                self.hand_value += n_aces

class croupier(blackjack_person):

    def __init__(self):

        #Gives two cards to the croupier and updates its hand value
        blackjack_person.__init__(self)
        self.game_deck = deck()
        self.deal_cards(self,2)
        self.show_full_hand = False

    def __str__(self):

        stars = "******************************************"
        printout = stars
        printout += "\n" + "*" + " " *(len(stars)-2) + "*"

        strng = "* Croupier:"
        printout += "\n" + strng + " " * (len(stars) - len(strng)-1) + "*"

        if self.show_full_hand == False:        
            strng = "*      - Half hand:  " + str(self.hand[0])
        else:
            strng = "*      - Hand:  " + str(self.hand)         

        printout += "\n" + strng + " " * (len(stars) - len(strng)-1) + "*"
        printout += "\n" + "*" + " " *(len(stars)-2) + "*"
        printout += "\n" + stars
        printout += "\n"

        return printout

    def deal_cards(self, blckjck_person, ncards = 1):

        #deals ncards to the passed blckjck_person and updates its hand_value

        for i in range(1,ncards+1):
            card = self.game_deck.get_card()
            blckjck_person.hand.append(card)

        blckjck_person.update_hand_value()                         

    def update_payout_money(self, player_object):
        #HIGHLIGHT: Type-hinting in PTVS. This is PTVS specific! (Visual Studio)
        #Python 3 supports directly type hinting
        #Oder IDEs support better type-hinting for Python than visual studio

        #assert isinstance(player_object, player)

        #HIGHLIGHT: Type-hinting alternative in PTVS. This code wont execute but helps
        #visual studio figure out what is going on
        if False:
            player_object = player()

        self.update_hand_value()
        player_object.update_hand_value()
        
        if player_object.hand_value < self.hand_value or player_object.hand_value > 21:
            player_object.payout = -player_object.bet
        elif player_object.hand_value > self.hand_value and player_object.hand_value < 21:
            player_object.payout = player_object.bet
        elif player_object.hand_value == 21:
            player_object.payout = player_object.bet*1.5

        player_object.money += player_object.payout

class player(blackjack_person):

    #TODO: Create a Method to Split Hand.

    def __init__(self, name, money = 1000):
        
        blackjack_person.__init__(self)
        self.name = name
        self.money = money
        self.bet = 50
        self.payout = 0

    def __str__(self):
        
        printout = self.name + ":"
        printout += "\n" + "       - Hand:  " + str(self.hand)
        printout += "\n" + "       - Money: " + str(self.money)
        #printout += "\n" + "       - Bet:   " + str(self.bet)
        printout += "\n"

        return printout

'''
GAME EXECUTION CODE
'''

print "   Welcome to the Super Black Jack Game   ".upper()
print "------------------------------------------" + "\n"

player_info_input = False
#CREATE'S CROUPIER OBJECT
the_croupier = croupier()

while True:

    '''
    ASK FOR THE PLAYERS NAMES AND INITIAL MONEY
    '''
    if player_info_input == False:
        #HIGHLIGHT - "try:" to check for integer values
        #ALTERNATIVE - Split string in a list to check for certain value. See milestone project 1
        while True:
            try:
                n_players = int(raw_input("please select the number of players (1 to 4): "))
            except:
                continue
            else:
                if n_players in range(1,5):
                    break
    
        players = [] #list containing the player objects

        for i in range(1, n_players+1):
            os.system("cls") 
            name = raw_input("please enter player's " + str(i) +" name: ")
            while True:
                try:
                    money = int(raw_input("please enter " + name +"'s money (integer value): "))
                except:
                    continue
                else:
                    break

            new_player = player(name, money)
            print(new_player)
            players.append(new_player)     

        player_info_input = True

    '''
    GET THE PLAYERS BETS
    '''
    for i in range(1, n_players+1):
        os.system("cls")
        while True:
            try:
                bet = int(raw_input("please enter " + players[i-1].name + "'s bet (integer value): "))
            except:
                continue
            else:
                players[i-1].bet = bet
                break  

    '''
    DEAL AND PRINT INITIAL CARDS
    '''
    #HIGHLIGHT - CLEAR TERMINAL (import os). Note in Linux: os.system("clear")
    os.system("cls")
    print ("          Lets see those cards!:          ")
    print ("------------------------------------------" + "\n")
    
    print(the_croupier)
    
    for i in range(1, n_players+1):
        the_croupier.deal_cards(players[i-1], 2)
        print(players[i-1])

    raw_input("\n" + "Press ENTER to continue")

    '''
    ASK FOR ACTION INPUT FROM EACH PLAYER
    '''

    #BASIC HIT OR PASS
    for i in range(1, n_players+1):
        os.system("cls")
        print(the_croupier)
        print(players[i-1])

        if players[i-1].hand_value <> 21:        

            while True:
                action = raw_input(players[i-1].name + ", hit or pass?: ")
                action = action.lower()
                if action == "hit":
                    the_croupier.deal_cards(players[i-1], 1)
                    os.system("cls")
                    print(the_croupier)
                    print(players[i-1])
                    if players[i-1].hand_value > 21:
                        raw_input("\nYOU HAVE BUSTED!")
                        break
                    elif players[i-1].hand_value == 21:
                        raw_input("\nBLACKJACK!!")
                        break
                    continue
                elif action == "pass":
                    break

        else:
            raw_input("\nBLACKJACK!!")

    '''
    REPRINT BOARD WITH REVEALED CARDS
    '''
    the_croupier.show_full_hand = True    

    os.system("cls")    
    print("    Let's see who wins and who loses!     ")
    print("------------------------------------------" + "\n")       

    print(the_croupier)
    for i in range(1, n_players+1):
        print(players[i-1])

    raw_input("\n PRESS 'ENTER' TO CONTINUE")

    '''
    EVALUATE PAYOUTS AND UPDATE ACCOUNTS
    '''

    for i in range(1, n_players+1):
        the_croupier.update_payout_money(players[i-1])

    os.system("cls")    
    print("      And here we have the results!       ")
    print("------------------------------------------" + "\n")     

    for i in range(1, n_players+1):
        printout = "- " + str(players[i-1].name) + "'s payout" + "."*(28-len(players[i-1].name))
        if players[i-1].payout > 0:
            printout += "+" + str(players[i-1].payout)
        else:
            printout += str(players[i-1].payout)
        print(printout)

    print("\n")

    for i in range(1, n_players+1):
        printout = "- " + str(players[i-1].name) + "'s money" + "."*(29-len(players[i-1].name))
        printout += str(players[i-1].money)
        print(printout)   

    raw_input("\n PRESS 'ENTER' TO CONTINUE")

#    '''
#    ASK FOR CONTINUE OR QUIT
#    '''
    while True:
        action = raw_input("Continue or Quit?: ")
        action = action.lower()
        if action in "continue quit".split():
            break

    if action == "continue":
        the_croupier.__init__()
        for i in range(1, n_players+1):
            players[i-1].__init__(players[i-1].name, players[i-1].money)
    else:
        break