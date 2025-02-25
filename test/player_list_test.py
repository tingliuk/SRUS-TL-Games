
import unittest
from app.player_list import PlayerList
from app.PlayerNode import PlayerNode
from app.Player import Player


class TestPlayerList(unittest.TestCase):
    def setUp(self):
        self.player_list=PlayerList()

    def test_insert_head_node_on_empty_list(self):
        player=Player("001","Amy Liu")
        self.player_list.insert_head_node(player)
        self.assertFalse(self.player_list.is_empty())
        self.assertEqual(self.player_list.get_head().player,player)

    def test_insert_head_node_on_non_empty_list(self):
        player1 = Player("001", "Amy Liu")
        player2 = Player("002", "Kathy Liu")

        self.player_list.insert_head_node(player1)
        self.player_list.insert_head_node(player2)
        self.assertEqual(self.player_list.get_head().player, player2)

    def test_insert_tail_node_on_empty_list(self):
        player = Player("001", "Amy Liu")
        self.player_list.insert_tail_node(player)
        self.assertFalse(self.player_list.is_empty())
        self.assertEqual(self.player_list.get_tail().player, player)

    def test_insert_tail_node_on_non_empty_list(self):
        player1 = Player("001", "Amy Liu")
        player2 = Player("002", "Kathy Liu")

        self.player_list.insert_tail_node(player1)
        self.player_list.insert_tail_node(player2)
        self.assertEqual(self.player_list.get_tail().player, player2)

    def test_delete_head_node_on_empty_list(self):
        self.player_list.delete_head_node()
        self.assertTrue(self.player_list.is_empty())

    def test_delete_head_node_on_non_empty_list(self):
        self.player_list.insert_head_node(self.player1)
        self.player_list.insert_head_node(self.player2)
        self.player_list.delete_head_node()
        self.assertEqual(self.player_list.get_head().player, self.player1)

    def test_delete_tail_node_on_empty_list(self):
        """Test deleting the tail node from an empty list."""
        self.player_list.delete_tail_node()
        self.assertTrue(self.player_list.is_empty())

    def test_delete_tail_node_on_non_empty_list(self):
        """Test deleting the tail node from a non-empty list."""
        self.player_list.insert_head_node(self.player1)
        self.player_list.insert_tail_node(self.player2)
        self.player_list.delete_tail_node()
        self.assertEqual(self.player_list.get_head().player, self.player1)
        self.assertIsNone(self.player_list.get_head().next)


if __name__ == "__main__":
    unittest.main()