from collections import Counter


class Player(object):

    def __init__(self, type_name):
        self.type = type_name
        self.memory = []

    def get_opponents_behavior(self, opponents_behavior: bool):
        self.memory.append(opponents_behavior)

    def behavior(self) -> bool:
        pass


class Cheater(Player):

    def __init__(self, type="Cheater"):
        super(Cheater, self).__init__(type)

    def behavior(self):
        return False


class Cooperator(Player):

    def __init__(self, type="Cooperator"):
        super(Cooperator, self).__init__(type)

    def behavior(self):
        return True


class Copycat(Player):
    def __init__(self, type="Copycat"):
        super(Copycat, self).__init__(type)
        self.memory = [True]

    def behavior(self):
        return self.memory[-1]


class Grudger(Player):
    def __init__(self, type="Grudger"):
        super(Grudger, self).__init__(type)
        self.memory = [True]

    def behavior(self):
        return all(self.memory)


class Detective(Copycat, Cheater):
    def __init__(self):
        super().__init__("Detective")
        self.starting_behavior = [True, True, False, True]
        self.was_deceived = False

    def get_opponents_behavior(self, opponents_behavior: bool):
        super().get_opponents_behavior(opponents_behavior)
        if not opponents_behavior:
            self.was_deceived = True

    def behavior(self):
        if self.starting_behavior:
            return self.starting_behavior.pop()
        elif self.was_deceived:
            return Copycat.behavior(self)
        else:
            return Cheater.behavior(self)


class Acquaintance(Player):
    def __init__(self):
        super().__init__("Acquaintance")
        self.round = 0

    def get_opponents_behavior(self, opponents_behavior: bool):
        super().get_opponents_behavior(opponents_behavior)
        self.round += 1

    def behavior(self):
        if self.round == 0:
            return True
        elif self.round == 1:
            if not self.memory[0]:
                return False
            else:
                return True
        else:
            if not self.memory[0]:
                return False
            elif not self.memory[1]:
                self.memory[1] = True
                return False
            else:
                return True


class Game(object):

    def __init__(self, matches=10):
        self.matches = matches
        self.registry = Counter()

    def play(self, player1: Player, player2: Player):
        for i in range(self.matches):
            operator_1 = player1.behavior()
            operator_2 = player2.behavior()
            if operator_1:
                if operator_2:
                    self.registry.update({player1.type: 2, player2.type: 2})
                else:
                    self.registry.update({player1.type: -1, player2.type: 3})
            else:
                if operator_2:
                    self.registry.update({player1.type: 3, player2.type: -1})
            player1.get_opponents_behavior(operator_2)
            player2.get_opponents_behavior(operator_1)

    def top3(self):
        for i in self.registry.most_common(3):
            print(i)


if __name__ == "__main__":
    game = Game(100)
    game.play(Cheater(), Cooperator())
    game.play(Cheater(), Copycat())
    game.play(Cheater(), Grudger())
    game.play(Cheater(), Detective())
    game.play(Cooperator(), Copycat())
    game.play(Cooperator(), Grudger())
    game.play(Cooperator(), Detective())
    game.play(Copycat(), Grudger())
    game.play(Copycat(), Detective())
    game.play(Grudger(), Detective())
    game.play(Acquaintance(), Cooperator())
    game.play(Acquaintance(), Cheater())
    game.play(Acquaintance(), Copycat())
    game.play(Acquaintance(), Grudger())
    game.play(Acquaintance(), Detective())
    game.top3()
