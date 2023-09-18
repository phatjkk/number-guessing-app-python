from desk import Desk
import unittest
class TestDesk(unittest.TestCase):
    def test_CompareTwoCards(self):
        d = Desk()
        self.assertEqual(d.CompareTwoCards("2_Spade","2_Club"),"A<B")
        self.assertEqual(d.CompareTwoCards("A_Heart","2_Club"),"A>B")

    def test_GetRandomTwoCards(self):
         d = Desk()
         cardA, cardB = d.GetRandomTwoCards()
         self.assertTrue(cardA[0] != cardB[0])
if __name__ == '__main__':
    unittest.main(verbosity=2)


# Run with pytest
# def test_CompareTwoCards():
#     d = Desk()
#     assert d.CompareTwoCards("2_Spade","2_Club") == "A<B"
#     assert d.CompareTwoCards("A_Heart","2_Club") == "A>B"

# def test_GetRandomTwoCards():
#      d = Desk()
#      cardA, cardB = d.GetRandomTwoCards()
#      assert cardA[0] != cardB[0]