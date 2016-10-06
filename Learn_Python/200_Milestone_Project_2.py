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
        
    def print_cards(self):
        print(self.cards)

class blackjack_person(object):

    hand = []
    hand_value = 0

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
    
    game_deck = deck()
    show_full_hand = False    #When print(croupier) shall show all the cards in the
                              #croupier's hand, change to true.
                              #TODO: investigate how the type of this attribute can be restricted
                              #      to make it only boolean type.

    def __init__(self):

        #Gives two cards to the croupier and updates its hand value
        self.deal_cards(self,2)

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

    def payout(self, player_object):
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
            payout = -player_object.bet
        elif player_object.hand_value > self.hand_value and player_object.hand_value < 21:
            payout = player_object.bet
        elif player_object.hand_value == 21:
            payout = player_object.bet*1.5

class player(blackjack_person):

    #TODO: Create a Method to Split Hand.

    def __init__(self, name, money = 1000):
        self.name = name
        self.money = money
        self.bet = 50

    def __str__(self):
        
        printout = self.name + ":"
        printout += "\n" + "       - Hand:  " + str(self.hand)
        printout += "\n" + "       - Money: " + str(self.money)
        printout += "\n" + "       - Bet:   " + str(self.bet)
        printout += "\n"

        return printout


#'''
#GAME EXECUTION CODE
#'''

#print "Welcome to the Super Black Jack Game".upper()
#print "------------------------------------"

#player_info_input = False
##CREATE'S CROUPIER OBJECT
#the_croupier = croupier()

#while True:

#    '''
#    ASK FOR THE PLAYERS NAMES AND INITIAL MONEY
#    '''
#    if player_info_input == False:
#        #HIGHLIGHT - "try:" to check for integer values
#        #ALTERNATIVE - Split string in a list to check for certain value. See milestone project 1
#        while True:
#            try:
#                n_players = int(raw_input("please select the number of players (1 to 4): "))
#            except:
#                continue
#            else:
#                if n_players in range(1,5):
#                    break
    
#        players = [] #list containing the player objects

#        for i in range(1, n_players+1):
#            os.system("cls") 
#            name = raw_input("please enter player's " + str(i) +" name: ")
#            while True:
#                try:
#                    money = int(raw_input("please enter " + name +"'s money (integer value): "))
#                except:
#                    continue
#                else:
#                    break

#            new_player = player(name, money)
#            players.append(new_player)     

#        player_info_input = True

#        #GETS THE PLAYER'S BETS:
#        for i in range(1, n_players+1):
#            os.system("cls")
#            while True:
#                try:
#                    bet = int(raw_input("please enter " + players[i-1].name + "'s bet (integer value): "))
#                except:
#                    continue
#                else:
#                    players[i-1].bet = bet
#                    break  

#    '''
#    DEAL AND PRINT INITIAL CARDS
#    '''
#    #HIGHLIGHT - CLEAR TERMINAL (import os). Note in Linux: os.system("clear")
#    os.system("cls")
#    print ("Lets see those cards!: ")
#    print ("---------------------- " + "\n")
        
#    the_croupier.print_info(True)

#    for i in range(1, n_players+1):
#        the_croupier.deal_cards(players[i-1], 2) 
#        players[i-1].print_info()

#    raw_input("\n" + "Press ENTER to continue")

#    #TODO
#    '''
#    ASK FOR ACTOPM INPUT FROM EACH PLAYER
#    '''
#    for i in range(1, n_players+1):
#        os.system("cls")
#        the_croupier.print_info(True)
#        players[i-1].print_info()

#        while True:
#            action = raw_input(players[i-1].name + ", hit or pass?")
#            action = action.lower()
#            if action == "hit":
#                the_croupier.deal_cards(players[i-1], 1)
                
#                pass
#            elif action == "pass":
#                pass
                


#    #TODO
#    '''
#    REPRINT BOARD WITH REVEALED CARDS
#    '''
#    os.system("cls")
#    the_croupier.print_info(False)
#    for i in range(1, n_players+1):
        
#        pass

#    #TODO
#    '''
#    EVALUATE PAYOUTS AND UPDATE ACCOUNTS
#    '''
    
#    #TODO
#    '''
#    ASK FOR CONTINUE OR QUIT
#    '''       