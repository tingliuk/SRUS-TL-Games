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

    def sort_quickly(self, players):
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
        return self.sort_quickly(left) + [pivot] + self.sort_quickly(right)
