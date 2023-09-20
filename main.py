import os
import logging
from desk import Desk
from house import House
from player import Player

isHack = False

POINTS_TO_START = 30
WINNER_POINTS = 1000

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
    if option != "0" and option !="1":
        raise ValueError("Input must be 0 or 1!")
    return option

def RoundPage(roundNum:int,player:Player,house:House,testValue = None):
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
    if testValue != None:
        playerGuess = testValue
    else:
        playerGuess:str = input("Type your guess:")
    if playerGuess != "1" and playerGuess !="2":
        raise ValueError("Input must be 1 or 2!")
    return playerGuess

def WinRoundPage(house:House):
    print("Congratulation! You win this round!")
    print("---------------------------------")
    print("Reward for next round is :",house.reward,"points")
    print("Do you want to continues?")
    print("1. Yes")
    print("2. No, back to home!")
    playerOption:str = input("Type your choice:")
    if playerOption != "1" and playerOption !="2":
        raise ValueError("Input must be 1 or 2!")
    return playerOption

def RoundFlow(roundNum:int,player:Player,house:House,desk:Desk,testValue:str = None):
    isPlayerWinRound:bool = False
    while(True):
        ClearConsole()
        # Check player input vailid
        playerGuess:str = None
        try:
            playerGuess = RoundPage(roundNum,player,house,testValue)
        except Exception as e:
            logging.warning(e) 
            PauseConsole()

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
    return isPlayerWinRound

def ShowResultFlow(isPlayerWinRound:bool,player:Player,house:House):
    ClearConsole()

    isPlayerWantToStop:bool = False

    if isPlayerWinRound == True:
        # Player WIN
        house.reward *= 2

        isPlayerWantToStop = WinRoundFlow(house,player)
        return isPlayerWantToStop
    else:
        print("---------------------------------")
        print("Your card is:",player.card)
        print("Your points now:",player.points)
        print("---------------------------------")
        # Player LOSE
        print("Oh no! You lose this round :(")
        print("You lost your reward and will go back to home")
        PauseConsole()
        isPlayerWantToStop = True
        return isPlayerWantToStop
    
def WinRoundFlow(house:House,player:Player):
    while(True):
        ClearConsole()
        print("---------------------------------")
        print("Your card is:",player.card)
        print("Your points now:",player.points)
        print("---------------------------------")
        playerOptionToStopOrContinues:str = None
        # Check player input vailid
        try:
            playerOptionToStopOrContinues = WinRoundPage(house)
        except Exception as e:
            logging.warning(e) 
            PauseConsole()

        if playerOptionToStopOrContinues == "2":
            # Player want to stop!
            player.points += house.reward
            # Check is WINNER?
            if(player.points>=WINNER_POINTS):
                print("Congratulation! YOU ARE THE CHAMPIONS!")
                print("CHAMPIONS points is greater than or equal to 1000 points")
                PauseConsole()
            isPlayerWantToStop = True
            return isPlayerWantToStop
        elif playerOptionToStopOrContinues == "1":
            # Player want to play next round!
            isPlayerWantToStop = False
            return isPlayerWantToStop

def CheckPlayerPoints(player:Player):
    isEnoughPoint:bool = True 
    if player.points < POINTS_TO_START:
        # Check enough points to start?
        print("You need at least 30 point to start!")
        print("Restarting the game to reset points!")
        print("Game Closed! Goodbye!")
        isEnoughPoint = False
    return isEnoughPoint



if __name__ == "__main__":
    player = Player()
    while(True):
        ClearConsole()

        # Check player input vailid
        option:str = None
        try:
            option = HomePage(player)
        except Exception as e:
            logging.warning(e) 
            PauseConsole()

        if option == "0":
            # Exit Game
            print("Game Closed! Goodbye!")
            break
        elif option == "1":
            # Start Game
            isEnoughPointToStart:bool = CheckPlayerPoints(player)
            if isEnoughPointToStart == False:
                break
            desk = Desk()
            house = House()
            roundNum = 1
            player.points -= 25

            while(True):
                # Get 2 cards for Player and House
                houseCard, playerCard = desk.GetRandomTwoCards()
                player.card, house.card = playerCard[0],houseCard[0]

                isPlayerWinRound:bool = RoundFlow(roundNum,player,house,desk)
                roundNum +=1

                isPlayerWantToStop = ShowResultFlow(isPlayerWinRound,player,house)
                if isPlayerWantToStop == True:
                    break
