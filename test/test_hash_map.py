import unittest
from app.hash_map import PlayerHashMap
from app.player_list import PlayerList
from app.Player import Player

class TestPlayerHashMap(unittest.TestCase):

    def setUp(self):
        self.hash_map=PlayerHashMap()


    def test_set_and_get_player(self): #test inserting and retrieving a player

        self.hash_map.__setitem__("123","Amy")
        self.hash_map.__setitem__("456","Kathy")

        player=self.hash_map.__getitem__("123")
        self.assertIsNotNone(player)
        self.assertEqual(player.name,"Amy")

        player = self.hash_map.__getitem__("456")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Kathy")

    def test_get_non_existent_player(self): #test retrieving a player does not exist

        retrieved_player = self.hash_map.__getitem__("111")
        self.assertIsNone(retrieved_player)

    def test_update_existing_player(self): #test updating an existing player's name

        self.hash_map.__setitem__("123", "Amy")
        self.hash_map.__setitem__("123", "Amiee")

        updated_player = self.hash_map.__getitem__("123")
        self.assertEqual(updated_player.name, "Amiee")

    def test_length(self):  #test the length of the hash map

        self.assertEqual(self.hash_map.__len__(), 0)
        self.hash_map.__setitem__("123", "Amy")
        self.assertEqual(self.hash_map.__len__(), 1)
        self.hash_map.__setitem__("456", "Kathy")
        self.assertEqual(self.hash_map.__len__(), 2)

    def test_delete_player(self):  #test removing a player

        self.hash_map.__setitem__("123", "Amy")
        self.hash_map.__delitem__("123", "Amy")

        player = self.hash_map.__getitem__("123")
        self.assertIsNone(player)

def test_display(self): #test the display function

        self.hash_map.__setitem__("123", "Amy")
        self.hash_map.__setitem__("456", "Kathy")
        self.hash_map.display()


if __name__ == "__main__":
    unittest.main()
