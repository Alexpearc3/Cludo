import Deck as deck


class Player:
    cards = []
    pId = "player ID"
    name = "player name"
    position = "doggy"
    hasAccused = False

    def __init__(self):
        do = "what a player do"

    def drawCard(self):
        draw = deck.drawCard()
        if not draw:
            return draw
        else:
            self.cards.append()
        return True
