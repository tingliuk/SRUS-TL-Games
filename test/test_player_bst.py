import unittest
from player_bst import PlayerBST
from player_bnode import PlayerBNode
from player import Player
class TestPlayerBST(unittest.TestCase):
    def setUp(self):
        self.tree=PlayerBST()
        self.p1=Player("Bob",101,10)
        self.p2=Player("Kathy",102,20)
        self.p3 = Player("Amy",102,20)
        self.p4 = Player("Bob",101,20) # duplicate player

    def test_insert_single_node(self):
        self.tree.insert(self.p1)
        self.assertEqual(self.tree.root.player.name,"Bob")

    def test_insert_multiple_nodes(self):
        self.tree.insert(self.p1)
        self.tree.insert(self.p2)
        self.tree.insert(self.p3)
        root=self.tree.root
        self.assertEqual(root.player.name,"Bob")# set Bob as root
        self.assertEqual(root.left.player.name,"Amy")# left child less than root
        self.assertEqual(root.right.player.name, "Kathy")# right child greater than root

    def test_insert_duplicate_player(self):

        self.tree.insert(self.p1)
        self.tree.insert(self.p4)# inserted a duplicate player
        root=self.tree.root
        self.assertEqual(root.player.score, 20)# check if root has been updated to new score

    def test_search_existing_player(self):
        self.tree.insert(self.p1) #insert player "Bob"
        self.tree.insert(self.p2)
        self.tree.insert(self.p3)
        node=self.tree.search("Bob")
        assert node is not None
        assert node.player.name=="Bob"

    def test_search_non_existing_player(self):
        self.tree.insert(self.p1)
        self.tree.insert(self.p2)
        node=self.tree.search("Amy")# search a player doesn't exist
        assert node is None



