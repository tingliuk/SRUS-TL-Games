import unittest
from Player import Player


class TestPlayer(unittest.TestCase):
    def test_sort_players(self):
        players = [Player("Alice", uid='01', score=10), Player("Bob", uid='02', score=5),
                   Player("Charlie", uid='03', score=15)]
        # note: ensure initialization code is valid for **your** implementation

        # do **not** change the following code:
        sorted_players = sorted(players)
        manually_sorted_players = [Player("Bob", uid='02', score=5), Player("Alice", uid='01', score=10),
                                   Player("Charlie", uid='03', score=15)]

        self.assertListEqual(sorted_players, manually_sorted_players)

    def test_players_can_be_compared_by_score(self):
        # note: ensure initialization code is valid for **your** implementation
        alice = Player("Alice", uid='01', score=10)
        bob = Player("Bob", uid='02', score=5)

        # Add the appropriate expression to the following assert test
        self.assertTrue(bob < alice)

    def test_sort_quickly(self):
        players = [Player("Alice", uid='01', score=10), Player("Bob", uid='02', score=5),
                   Player("Charlie", uid='03', score=15)]
        sorted_players = Player.sort_quickly(players, )
        manually_sorted_players = []
