import os
import logging
from desk import Desk
from house import House
from player import Player
from enum import Enum
import core as c


def main():
    player = Player()
    desk = Desk()
    house = House()
    while(True):
        c.ClearConsole()
        option:str = c.HomeFlow(player)
        if option == c.Options.EXIT.value:
            # Exit Game
            print("Game Closed! Goodbye!")
            break
        elif option == c.Options.START.value:
            if c.StartNewGame(player,house,desk) == c.Options.STOP.value:
                break



if __name__ == "__main__":
    main()