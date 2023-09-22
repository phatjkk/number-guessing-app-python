from config import Settings
class House():
    def __init__(self):
        self._card:str = ""
        self._reward:int = Settings.REWARD_POINTS_FOR_FIRST_ROUND.value
    @property
    def card(self):
        return self._card
    @card.setter
    def card(self,card:str):
        self._card = card
    @property
    def reward(self):
        return self._reward
    @reward.setter
    def reward(self,reward:str):
        self._reward = reward