import random

class Desk():
    def __init__(self):
        self.cardsStructure = {
        "groups": [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"],
        "suites": ["Spade","Club","Diamond","Heart"],
        # "highestCards":["Black Joker", "Red Joker"]
        }
        self.cards = dict()
        counter:str = 1
        for group in self.cardsStructure["groups"]:
            for suite in self.cardsStructure["suites"]:
                self.cards[str(group)+"_"+suite] = counter
                counter +=1
        # Add 2 joker cards
        # self.cards["Black Joker"] = 53
        # self.cards["Red Joker"] = 54

    def getKey(self,dct:dict,value:str):
        return [key for key in dct if (dct[key] == value)]

    def GetRandomTwoCards(self):
        numbers:list = list(range(1,53))
        random.shuffle(numbers)
        
        playerCard:str = self.getKey(self.cards,numbers.pop())
        houseCard:str = self.getKey(self.cards,numbers.pop())
        return (playerCard[0],houseCard[0])

    def CompareTwoCards(self,cardA:str,cardB:str):
        if self.cards[cardA] > self.cards[cardB]:
            return "A>B"
        else:
            return "A<B"

    def PrintAllCards(self):
        print(self.cards)
