import unittest
from blackJack import Game


def getOutcome(player, dealer):
    game = Game()
    result = game.calculateResult(player, dealer)
    return result

def test_round(player, dealer, playerDeck = [], dealerDeck = []):
    game = Game(player, dealer, playerDeck, dealerDeck)
    result = game.run()
    return result


class OutcomesTest(unittest.TestCase):
    # def test_Stand2(self):
    #     player = ['S-10', 'H-7']
    #     dealer = ['D-K', 'C-7']
    #     self.assertEqual(test_round(player, dealer), 0)

    # def test_Hit(self):
    #     player = ['S-5', 'H-3']
    #     dealer = ['D-K', 'C-8']
    #     playerDeck = ['D-9']
    #     self.assertEqual(test_round(player, dealer, playerDeck), -10)

    # def test_Split1(self):
    #     player = ['S-6', 'D-6']
    #     dealer = ['H-6', 'D-9']
    #     playerDeck = ['D-7', 'S-9']
    #     dealerDeck = ['D-3']
    #     self.assertEqual(test_round(player, dealer, playerDeck, dealerDeck), -20)

    # def test_Split0(self):
    #     player = ['S-8', 'H-8']
    #     dealer = ['H-10', 'C-7']
    #     playerDeck = ['H-4', 'C-4', 'H-5', 'S-5']
    #     self.assertEqual(test_round(player, dealer, playerDeck), 0)

    def test_Split2(self):
        player = ['S-8', 'H-8']
        dealer = ['H-10', 'C-7']
        playerDeck = ['H-4', 'C-4', 'H-3', 'S-7', 'C-6', 'S-5']
        self.assertEqual(test_round(player, dealer, playerDeck), 0)

    # def test_Split_BJ(self):
    #     player = ['S-8', 'H-8']
    #     dealer = ['H-10', 'C-7']
    #     playerDeck = ['H-4', 'C-4', 'H-3', 'S-6', 'C-6', 'S-5']
    #     self.assertEqual(test_round(player, dealer, playerDeck), 25)

    # def test_Double(self):
    #     player = ['H-6', 'H-5']
    #     dealer = ['S-5', 'D-3']
    #     playerDeck = ['D-K']
    #     dealerDeck = ['S-4', 'D-5']
    #     self.assertEqual(test_round(player, dealer, playerDeck, dealerDeck), 15)


if __name__ == '__main__':
    unittest.main()
