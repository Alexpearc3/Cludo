class Player:

    def __init__(self, player_name, start_position, player_ID):
        do = "what a player do"
        self.cards = []
        self.name = player_name
        self.position = start_position
        self.pId = player_ID

    def setCard(self, card):
        self.cards.append(card)

    def getCards(self):
        return self.cards

    def setPosition(self, position):
        self.position = position

    def accuse(self):
        self.hasAccused = True

    def getName(self):
        return self.name
