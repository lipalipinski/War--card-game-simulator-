'''
War v1 by JL 2022
'''
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12,
          'King': 13, 'Ace': 14}


class Card():
    '''
    single card class
    '''

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck():
    '''
    52 cards deck
    '''

    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        '''
        shuffle the deck
        '''
        random.shuffle(self.all_cards)

    def deal(self):
        '''
        pop one card from the deck
        '''
        return self.all_cards.pop()


class Player():
    '''
    player holding cards
    '''

    def __init__(self, name):
        self.name = name
        self.hand = []

    def __str__(self):
        return '+'*len(self.hand)

    def add_cards(self, cards):
        '''
        cards - a card or a list of cards.
        adds cards to player's hand
        '''
        if isinstance(cards, list):
            random.shuffle(cards)
            self.hand.extend(cards)
        else:
            self.hand.append(cards)

    def pick_card(self):
        '''
        returns one card from the top of player's hand
        '''
        return self.hand.pop(0)


# THE GAME
player1 = Player('Player One')
player2 = Player('Player Two')
new_deck = Deck()
new_deck.shuffle()

# deal the cards
for card in range(26):
    player1.add_cards(new_deck.deal())
    player2.add_cards(new_deck.deal())

turn_counter = 0
game_on = True
while game_on:  # main loop

    turn_counter += 1
    print(f'Round {turn_counter}')
    print(player1,player2)

    if len(player1.hand) == 0:  # check if player 2 has won
        print(f'{player2.name} WINS!')
        game_on = False
        break
    elif len(player2.hand) == 0:  # check if player 1 has won
        print(f'{player1.name} WINS!')
        game_on = False
        break

    player1_cards = []
    player2_cards = []

    player1_cards.append(player1.pick_card())
    player2_cards.append(player2.pick_card())

    at_war = True
    while at_war:

        if player1_cards[-1].value > player2_cards[-1].value:
            player1.add_cards(player1_cards)
            player1.add_cards(player2_cards)
            at_war = False
        elif player1_cards[-1].value < player2_cards[-1].value:
            player2.add_cards(player1_cards)
            player2.add_cards(player2_cards)
            at_war = False
        else:
            print('WAR!')
            if len(player1.hand) < 5:
                print(f'{player1.name} has to few cards ({len(player1.hand)}) to go to WAR!')
                print(f'{player2.name} wins!')
                at_war = False
                game_on = False
            elif len(player2.hand) < 5:
                print(f'{player2.name} has to few cards ({len(player2.hand)}) to go to WAR!')
                print(f'{player1.name} wins!')
                at_war = False
                game_on = False
            else:
                for num in range(5):
                    player1_cards.append(player1.pick_card())
                    player2_cards.append(player2.pick_card())
