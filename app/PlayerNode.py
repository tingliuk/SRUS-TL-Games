class PlayerNode:
    def __init__(self,player):
        self._player=player
        self._next=None
        self._prev=None

    @property
    def player(self):  #return the player
        return self._player

    @property
    def next(self):  #return the next node
        return self._next

    @next.setter
    def next(self,node):  #set the next node in the list
        self._next=node

    @property
    def prev(self):  #return the previous node
        return self._prev

    @prev.setter
    def prev(self,node): #set the previous node
        self._prev=node

    def key(self):
        return self._player.uid # return the uid of the player

    def __str__(self): #return the string represent the node object
        return f"Node[Key:{self.key},Player:{self.player}]"