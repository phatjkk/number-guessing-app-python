# number-guessing-app-python

Clone project and python main.py to run.

Set isHack = True to enable game cheat.

Image Demo:

![image](https://github.com/phatjkk/number-guessing-app-python/assets/48487157/d1aa4d53-cd70-46ef-8516-3a83fbca5226)

![image](https://github.com/phatjkk/number-guessing-app-python/assets/48487157/b65954ce-28c2-4a6e-a475-88f315b726ff)

Details:

Make a "Number Guessing App":
 - There are 02 roles: Player, and House(PC)
 - There is a deck, contains 52 playing cards. There are:
   + 4 Suites: Heart, Diamond, Club, Spade
   + 13 groups: A(Ace), 2, 3, 4, 5, 6, 7, 8, 9, 10, J(Jack), Q(Queen), K(King)
   + 02 greatest cards: Black Joker, Red Joker
 - Each round, the Player and the House receive 01 card from the deck.
 - Player has to guess that his card is greater or less than the House's card.
 - Player starts with 60 points.
 - Reward for each winning round is 20 points.
 - Player must pay 25 points to join a single match
 - Game stages:
    + The House receives and shows his card first.
    + Player start guessing.
    + If the Player loses the round, he'll lose the reward.
    + If the Player wins the round, he can decide to continue or stop.
    + If the Player decides to stop, he can keep his current reward.
    + If the Player decides to continue, He does not receive the reward yet. But the reward will be doubled on the next round.
 - Game Win/Lose conditions:
    + Player will WIN the game if he has greater than or equal to 1000 points after any match.
    + Player will LOSE the game if he has less than 30 points after any match.


Auhor: Nguyen Thanh Phat - aka phatjk
