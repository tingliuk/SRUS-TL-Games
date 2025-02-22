import unittest
from app.Player import Player

class TestPlayer(unittest.TestCase):
    def test_uid_property(self):
        player = Player("001","Amy Liu")
        self.assertEqual(player.uid,"001")

    def test_name_property(self):
        player = Player("002","Kathy Liu")
        self.assertEqual(player.name,"Kathy Liu")

if __name__ == "__main__":
    unittest.main()


