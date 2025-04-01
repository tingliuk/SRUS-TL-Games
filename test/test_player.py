import unittest
from player import Player
import random

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
        sorted_players = Player.sort_quickly(players)
        manually_sorted_players = [Player("Bob", uid='02', score=5),Player("Alice", uid='01', score=10),
            Player("Charlie", uid='03', score=15)]
        self.assertListEqual(sorted_players, manually_sorted_players)

    def test_class_sort_descending(self):
        players = [Player("Alice", uid='01', score=10), Player("Bob", uid='02', score=5),
                   Player("Charlie", uid='03', score=15)]
        sorted_players = Player.sort_descending(players)
        manually_sorted_players = [Player("Charlie", uid='03', score=15),Player("Alice", uid='01', score=10),
                                   Player("Bob", uid='02', score=5)]
        self.assertListEqual(sorted_players, manually_sorted_players)

    def test_sort_descending_random(self):
        players = [Player(f"Player {i}", uid=f"{i:03}", score=random.randint(0, 1000)) for i in range(1000)]
        sorted_players = Player.sort_descending(players)
        expected_order = sorted(players, key=lambda p: p.score, reverse=True)
        self.assertEqual(sorted_players, expected_order)

    def test_sort_descending_random_already_sorted_list(self):

        players = [Player(f"Player {i}", uid=f"{i:03}", score=i) for i in range(1000)] # Create 1000 players with scores in ascending order (already sorted)
        sorted_players = Player.sort_descending(players)
        expected_order = sorted(players, key=lambda p: p.score, reverse=True)  # players sorted in descending order of score
        self.assertEqual(sorted_players, expected_order)# Assert that the sorted_players list matches the expected_order

        if __name__ == '__main__':
            unittest.main()