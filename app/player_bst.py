from player_bnode import PlayerBNode
class PlayerBST:
    def __init__(self):
        self._root=None
    @property
    def root(self):
        return self._root

    def insert(self,player):
        if self._root is None:
            self._root=PlayerBNode(player)
        else:
            self._insert_recursive(self._root,player)

    def _insert_recursive(self,current_node,player):
        if player.name<current_node.player.name:
            if current_node.left is None:
                current_node.left=PlayerBNode(player)
            else:
                self._insert_recursive(current_node.left,player)
        elif player.name > current_node.player.name:
            if  current_node.right is None:
                current_node.right=PlayerBNode(player)
            else:
                self._insert_recursive(current_node.right,player)
        else:
            current_node.player=player #update duplicate player

    def search(self,name):# use name as the key for searching
        return self._search_recursive(self._root,name)

    def _search_recursive(self,current_node,name):
        if current_node is None:#empty tree
            return None
        if name==current_node.player.name:# found the node and return
            return current_node
        elif name<current_node.player.name:
            return self._search_recursive(current_node.left,name)
        else:
             return self._search_recursive(current_node.right,name)


    def to_sorted_list(self): #create a sorted list
        list=[]
        self._inorder_traversal(self.root,list)
        return list
    def _inorder_traversal(self,node,list):
        if node:
            self._inorder_traversal(node.left,list)
            list.append(node.player)
            self._inorder_traversal(node.right,list)
    def balance(self):# new binary tree will be balanced since we got the middle node as root
        sorted_players=self.to_sorted_list()# new sorted list
        self._root=self._build_balanced_bst(sorted_players)# set the middle node as root

    def _build_balanced_bst(self, players):
        if not players:
            return None

        mid = len(players) // 2
        node = PlayerBNode(players[mid])
        node.left = self._build_balanced_bst(players[:mid])#left children of the root
        node.right = self._build_balanced_bst(players[mid + 1:])#right children of the root
        return node



