import numpy as np
import pygame as py
import copy


class tile():
    """
    A Class to be used as an instance to hold attributes and functions
    of tile
    """

    def __init__(self,
                 room="blank",
                 door=False,
                 isTile=False,
                 selected=False,
                 hover=False,
                 blank=False,
                 player=0,
                 possibleMove=False,
                 hiddenPassage=False):
        """
        init function for tile, here 9 parameters are passed through:

            Parameter:
                room (str)
                door (bool)
                isTile (bool)
                selected (bool)
                hover (bool)
                blank (bool)
                player (int)
                possibleMove (bool)
                hiddenPassage (int, bool)
        """

        self.room = room  # name of room, default is blank
        self.door = door  # is it a door? (bool)
        self.isTile = isTile  # is this a walkway (tile) (bool)
        self.selected = selected  # if tile selected (bool)
        self.hover = hover  # is mouse over (bool)
        self.blank = blank  # is tile not part of playable board (bool)
        self.player = player  # player number 1-6, 0 = no player
        self.possibleMove = possibleMove  # are there possible moves (bool)
        self.hiddenPassage = hiddenPassage  # is tile a hidden passage, if not, coordinates
        #   of linked passage

    def getRoom(self):
        """
        gets room

            Returns:
                room (str): name of room
        """
        return self.room

    def getDoor(self):
        """
        gets door

            Returns:
                door (bool): is it a door?
        """
        return self.door

    def getIsTile(self):
        """
        gets isTile

            Returns:
                isTile (bool): is this a tile? 
        """
        return self.isTile

    def getSelected(self):
        """
        gets selected

            Returns:
                selected (bool): is this tile selected
        """
        return self.selected

    def getHover(self):
        """
        gets hover

            Returns:
                hover (bool): is this tile hovering
        """
        return self.hover

    def getBlank(self):
        """
        gets blank

            Returns:
                blank (bool): is tile blank
        """
        return self.blank

    def getPlayer(self):
        """
        gets Player

            Returns:
                Player (int): if player is on tile, return number of player
        """
        return self.player

    def setSelected(self, boolean):
        """
        sets selected

            Parameter:
                boolean (bool): state of selected
        """
        self.selected = boolean

    def getPossibleMove(self):
        """
        gets possible moves

            Returns:
                possibleMove (bool): if possible move
        """
        return self.possibleMove

    def setPossibleMove(self, possibleMove):
        """
        sets possible moves

            Parameter:
                boolean (bool): state of selected
        """
        self.possibleMove = possibleMove

    def setPlayer(self, i):
        """
        sets player

            Parameter:
                i (int): sets current player
        """
        self.player = i

    def getHiddenPassage(self):
        """
        gets geHiddenPassage

            returns:
                hiddenPassage (bool): if hidden passage or coordinates
        """
        return self.hiddenPassage
