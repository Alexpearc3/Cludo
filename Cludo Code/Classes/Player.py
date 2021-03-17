import Deck as deck


class Player:
    cards = []

    def __init__(self):
        do = "what a player do"

    def drawCard(self):
        draw = deck.drawCard()
        if not draw:
            return draw
        else:
            self.cards.append()
        return True
