import unittest
from statistics_service import SortBy, StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class StatisticsServiceTest(unittest.TestCase):
    def setUp(self):
        self.service = StatisticsService(PlayerReaderStub())

    def test_search(self):
        player = self.service.search("Kurri")
        self.assertEqual(player.name, "Kurri")
        self.assertEqual(player.team, "EDM")
        self.assertEqual(player.goals, 37)
        self.assertEqual(player.assists, 53)

    def test_search_no_player(self):
        player = self.service.search("nonexistent")
        self.assertIsNone(player)

    def test_team(self):
        players = self.service.team("EDM")
        
        self.assertTrue(all(player.name in ["Semenko", "Kurri", "Gretzky" ] for player in players))

    def test_top(self):
        top = self.service.top(3)
        self.assertEqual(top[0].name, "Gretzky")
        self.assertEqual(top[1].name, "Lemieux")
        self.assertEqual(top[2].name, "Yzerman")

    def test_top_goals(self):
        top = self.service.top(1, sort_by=SortBy.GOALS)
        self.assertEqual(top[0].name, "Lemieux")

    def test_top_assists(self):
        top = self.service.top(1, sort_by=SortBy.ASSISTS)
        self.assertEqual(top[0].name, "Gretzky")
    
    def test_top_default_is_points(self):
        top = self.service.top(3)
        top_points = self.service.top(3, sort_by=SortBy.POINTS)
        
        for i in range(3):
            self.assertEqual(top[i].name, top_points[i].name)
    