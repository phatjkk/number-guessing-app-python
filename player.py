from config import Settings
class Player():
    def __init__(self):
        self._points:int = Settings.PLAYER_START_POINTS.value
        self._card:str = ""
    @property
    def card(self):
        return self._card
    @card.setter
    def card(self,card:str):
        self._card = card
    @property
    def points(self):
        return self._points
    @points.setter
    def points(self,points:int):
        self._points = points
