import numpy as np
import pygame as py
import copy

class tile():
    def __init__(self, room = "blank", door = False, isTile = False, selected = False, hover = False, blank = False , player = 0, possibleMove=False):
        self.room = room            # name of room, default is blank
        self.door = door            # is it a door? (bool)
        self.isTile = isTile        # is this a walkway (tile) (bool)
        self.selected = selected    # if tile selected (bool)
        self.hover = hover          # is mouse over (bool)
        self.blank = blank          # is tile not part of playable board (bool)
        self.player = player        # player number 1-6, 0 = no player
        self.possibleMove = possibleMove



    def getRoom(self):
        return self.room

    def getDoor(self):
        return self.door

    def getIsTile(self):
        return self.isTile

    def getSelected(self):
        return self.selected

    def getHover(self):
        return self.hover

    def getBlank(self):
        return self.blank

    def getPlayer(self):
        return self.player

    def setSelected(self, boolean):
        self.selected = boolean

    def getPossibleMove(self):
        return self.possibleMove

    def setPossibleMove(self, possibleMove):
        self.possibleMove = possibleMove

    def setPlayer(self,i):
        self.player = i

    
#sorry tom i moved it, it did not belong here ;)