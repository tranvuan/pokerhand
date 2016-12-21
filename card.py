class Card(object):

    def __init__(self, value):
        self.value = value 

    def showCard(self):
        print "{}".format(self.value) 

    def __str__(self):
        return "{}".format(self.value)


if __name__ == "__main__":
    happy_bday = Card("2S")

    bulls_on_parade = Card("KH")

    happy_bday.showCard()

    bulls_on_parade.showCard()


