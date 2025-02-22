class Player:
    def __init__(self,uid:str,name:str):# constructor
     self.__uid = uid  #private instance variable for unique ID
     self.__name = name #private instance variable for player name

    @property
    def uid(self):
        return self.__uid #return the id of the player

    @property
    def name(self):
        return self.__name #return the name of the player

    def __str__(self):
        return f"Player[ID:{self.__uid},Name:{self.__name}]"
