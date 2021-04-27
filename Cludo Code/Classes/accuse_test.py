import accuse
import Deck
import Player

d = Deck.Deck()
d.init()
d.initEnvelope()
d.shuffle()

player1 = Player.Player("abby", 1)
a = accuse.Accuse
b = a(player1, d.getEnvelope())
b.displayScreen()
#accuse.Accuse.displayScreen(accuse, player1, d.getEnvelope())

