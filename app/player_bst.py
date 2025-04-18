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
