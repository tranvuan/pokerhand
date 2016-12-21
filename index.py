#!/usr/bin/python
import web
from utils import Utils
from sets import Set
from card import Card
from hand import Hand
from pot import Pot
import sys

import itertools

def findsubsets(S,m):
    return set(itertools.combinations(S, m))


def poker(hands):
    scores = [(i, score(hand.split())) for i, hand in enumerate(hands)]
    winner = sorted(scores , key=lambda x:x[1])[-1][0]

    return hands[winner]

def pokerrank(hands):
    scores = [(i, score(hand.split())) for i, hand in enumerate(hands)]
    winner = sorted(scores , key=lambda x:x[1])[-1][0]
    winners = sorted(scores , key=lambda x:x[1])
    indexes = [s[0] for s in winners]
    sorthand = []
    for ind in reversed(indexes):
        sorthand.append(hands[ind])

    return sorthand

def score(hand):
    ranks = '23456789TJQKA'
    rcounts = {ranks.find(r): ''.join(hand).count(r) for r, _ in hand}.items()
    score, ranks = zip(*sorted((cnt, rank) for rank, cnt in rcounts)[::-1])
    if len(score) == 5:
        if ranks[0:2] == (12, 3): #adjust if 5 high straight
            ranks = (3, 2, 1, 0, -1)
        straight = ranks[0] - ranks[4] == 4
        flush = len({suit for _, suit in hand}) == 1
        '''no pair, straight, flush, or straight flush'''
        score = ([1, (3,1,1,1)], [(3,1,1,2), (5,)])[flush][straight]
    return score, ranks

def allCardsExceptHand(pot, hand):
    allcards = set(["2C","3C", "4C", "5C", "6C",
                   "7C", "8C", "9C", "TC", "JC",
                   "QC", "KC", "AC",
                   "2D", "3D", "4D", "5D", "6D",
                   "7D", "8D", "9D", "TD", "JD",
                   "QD", "KD", "AD",
                   "2H", "3H", "4H", "5H", "6H",
                   "7H", "8H", "9H", "TH", "JH",
                   "QH", "KH", "AH",
                   "2S", "3S", "4S", "5S", "6S",
                   "7S", "8S", "9S", "TS", "JS",
                   "QS", "KS", "AS"])
    validcards = allcards - hand.cards - pot.cards
    allhands = findsubsets(validcards, 2)
    return allhands
    # allHandsSet = set()
    # for alist in allhands:
    #     if (hand.cards != set(alist)):
    #     #if (len(hand.cards.intersection(alist)) == 0):
    #         allHandsSet.add(alist)
    #
    # return allHandsSet


def getBestFromPotAndHand(pot, hand):
    cards = pot.cards.union(hand.cards)
    allsets = findsubsets(cards, 5)

    allhands = []
    for aset in allsets:
        cardstr = ""
        for card in aset:
            cardstr += card.__str__() + " "
        cardstr = cardstr[0:-1]
        allhands.append(cardstr)

    return poker(allhands)

def getBestFromPotAndHandList(pot, handlist):
    handset = set(handlist)
    if (len(pot.cards.intersection(handset)) == 0):
        cards = pot.cards.union(handset)
        allsets = findsubsets(cards, 5)

        allhands = []
        for aset in allsets:
            cardstr = ""
            for card in aset:
                cardstr += card.__str__() + " "
            cardstr = cardstr[0:-1]
            allhands.append(cardstr)

        besthand = poker(allhands)
        return besthand
        #print besthand
    else:
        return "2S 3C 7D 5C 6H"
        #print "invalid hand " + str(handlist)


render = web.template.render('templates/')
#db = web.database(dbn='mysql', user='antran', pw='12345678', db='webpy')

urls = (
  '/', 'index',
  '/calc', 'calc'
)

class index:
    def GET(self):
        #todos = db.select('todo')
        todos = []
        return render.index(todos)

class calc:
    def POST(self):
        i = web.input()
        #n = db.insert('todo', title=i.title)
        #raise web.seeother('/')
        potstr = i.pot
        handstr = i.hand
        my_pot = Pot(set(potstr.split()))
        my_hand = Hand(set(handstr.split()))

        # my_pot = Pot(set(["AC", "2C", "2S", "KS"]))
        # my_hand = Hand(set(["3C", "KH"]))
        allotherhand = allCardsExceptHand(my_pot, my_hand)
        mybesthand = getBestFromPotAndHand(my_pot, my_hand)

        results = [mybesthand]
        for alist in allotherhand:
            besthand = getBestFromPotAndHandList(my_pot, alist)
            results.append(besthand)


        sortResults = pokerrank(results)
        finalResults = []
        for ahand in sortResults:
            finalResults.append(ahand)
            if (set(ahand.split()) == set(mybesthand.split())):
                break

        return render.calc(finalResults)
        # counter = 0
        # for ahand in sortResults:
        #     counter += 1
        #     print ahand
        #     if (set(ahand.split()) == set(mybesthand.split())):
        #         break
        #
        # print counter

if __name__ == "__main__":
    app = web.application(urls, globals())
    web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
    app.run()
