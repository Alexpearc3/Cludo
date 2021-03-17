import Deck as deck


class Player:
    cards = []

    def __init__(self):
        do = "what a player do"

    def drawCard(self):
        self.cards.append(deck.drawCard())
