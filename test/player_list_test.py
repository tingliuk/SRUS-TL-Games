
import unittest
from app.player_list import PlayerList
from app.PlayerNode import PlayerNode
from app.player import Player


class TestPlayerList(unittest.TestCase):
    # def __init__(self, methodName: str = "runTest"):
    #     super().__init__(methodName)
    #     self.player1 = None
    #     self.player2 = None

    def setUp(self):
        self.player_list=PlayerList()

    def test_insert_head_node_on_empty_list(self):
        player=Player("001","Amy Liu")
        self.player_list.insert_head_node(player)
        self.assertFalse(self.player_list.is_empty())
        self.assertEqual(self.player_list.head.player,player)

    def test_insert_head_node_on_non_empty_list(self):
        player1 = Player("001", "Amy Liu")
        player2 = Player("002", "Kathy Liu")

        self.player_list.insert_head_node(player1)
        self.player_list.insert_head_node(player2)
        self.assertEqual(self.player_list.head.player, player2)

    def test_insert_tail_node_on_empty_list(self):
        player = Player("001", "Amy Liu")
        self.player_list.insert_tail_node(player)
        self.assertFalse(self.player_list.is_empty())
        self.assertEqual(self.player_list.tail.player, player)

    def test_insert_tail_node_on_non_empty_list(self):
        player1 = Player("001", "Amy Liu")
        player2 = Player("002", "Kathy Liu")

        self.player_list.insert_tail_node(player1)
        self.player_list.insert_tail_node(player2)
        self.assertEqual(self.player_list.tail.player, player2)

    def test_delete_head_node_on_empty_list(self):
        self.player_list.delete_head_node()
        self.assertTrue(self.player_list.is_empty())

    def test_delete_head_node_on_non_empty_list(self):
        player1 = Player("001", "Amy Liu")
        player2 = Player("002", "Kathy Liu")
        self.player_list.insert_head_node(player1)
        self.player_list.insert_head_node(player2)
        self.player_list.delete_head_node()
        self.assertEqual(self.player_list.head.player, player1)

    def test_delete_tail_node_on_empty_list(self):
        self.player_list.delete_tail_node()
        self.assertTrue(self.player_list.is_empty())

    def test_delete_tail_node_on_non_empty_list(self):
        player1 = Player("001", "Amy Liu")
        player2 = Player("002", "Kathy Liu")
        self.player_list.insert_tail_node(player1)
        self.player_list.insert_tail_node(player2)
        self.player_list.delete_tail_node()
        self.assertEqual(self.player_list.tail.player, player1)
        self.assertIsNone(self.player_list.tail.next)

    def test_delete_node_by_key(self):
        player1 = Player("001", "Amy Liu")
        player2 = Player("002", "Kathy Liu")
        player3 = Player("003", "Ada Liu")

        self.player_list.insert_tail_node(player1)
        self.player_list.insert_tail_node(player2)
        self.player_list.insert_tail_node(player3)

        #delete node on head
        self.player_list.delete_node_by_key(player1)
        self.assertEqual(self.player_list.head.player,player2)
        # delete node on head
        self.player_list.delete_node_by_key(player3)
        self.assertEqual(self.player_list.tail.player, player2)
        # delete node in between head and tail
        self.player_list.delete_node_by_key(player2)
        self.assertIsNone(self.player_list.head)
        self.assertIsNone(self.player_list.tail)




if __name__ == "__main__":
    unittest.main()