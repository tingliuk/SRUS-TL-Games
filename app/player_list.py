from app.PlayerNode import  PlayerNode

class PlayerList:
    def __init__(self):
        self.__head=None
        self.__tail=None

    def is_empty(self):
        return self.__head is None #return True if list is empty,otherwise False

    def insert_head_node(self,player):
        new_node=PlayerNode(player)#insert a new player node at the head of the list
        if self.__head is not None:
            self.__head.prev=new_node
            new_node.next=self.__head
        self.__head=new_node

    def get_head(self):#return the head node for testing
        return self.__head

    def get_tail(self):
        return self.__tail


    def insert_tail_node(self,player):#insert a new player node at the end of the list
        node=PlayerNode(player)
        if self.__head is not None:
             self.__tail.next=node
             node.prev=self.__tail
             node.next=None
        self.__tail=node
        self.__head=node

    def delete_head_node(self,player):
        if self.__head is None: #empty list, nothing to delete
            return
        elif self.__head==self.__tail:# list only has one node
            self.__head=None
            self.__tail=None
        else:
            self.__head.next=self.__head
            self.__head,prev=None

    def delete_tail_node(self,player):
        if self.__head is None:#empty list, nothing to delete
            return
        elif self.__head==self.__tail:# list only has one node
            self.__head=None
            self.__tail=None
        else:
            self.__tail.prev=self.__tail
            self.__tail.next=None











