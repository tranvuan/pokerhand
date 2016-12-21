from sets import Set
from card import Card


class Hand(object):

    def __init__(self, cards):
        self.cards = cards 

    def showHand(self):
        for card in self.cards:
            print card 

    def __str__(self):
        str1 = "== Hand ==\n"
        for card in self.cards:
            str1 += card.__str__() + "\n"
        str1 += "== end =="
        return str1

if __name__ == "__main__":
    happy_bday = Hand(set([Card("2S"), Card("KS")]))

    print happy_bday

