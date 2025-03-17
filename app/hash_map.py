from tkinter.font import names

from app.player_list import PlayerList
from app.Player import Player

class PlayerHashMap:
    def __init__(self,size=10):
        self._size=size
        self._table=[PlayerList()for _ in range(size)]
        self._count=0

    def _hash(self,key):
        return hash(key)%self._size   #hash function to get the index for a given key

    def get_index(self,key:str | Player) -> int:  #return the index where the player should be placed
        if isinstance(key,Player):  #if the key is an instance of the Player class, it uses built-in hash function on the Player object.
            return hash(key)%self._size
        else:#If the key is a str, it calls a class method
            return Player.sum_of_ascii_values(key,10)

    def __setitem__(self, key:str ,name:str) -> None:
        index = self.get_index(key)
        player_list=self._table[index]   # place the playerlist at the index

        current=player_list.head  #check if the player already exist
        while current:
            if current.player.uid==key:
                current.player._name=name
                return
            current=current.next

        new_player=Player(key,name)   #if player doesn't exist,create and insert
        player_list.insert_tail_node(new_player)  #insert new player at the tail
        self._count+=1

    def __getitem__(self, key:str):
        index = self.get_index(key)  #get the index
        current=self._table[index].head

        while current:  #iterate through the linklist to find the player
            if current.player.uid==key:
                return current.player  # return the found player
            current=current.next

        return None # if not found

    def __len__(self):
        return self._count  #return the number of players in hash map

    def __delitem__(self,key:str,name:str):
        index = self.get_index(key)   #get the index
        self._table[index].delete_node_by_key(key)   #delete the player from linklist
        self._count -= 1

    def display(self):
        for index, player_list in enumerate(self._table):# loop through the hash table to print the index
            if player_list.head is not None:  # print non-empty lists
                print(f"Index {index}: ", end="")
                current = player_list.head  #
                while current: #loop through the linklist to print the player's uid and name
                    print(f"[{current.player.uid}: {current.player.name}]", end=" -> ")
                    current = current.next





