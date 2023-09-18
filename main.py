import os
from desk import Desk
from house import House
from player import Player

isHack = False

def ClearConsole():
    os.system('cls')
def PauseConsole():
    os.system('pause')

def HomePage(player:Player):
    print("---------------------------------")
    print("Number Guessing App")
    print("Your points now:",player.points)
    print("---------------------------------")
    print("Select your choice:")
    print("1. Start Game")
    print("0. Exit")
    option:str = input("Your select:")
    return option

def RoundPage(roundNum:int,player:Player,house:House):
    print("Game Started! Round",roundNum)
    print("---------------------------------")
    print("Your points:",player.points)
    print("Paid for this match: 25 points")
    print("Reward for this round:",house.reward,"points")
    print("The reward will be doubled on the next round.")
    print("---------------------------------")
    print("House Card:",house.card)
    if isHack ==True:
        print("Your Card:",player.card)
    else:
        print("Your Card: Hidden")
    print("---------------------------------")
    print("You have 2 option to guess:")
    print("1. My card is greater than the House's card")
    print("2. My card is less than the House's card")
    playerGuess:str = input("Type your guess:")
    return playerGuess

def WinRoundPage(house:House):
    print("Congratulation! You win this round!")
    print("---------------------------------")
    print("Reward for next round is :",house.reward,"points")
    print("Do you want to continues?")
    print("1. Yes")
    print("2. No, back to home!")
    playerOption:str = input("Type your choice:")
    return playerOption

if __name__ == "__main__":
    player = Player()
    while(True):
        ClearConsole()
        option:str = HomePage(player)

        if option == "0":
            # Exit Game
            print("Game Closed! Goodbye!")
            break
        elif option == "1":
            # Start Game
            if player.points < 30:
                # Check enough points to start?
                print("You need at least 30 point to start!")
                print("Restarting the game to reset points!")
                print("Game Closed! Goodbye!")
                break

            desk = Desk()
            house = House()
            roundNum = 1
            player.points -= 25

            while(True):
                # Get 2 cards for Player and House
                houseCard, playerCard = desk.GetRandomTwoCards()
                player.card = playerCard[0]
                house.card = houseCard[0]
                isPlayerWinRound:bool = False

                while(True):
                    ClearConsole()
                    playerGuess:str = RoundPage(roundNum,player,house)
                    if playerGuess == "1":
                        # Player's Card > House's Card
                        if(desk.CompareTwoCards(player.card,house.card) == "A>B"):
                            isPlayerWinRound = True
                        break
                    elif playerGuess == "2":
                        # Player's Card < House's Card
                        if(desk.CompareTwoCards(player.card,house.card) == "A<B"):
                            isPlayerWinRound = True
                        break

                ClearConsole()
                print("---------------------------------")
                print("Your card is:",player.card)
                print("Your points now:",player.points)

                roundNum +=1

                if isPlayerWinRound == True:
                    # Player WIN
                    house.reward *= 2
                    playerOptionToStopOrContinues:str = WinRoundPage(house)
                    if playerOptionToStopOrContinues != "1":
                        # Player want to stop!
                        player.points += house.reward
                        # Check is WINNER?
                        if(player.points>=1000):
                            print("Congratulation! YOU ARE THE CHAMPIONS!")
                            print("CHAMPIONS points is greater than or equal to 1000 points")
                            PauseConsole()
                        break
                else:
                    # Player LOSE
                    print("Oh no! You lose this round :(")
                    print("You lost your reward and will go back to home")
                    PauseConsole()
                    break

