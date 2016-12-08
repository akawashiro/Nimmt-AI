import random
# from player import RamdomPlayer
# from player import HumanPlayer
from player import GreedyPlayer


class Game():

    def __init__(self):
        cards = self.make_card_list()
        random.shuffle(cards)
        self.players = []
        # Append players instance to players
        self.players.append(GreedyPlayer(cards[0:10], 0))
        self.players.append(GreedyPlayer(cards[10:20], 1))
        self.players.append(GreedyPlayer(cards[30:40], 2))
        self.players.append(GreedyPlayer(cards[40:50], 3))

        self.board = sorted(
            [[c] for c in cards[50:55]], key=lambda x: x[0][0])

    def one_turn(self):
        # Lis of (#player, his/her card)
        current_cards = []
        for (i, p) in enumerate(self.players):
            current_cards.append((i, p.show_cards(self.board, self.players)))
            print "player ", i, "shows ", current_cards[-1][1]

        current_cards = sorted(current_cards, key=lambda x: x[1][0])
        for (i, c) in enumerate(current_cards):
            if c[1][0] < self.board[0][-1][0]:
                r = self.players[c[0]].select_row(
                    self.board, self.players, current_cards[i:])
                self.players[c[0]].push_cards(self.board[r])
                self.board[r] = [c[1]]
            else:
                for j in reversed(range(0, len(self.board))):
                    if self.board[j][-1][0] < c[1][0]:
                        if len(self.board[j]) < 5:
                            self.board[j].append(c[1])
                        else:
                            self.players[c[0]].push_cards(self.board[j])
                            self.board[j] = [c[1]]
                        break
            self.board = sorted(self.board, key=lambda x: x[0][0])

    def play_game(self):
        for i in range(10):
            print "----------- turn ", i + 1, "----------"
            for cs in self.board:
                for c in cs:
                    print c,
                print ""

            self.one_turn()

            for (j, p) in enumerate(self.players):
                print "point of player ", j, "is ", self.players[j].get_point()
        return [p.get_point() for p in self.players]

    def make_card_list(self):
        c = [(n, 1) for n in range(1, 105)]
        c = map(lambda (n, c): (n, 2) if n % 5 == 0 else (n, c), c)
        c = map(lambda (n, c): (n, 3) if n % 10 == 0 else (n, c), c)
        c = map(lambda (n, c): (n, 5) if n % 11 == 0 else (n, c), c)
        return c


if __name__ == '__main__':
    rs = []
    for i in range(100):
        g = Game()
        rs.append(g.play_game())
    res = [0 for x in g.players]
    for r in rs:
        for i in range(len(res)):
            res[i] += r[i]
    print "----------- result ----------"
    for i, r in enumerate(res):
        print "sum of point of player ", i, "is ", r
