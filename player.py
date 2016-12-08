# To make conclete player,
# inherit Player class and define show_cards and select_row
from abc import *


class Player(object):

    def __init__(self, cards, id_num):
        self.cards = cards
        self.id = id_num
        self.pushed_cards = []

    @abstractmethod
    def show_cards(self, board, players):
        pass

    @abstractmethod
    def select_row(self, board, players, current_cards):
        pass

    def get_point(self):
        return sum(map(lambda x: x[1], self.pushed_cards))

    def push_cards(self, cards):
        self.pushed_cards += cards


class RamdomPlayer(Player):

    def __init__(self, cards, id_num):
        super(RamdomPlayer, self).__init__(cards, id_num)

    def show_cards(self, board, players):
        c = self.cards[0]
        self.cards = self.cards[1:]
        return c

    def select_row(self, board, players, current_cards):
        return 0


class HumanPlayer(Player):

    def __init__(self, cards, id_num):
        cards = sorted(cards)
        super(HumanPlayer, self).__init__(cards, id_num)

    def show_cards(self, board, players):
        print "your cards are"
        for (i, c) in enumerate(self.cards):
            print "card number ", i, "is ", c
        inp = input("Please input card number :")
        c = self.cards[inp]
        self.cards = self.cards[0:inp] + self.cards[inp + 1:]

        return c

    def select_row(self, board, players, current_cards):
        inp = input("Please input row number :")
        return inp


class GreedyPlayer(Player):

    def __init__(self, cards, id_num):
        cards = sorted(cards)
        super(GreedyPlayer, self).__init__(cards, id_num)

    def show_cards(self, board, players):
        # i th element of costs is (expected point, expected cost)
        costs = []
        for c in self.cards:
            if c[0] < board[0][-1][0]:
                a = sorted(
                    map(lambda b: sum(map(lambda x: x[1], b)), board))[0]
                costs.append((a, 0))
            else:
                ins = 0
                for ins in reversed(range(0, len(board))):
                    if board[ins][-1][0] < c[0]:
                        break
                if 5 == len(board[ins]):
                    a = sum(map(lambda x: x[1], board[ins]))
                    costs.append((a, 0))
                else:
                    s = float(c[0] - board[ins][-1][0]) / (5 - len(board[ins]))
                    costs.append((0, s))
        min_cost = (100000, 0)
        c_n = 0
        for i in range(len(self.cards)):
            if costs[i] < min_cost:
                min_cost = costs[i]
                c_n = i
        c = self.cards[c_n]
        self.cards = self.cards[:c_n] + self.cards[c_n + 1:]
        return c

    def select_row(self, board, players, current_cards):
        costs = []
        for i, b in enumerate(board):
            costs.append((i, sum(map(lambda x: x[1], b))))
        costs = sorted(costs, key=lambda x: x[1])
        return costs[0][0]
