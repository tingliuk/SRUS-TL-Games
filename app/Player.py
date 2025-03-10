class Player:
    def __init__(self,uid:str,name:str):# constructor
     self._uid = uid  #private instance variable for unique ID
     self._name = name #private instance variable for player name

    @property
    def uid(self):
        return self._uid #return the id of the player

    @property
    def name(self):
        return self._name #return the name of the player

    @classmethod
    def sum_of_ascii_values(key: str, size: int) -> int:
        total = 0
        for char in key:
            total += ord(char)
        return total % size

    def __hash__(self):
        return self.sum_of_ascii_values(self._uid,10)

    def __eq__(self, other):
        if isinstance(other, Player): #check if two players are equal base on uid
            return self._uid == other._uid
        return False

    def __str__(self):
        return f"Player[ID:{self._uid},Name:{self._name}]"
