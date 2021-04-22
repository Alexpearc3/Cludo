import numpy as np
import pygame as py
import copy

class tile():
    def __init__(self, room = "blank", door = False, isTile = False, selected = False, hover = False, blank = False , player = 0):
        self.room = room            # name of room, default is blank
        self.door = door            # is it a door? (bool)
        self.isTile = isTile        # is this a walkway (tile) (bool)
        self.selected = selected    # if tile selected (bool)
        self.hover = hover          # is mouse over (bool)
        self.blank = blank          # is tile not part of playable board (bool)
        self.player = player        # player number 1-6, 0 = no player



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
    
#sorry tom i moved it, it did not belong here ;)
    def drawGrid(self, board):
        for row in range(self.BOARDWIDTH):
            for column in range(self.BOARDHEIGHT):
                x, y = pygame.mouse.get_pos()
                x = x - self.GRIDBUFFX
                y = y - self.GRIDBUFFY

                if self.board[row, column].getPlayer() == 1:
                    self.screen.blit(self.tileImgP1,
                                     (column * self.WIDTH + self.GRIDBUFFX, self.HEIGHT * row + self.GRIDBUFFY))

                elif self.board[row, column].getPlayer() == 2:
                    self.screen.blit(self.tileImgP2,
                                     (column * self.WIDTH + self.GRIDBUFFX, self.HEIGHT * row + self.GRIDBUFFY))

                elif self.board[row, column].getPlayer() == 3:
                    self.screen.blit(self.tileImgP3,
                                     (column * self.WIDTH + self.GRIDBUFFX, self.HEIGHT * row + self.GRIDBUFFY))

                elif self.board[row, column].getPlayer() == 4:
                    self.screen.blit(self.tileImgP4,
                                     (column * self.WIDTH + self.GRIDBUFFX, self.HEIGHT * row + self.GRIDBUFFY))

                elif self.board[row, column].getPlayer() == 5:
                    self.screen.blit(self.tileImgP5,
                                     (column * self.WIDTH + self.GRIDBUFFX, self.HEIGHT * row + self.GRIDBUFFY))

                elif self.board[row, column].getPlayer() == 6:
                    self.screen.blit(self.tileImgP6,
                                     (column * self.WIDTH + self.GRIDBUFFX, self.HEIGHT * row + self.GRIDBUFFY))

                # selected tile
                elif self.board[row, column].getSelected() and self.board[row, column].getIsTile():
                    self.screen.blit(self.tileImgSELECT,
                                     (column * self.WIDTH + self.GRIDBUFFX, self.HEIGHT * row + self.GRIDBUFFY))

                # hover tile
                elif (np.ceil(x / self.WIDTH) == column + 1 and np.ceil(y / self.WIDTH) == row + 1 and self.board[
                    row, column].getIsTile()):
                    self.screen.blit(self.tileImgHover,
                                     (column * self.WIDTH + self.GRIDBUFFX, self.HEIGHT * row + self.GRIDBUFFY))

                # unselected tile
                elif self.board[row, column].getIsTile():
                    self.screen.blit(self.tileImg,
                                     (column * self.WIDTH + self.GRIDBUFFX, self.HEIGHT * row + self.GRIDBUFFY))
