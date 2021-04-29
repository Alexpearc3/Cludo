import accuse
import Deck
import Player
import board

d = Deck.Deck()
d.init()
plys = ["pl1","pl2","pl3","pl4","pl5","pl6"]
bo = board.board(plys, 1)
d.initEnvelope()
d.shuffle()
currentPlayer = bo.getCurrentPlayer()
notepad = currentPlayer.getNotepad()
player1 = Player.Player("abby", 1,  notepad)
a = accuse.Accuse
b = a(player1, d.getEnvelope())
b.displayScreen()
#accuse.Accuse.displayScreen(accuse, player1, d.getEnvelope())

