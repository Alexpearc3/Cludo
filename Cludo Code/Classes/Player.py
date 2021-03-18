import Deck as deck


class Player:
    cards = []
    pId = "player ID"
    name = "player name"
    position = "doggy"
    hasAccused = False

    def __init__(self):
        do = "what a player do"

    def setCard(self, card):
        self.cards.append(card)

