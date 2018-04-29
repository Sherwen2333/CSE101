# Zhaowen Huang
# zhaowhuang
# 111067886
# CSE 101
# Homework 5

from war_classes import *


# Part I
def create_deck():
    res = []
    i = 0
    while i < 4:
        z = 0
        while z < 13:
            res.append(Card(z, i))
            z += 1
        i += 1
    return res


# Part II
def deal_cards(deck):
    resa, resb = [], []
    for i in range(len(deck)):
        if i % 2 is 1:
            resb.append(deck[i])
        else:
            resa.append(deck[i])
    return Player(1, 0, resa), Player(2, 0, resb)


# Part III
def play_normal_round(player1, player2):
    i = 2
    while (len(player1._cards) is not 0
           and len(player2._cards) is not 0):
        resa, resb = player1.draw_card(), player2.draw_card()
        if resa._rank > resb._rank:
            return 1, i
        elif resa._rank < resb._rank:
            return 2, i
        else:
            i += 2
    return 0, 0


# Part IV
def check_game_winner(player1, player2):
    resa, resb = player1._score, player2._score
    if resa is resb:
        return 0
    elif resa > resb:
        return 1
    else:
        return 2


# Part V
def play_with_suits(player1, player2):
    i = 2
    while (len(player1._cards) is not 0 and len(player2._cards) is not 0):
        resa,resb = player1.draw_card(),player2.draw_card()
        if resa._suit is 3:
            if resb._suit is 1 \
                    or resb._suit is 2:
                return 1, i
            elif resb._suit is 0:
                return 2, i
            else:
                i += 2
        elif resa._suit is 1:
            if resb._suit is 3:
                return 2, i
            elif resb._suit is 2 \
                    or resb._suit is 0:
                return 1, i
            else:
                i += 2
        elif resa._suit is 2:
            if resb._suit is 0:
                return 1, i
            elif resb._suit is 3 \
                    or resb._suit is 1:
                return 2, i
            else:
                i += 2
        else:
            if resb._suit is 3:
                return 1, i
            elif resb._suit is 2 \
                    or resb._suit is 1:
                return 2, i
            else:
                i += 2
    return 0, 0


# Part VI
def play_with_scouts(player1, player2):
    iz = 2
    while (len(player1._cards) is not 0 and len(player2._cards) is not 0):
        resa,resb = player1.draw_card()._rank,player2.draw_card()._rank
        if (resa <= 3) and len(player1._cards) is not 0:
            resa = player1.draw_card()._rank + resa \
                   + 2
            iz += 1
        elif (resb <= 3) and len(player2._cards) is not 0:
            resb = player2.draw_card()._rank + resb \
                   + 2
            iz += 1
        if resa > resb:
            return 1, iz
        elif resa < resb:
            return 2, iz
        iz += 2
    return 0, 0
