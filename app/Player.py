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

    def __str__(self):
        return f"Player[ID:{self._uid},Name:{self._name}]"
