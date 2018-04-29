# Initialize card data
CLUBS = u'\u2663'
SPADES = u'\u2660'
DIAMONDS = u'\u2666'
HEARTS = u'\u2665'
suits = {0: CLUBS, 1: SPADES, 2: DIAMONDS, 3: HEARTS}
ranks = {k: k + 2 for k in range(9)}  # maps 0->2, 1->3, ..., 8:10
ranks[9] = 'J'
ranks[10] = 'Q'
ranks[11] = 'K'
ranks[12] = 'A'

print_output = False


# DO NOT CHANGE THE CONTENTS OF THIS FILE #
# DO NOT CHANGE THE CONTENTS OF THIS FILE #
# DO NOT CHANGE THE CONTENTS OF THIS FILE #

class Card:
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    def __str__(self):
        return str(ranks[self._rank]) + str(suits[self._suit])

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self._rank == other._rank and self._suit == other._suit


# DO NOT CHANGE THE CONTENTS OF THIS FILE #
# DO NOT CHANGE THE CONTENTS OF THIS FILE #
# DO NOT CHANGE THE CONTENTS OF THIS FILE #

class Player:
    def __init__(self, player_num, score, cards):
        self._player_num = player_num
        self._score = score
        self._cards = cards

    def __str__(self):
        return 'Player(' + str(self._player_num) + ',' + str(self._score) + ',' + \
               str(self._cards) + ')'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self._player_num == other._player_num and self._score == other._score and \
               self._cards == other._cards

    def draw_card(self):
        card = self._cards.pop(0)
        if print_output: print('Player', self._player_num, 'drew', card)
        return card

# DO NOT CHANGE THE CONTENTS OF THIS FILE #
# DO NOT CHANGE THE CONTENTS OF THIS FILE #
# DO NOT CHANGE THE CONTENTS OF THIS FILE #
