import unittest
from app.hash_map import PlayerHashMap
from app.player_list import PlayerList
from app.Player import Player

class TestPlayerHashMap(unittest.TestCase):

    def setUp(self):
        self.hash_map=PlayerHashMap()



    def test_put_and_get(self):
        """Test inserting and retrieving a player."""
        player = Player("001", "Amy Liu")
        self.hash_map.put(player.uid, player)

        # Check if the player is stored correctly
        retrieved_player = self.hash_map.get("001")
        self.assertEqual(retrieved_player, player)

    def test_get_non_existent_key(self):
        """Test retrieving a player that does not exist."""
        retrieved_player = self.hash_map.get("999")  # Non-existent key
        self.assertIsNone(retrieved_player)

    def test_update_existing_player(self):
        """Test updating an existing player's name."""
        player = Player("001", "Amy Liu")
        self.hash_map.put(player.uid, player)

        updated_player = Player("001", "Kathy Liu")
        self.hash_map.put(updated_player.uid, updated_player)

        # Ensure the player's name is updated
        retrieved_player = self.hash_map.get("001")
        self.assertEqual(retrieved_player.name, "Kathy Liu")

    def test_remove_existing_player(self):
        """Test removing a player."""
        player = Player("002", "John Doe")
        self.hash_map.put(player.uid, player)

        # Ensure the player exists before removal
        self.assertEqual(self.hash_map.get("002"), player)

        # Remove the player
        self.hash_map.remove("002")

        # Ensure the player is removed
        self.assertIsNone(self.hash_map.get("002"))

    def test_remove_non_existent_player(self):
        """Test removing a player that doesn’t exist."""
        self.hash_map.remove("999")  # Should not raise an error
        self.assertIsNone(self.hash_map.get("999"))

    def test_size(self):
        """Test the size of the hash map."""
        self.assertEqual(self.hash_map.size(), 0)  # Initially empty

        player1 = Player("003", "Alice Smith")
        player2 = Player("004", "Bob Brown")

        self.hash_map.put(player1.uid, player1)
        self.hash_map.put(player2.uid, player2)

        self.assertEqual(self.hash_map.size(), 2)  # Two players added

        self.hash_map.remove("003")
        self.assertEqual(self.hash_map.size(), 1)  # One player removed

    def test_display(self):
        """Test the display function (print output)."""
        player1 = Player("005", "Eve Black")
        player2 = Player("006", "Charlie Green")

        self.hash_map.put(player1.uid, player1)
        self.hash_map.put(player2.uid, player2)

        # Manually inspect console output to verify correctness
        self.hash_map.display()


if __name__ == "__main__":
    unittest.main()
