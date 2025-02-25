class PlayerNode:
    def __init__(self,player):
        self.__player=player
        self.__next=None
        self.__prev=None

    @property
    def player(self):  #return the player
        return self.__player

    @property
    def next(self):  #return the next node
        return self.__next

    @next.setter
    def next(self,node):  #set the next node in the list
        self.__next=node

    @property
    def prev(self):  #return the previous node
        return self.__prev

    @prev.setter
    def prev(self,node): #set the previous node
        self.__prev=node

    def key(self):
        return self.__player.uid # return the uid of the player

    def __str__(self): #return the string represent the node object
        return f"Node[Key:{self.key},Player:{self.player}]"