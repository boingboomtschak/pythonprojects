from random import randint
from random import choice
class Deck(object):
    def __init__(self):
        self.cards = ("2,3,4,5,6,7,8,9,J,Q,K,A")
        self.spades = self.cards.split(",")
        self.clubs = self.cards.split(",")
        self.diamonds = self.cards.split(",")
        self.hearts = self.cards.split(",")
        self.deck = (self.spades, self.clubs, self.diamonds, self.hearts)
class Player(object):
    def __init__(self, deck):
        self.cards = []
        self.done = False #determines whether player is done playing their hand or not
        randsuit = randint(0,3)
        randcard = randint(0, (len(deck.deck[randsuit])-1))
        self.cards.append(deck.deck[randsuit][randcard])
        del deck.deck[randsuit][randcard]
        #print (self.cards) #debug
        randsuit = randint(0,3)
        randcard = randint(0, (len(deck.deck[randsuit])-1))
        self.cards.append(deck.deck[randsuit][randcard])
        del deck.deck[randsuit][randcard]
        #print (self.cards) #debug
    def hit(self, deck):
        randsuit = randint(0,3)
        randcard = randint(0, (len(deck.deck[randsuit])-1))
        self.cards.append(deck.deck[randsuit][randcard])
        del deck.deck[randsuit][randcard]
    def stay(self):
        self.done = True
    def value(self):
        self.tvalue = 0 #tvalue = total value
        for card in self.cards:
            if card == "J":
                self.tvalue = self.tvalue + 10
            elif card == "Q":
                self.tvalue = self.tvalue + 10
            elif card == "K":
                self.tvalue = self.tvalue + 10
            elif card == "A":
                pass
            else:
                self.tvalue = self.tvalue + int(card)
        if "A" in self.cards:
            if self.tvalue + 11 <= 21:
                self.tvalue = self.tvalue + 11
            else:
                self.tvalue = self.tvalue + 1
class Game(object):
    def hand(self, player1, player2, deck):
        print("**A new hand has begun**")
        while player1.done == False or player2.done == False:
            player1.value()
            player2.value()
            print ("Your hand contains: " + ", ".join(player1.cards))
            print ("Your hand has a value of " + str(player1.tvalue))
            action = raw_input("Would you like to hit or stay (type 'h' or 's'):")
            if action == "h":
                player1.hit(deck)
                player1.value()
                if player1.tvalue > 21:
                    print("You went over 21!")
                    player1.stay()
                else:
                    print("Your hand now has a value of " + str(player1.tvalue))   
            elif action == "s":
                player1.stay()
            else:
                print ("That is not a valid action!")
            while player2.done == False:
                if player2.tvalue <= 16:
                    player2.hit(deck)
                    player2.value()
                elif player2.tvalue > 21:
                    player2.stay()
                else:
                    player2.stay()
        print("The round is over.")
        player1.value()
        player2.value()
        print("Your card value was " + str(player1.tvalue))
        print("Your opponents card value was " + str(player2.tvalue))
        if player1.tvalue > 21 and player2.tvalue > 21:
            print("You both went over 21 and lost!")
        elif player1.tvalue > 21 and player2.tvalue <= 21:
            print("You lost this round...")
        elif player2.tvalue > 21 and player1.tvalue <= 21:
            print("You won this round!")
        elif player1.tvalue > player2.tvalue:
            print("You won this round!")
        elif player2.tvalue > player1.tvalue:
            print("You lost this round...")
        else:
            print("You tied this round!")
#class definition ends, class references begin
game = Game() #creates new "Game" object
deck1 = Deck() #creates new "Deck" object
playerT = Player(deck1) #creates new player "playerT"
playerA = Player(deck1) #creates new player "playerA"
game.hand(playerT, playerA, deck1) #starts a new hand as a method of the "Game" object, taking two players (user vs AI) and the deck used as arguments
