from enum import Enum

class Settings(Enum):
    isHack = True
    PLAYER_START_POINTS = 60
    POINTS_PAY_FOR_FIRST_ROUND = 25
    REWARD_POINTS_FOR_FIRST_ROUND = 20
    POINTS_TO_START = 30
    WINNER_POINTS = 1000

class Options(Enum):
    START = CONTINUES = "1"
    STOP = "2"
    EXIT = "0"
    PLAYER_CARD_BIGGER = "1"
    PLAYER_CARD_SMALLER = "2"
