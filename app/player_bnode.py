class PlayerBNode:
    def __init__(self, player):
        self._player = player
        self._left = None
        self._right = None

    @property
    def player(self):# property for player
        return self._player

    @player.setter
    def player(self, player):
        self._player = player

    @property
    def left(self):# property for left node
        return self._left

    @left.setter
    def left(self, node):
        self._left = node

    @property
    def right(self):# property for left node
        return self._right

    @right.setter
    def right(self, node):
        self._right = node
