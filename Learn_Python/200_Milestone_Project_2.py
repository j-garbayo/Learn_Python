#BLACKJACK GAME

#TODO Add Double-Downs.
#TODO Add Card Splits.

import random
import collections

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

class croupier(object):
    
    game_deck = deck()
    hand = []

    def __init__(self):
        #Gives two cards to the croupier
        self.hand = []
        self.deal_cards(self,2)

    def deal_cards(self, player_object, ncards = 1):
        for i in range(1,ncards+1):
            card = self.game_deck.get_card()
            player_object.hand.append(card)
                   
    def hand_value(self, player_object):
        #HIGHLIGHT - Function Doc Strings!
        '''
        Calculates the value of the hand of the player.
        '''
        #HIGHLIGHT use of collections.Counter (imported) to count elements within a list of tuples
        #HIGHLOGHT use of sum
        #Generates a dictionary with
            #Keys equal to the cards name or value
            #Values equal to the number of occurrences of the card
        hand_count = collections.Counter(elem[0] for elem in player_object.hand)

        n_aces = hand_count["A"]
        #print "aces: " + str(n_aces)

        #Counts the number of Js, Ks, Qs
        #HIGHLIGHT - Count the number of occurrences of an element in a list.
        n_specials = hand_count["K"] + hand_count["J"] + hand_count["Q"]
        hand_value = n_specials*10
        #print "specials: " + str(n_specials)
        
        #First, the value without aces is calculated:
        for card in player_object.hand:
            card_value = card[0]
            if type(card_value) == int:
                hand_value += card_value

        #Finally, if there are aces present, their value is calculated:
        if n_aces <> 0:
            margin = 21 - hand_value
            if margin < 11:
                hand_value += n_aces
            elif margin == 11 and n_aces == 1:
                hand_value += 11
            elif margin == 11 and n_aces > 1:
                hand_value += n_aces
            elif margin > 11 and margin - 11 - (n_aces-1) >= 0:
                hand_value += 11 + (n_aces-1)
            else:
                hand_value += n_aces

        return hand_value
        
    def payout(self, player_object):
        #HIGHLIGHT: Type-hinting in PTVS. This is PTVS specific! (Visual Studio)
        #Python 3 supports directly type hinting
        #Oder IDEs support better type-hinting for Python than visual studio

        #assert isinstance(player_object, player)

        #HIGHLIGHT: Type-hinting alternative in PTVS. This code wont execute but helps
        #visual studio figure out what is going on

        if False:
            player_object = player()

        croupier_hand = self.hand_value(self)
        player_object_hand = self.hand_value(player_object)

        if player_object_hand < croupier_hand or player_object_hand > 21:
            player_object.money -= player_object.bet
        elif player_object_hand > croupier_hand and player_object_hand < 21:
            player_object.money += player_object.bet
        elif player_object_hand == 21:
            player_object.money += player_object.bet *1.5
        
class player(object):

    #TODO: Create a Method to Split Hand.

    hand = []   #List containing the player's hand of cards. It will be handled by the croupier object.
    bet = 50    #Default initial bet.

    def __init__(self, money = 1000):
        self.money = money
        self.hand = []
        self.bet = 50

Juan = player()
the_croupier = croupier()
the_croupier.deal_cards(Juan, 2)
print Juan.hand
print the_croupier.hand
print "Juan " + str(the_croupier.hand_value(Juan))
print "Croupier " + str(the_croupier.hand_value(the_croupier))
print "Juan's bet was: " + str(Juan.bet)
print "Juan's money was: " + str(Juan.money)
the_croupier.payout(Juan)
print "Juan's money is: " + str(Juan.money)