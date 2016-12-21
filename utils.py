from sets import Set
from card import Card 
from hand import Hand 
from pot import Pot 
import itertools
def findsubsets(S,m):
    return set(itertools.combinations(S, m))

class Utils(object):

    def __init__(self, info):
        self.info = info 

    @staticmethod
    def getAllCombi(hand, pot):
        for card in hand.cards:
            print card 
        for card in pot.cards:
            print card 



if __name__ == "__main__":
    my_pot = Pot(set([Card("A", "C"),Card("2", "C"),Card("2", "S"), Card("K", "S")]))
    my_hand = Hand(set([Card("3", "C"), Card("K", "H")]))



    Utils.getAllCombi(my_hand, my_pot) 
