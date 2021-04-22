class Player:

    def __init__(self, player_name, start_location, player_ID):
        do = "what a player do"
        self.cards = []
        self.name = player_name
        self.location = start_location #2d array value e.g. [0][0] can find room details from tile details
        self.pId = player_ID
        self.accusations = 1
        self.hasWon = False


    def setCard(self, card):
        self.cards.append(card)

    def getCards(self):
        return self.cards

    def setLocation(self, location):
        self.location = location

    def accuse(self):
        #check envelope
        self.accusations = self.accusations - 1

    def getName(self):
        return self.name

    def hasWon(self):
        return self.hasWon

    def setWin(self):
        self.hasWon = True

    def getLocation(self):
        return self.location

    def getPlayerID(self):
        return self.pId