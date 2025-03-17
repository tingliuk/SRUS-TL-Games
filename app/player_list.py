from app.PlayerNode import  PlayerNode

class PlayerList:
    def __init__(self):
        self._head=None
        self._tail=None

    @property
    def head(self):  # return the head node for testing
        return self._head

    @property
    def tail(self):
        return self._tail

    def is_empty(self):
        return self._head is None #return True if list is empty,otherwise False

    def insert_head_node(self,player):
        new_node=PlayerNode(player)#insert a new player node at the head of the list
        if self._head is not None:
            self._head.prev=new_node
            new_node.next=self._head
        self._head=new_node

    def insert_tail_node(self,player):#insert a new player node at the end of the list
        node=PlayerNode(player)
        if self._tail is not None:
             self._tail.next=node
             node.prev=self._tail
             node.next=None
        else:
            self._head=node
        self._tail=node


    def delete_head_node(self):
        if self._head is None: #empty list, nothing to delete
            return
        elif self._head==self._tail:# list only has one node
            self._head=None
            self._tail=None
        else:
            self._head=self._head.next
            self._head.prev=None

    def delete_tail_node(self):
        if self._tail is None:#empty list, nothing to delete
            return
        elif self._head==self._tail:# list only has one node
            self._head=None
            self._tail=None
        else:
            self._tail=self._tail.prev
            self._tail.next=None

    def delete_node_by_key(self,key):
        current=self._head
        while self._head is not None:
            if current.player.uid==key:
                if current==self._head:#key on head
                    self.delete_head_node()
                elif current==self._tail:#key on tail
                    self.delete_tail_node()
                else:#key in between head and tail
                    current.prev.next=current.next
                    current.next.prev=current.prev
                return
            current=current.next #move to next node
    def display(self,forward=True):
        if self.is_empty():
            print("List is Empty")

        if self._head==self._tail:
            print(f"ID:{self._head.player.uid},Name:{self._head.player.name}")

        if forward:
            current=self._head
            print("List from head to tail")
            while current:
                print(f"ID: {current.player.vid}, Name: {current.player.name}")
                current=current.next
        else:
            current=self._tail
            print("List from tail to head")
            while current:
                print(f"ID: {current.player.vid}, Name: {current.player.name}")
                current = current.prev











