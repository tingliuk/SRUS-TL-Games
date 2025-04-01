import random
class Player:
    def __init__(self, name, uid, score: int):
        self.name = name
        self.uid = uid
        self._score = score

    def __eq__(self, other):
        return self.score == other.score

    def __lt__(self, other):
        return self.score <= other.score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):

        if value < 0:
            raise ValueError("Score cannot be negative.")
        self._score = value

    def __repr__(self):
        return f"Player: {self.name}, Score: {self.score}"
    @staticmethod
    def sort_quickly( players):
        if len(players) <= 1:
            return players
        pivot = players[0]
        left = []
        right = []
        for x in players[1:]:
            if x < pivot:
                left.append(x)
            else:
                right.append(x)
        return Player.sort_quickly(left) + [pivot] + Player.sort_quickly(right)
    @classmethod
    def sort_descending(cls, players):
        if len(players) <= 1:
            return players
        #pivot = players[0]
        pivot = random.choice(players)  # Choose a random pivot
        left = [p for p in players if p.score > pivot.score]  # Higher scores go left
        middle = [p for p in players if p.score == pivot.score]  # Handle duplicates
        right = [p for p in players if p.score < pivot.score]  # Lower scores go right
        return cls.sort_descending(left) + middle + cls.sort_descending(right)

