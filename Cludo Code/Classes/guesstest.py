import pygame as pg
import guess
import Deck
import Player
import board

d = Deck.Deck()
d.init()
d.initEnvelope()
d.shuffle()

plys = ["player6", "player5", "player4", "player3", "player2", "player1"]

bo = board.board(plys, 1)
currentPlayer = bo.getCurrentPlayer()
notepad = currentPlayer.getNotepad()

guess.Guess.screenDisplay(guess, plys)
