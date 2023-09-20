import main
from desk import Desk
from player import Player
from house import House
import unittest
class TestMain(unittest.TestCase):
    def test_PlayerWinRound(self):
        d = Desk()
        h = House()
        p = Player()
        p.card,h.card = "3_Spade","A_Heart"
        isPlayerWinRound = main.RoundFlow(house=h,player=p,desk=d,roundNum=1,testValue="2")
        self.assertTrue(isPlayerWinRound)

    def test_PlayerLoseRound(self):
        d = Desk()
        h = House()
        p = Player()
        p.card,h.card = "3_Spade","A_Heart"
        isPlayerWinRound = main.RoundFlow(house=h,player=p,desk=d,roundNum=1,testValue="1")
        self.assertFalse(isPlayerWinRound)

if __name__ == '__main__':
    unittest.main(verbosity=2)