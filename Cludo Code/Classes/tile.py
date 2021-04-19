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
    
    
    def initiateBoard(player1 = True, player2 = True, player3 = True, player4 = True, player5 = True, player6 = True):

        """
            there are 27 possible tile states.

            str = study (room)
            har = hall (room)
            lor = lounge (room)
            drr = dining room (room)
            kir = kitchen (room)
            brr = ball room (room)
            cvr = conservatory (room)
            bir = billiards room (room)
            lir = library (room)

            std = study (door)
            had = hall (door)
            lod = lounge (door)
            drd = dining room (door)
            kid = kitchen (door)
            brd = ball room (door)
            cvd = conservatory (door)
            bid = billiards room (door)
            lid = library (door)

            wwe = walkway empty
            wwh = walkway hover
            wws = walkway select
            
            blk = blank

            ww1 = walkway player 1
            ww2 = walkway player 2
            ww3 = walkway player 3
            ww4 = walkway player 4
            ww5 = walkway player 5
            ww6 = walkway player 6

            """

        grid = [["str", "str", "str", "str", "str", "str", "str", "wwe", "blk", "blk", "har", "har", "har", "har", "har", "blk", "wwe", "lor", "lor", "lor", "lor", "lor", "lor", "lor"],
                ["str", "str", "str", "str", "str", "str", "str", "wwe", "wwe", "har", "har", "har", "har", "har", "har", "wwe", "wwe", "lor", "lor", "lor", "lor", "lor", "lor", "lor"],
                ["str", "str", "str", "str", "str", "str", "str", "wwe", "wwe", "har", "har", "har", "har", "har", "har", "wwe", "wwe", "lor", "lor", "lor", "lor", "lor", "lor", "lor"],
                ["str", "str", "str", "str", "str", "str", "str", "wwe", "wwe", "har", "har", "har", "har", "har", "har", "wwe", "wwe", "lor", "lor", "lor", "lor", "lor", "lor", "lor"],
                ["blk", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "har", "har", "har", "har", "har", "har", "wwe", "wwe", "lor", "lor", "lor", "lor", "lor", "lor", "lor"],
                ["wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "har", "har", "har", "har", "har", "har", "wwe", "wwe", "lor", "lor", "lor", "lor", "lor", "lor", "lor"],
                ["blk", "lir", "lir", "lir", "lir", "lir", "wwe", "wwe", "wwe", "har", "har", "har", "har", "har", "har", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "blk"],
                ["lir", "lir", "lir", "lir", "lir", "lir", "lir", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe"],
                ["lir", "lir", "lir", "lir", "lir", "lir", "lir", "wwe", "wwe", "blk", "blk", "blk", "blk", "blk", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "blk"],
                ["lir", "lir", "lir", "lir", "lir", "lir", "lir", "wwe", "wwe", "blk", "blk", "blk", "blk", "blk", "wwe", "wwe", "drr", "drr", "drr", "drr", "drr", "drr", "drr", "drr"],
                ["blk", "lir", "lir", "lir", "lir", "lir", "wwe", "wwe", "wwe", "blk", "blk", "blk", "blk", "blk", "wwe", "wwe", "drr", "drr", "drr", "drr", "drr", "drr", "drr", "drr"],
                ["blk", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "blk", "blk", "blk", "blk", "blk", "wwe", "wwe", "drr", "drr", "drr", "drr", "drr", "drr", "drr", "drr"],
                ["bir", "bir", "bir", "bir", "bir", "bir", "wwe", "wwe", "wwe", "blk", "blk", "blk", "blk", "blk", "wwe", "wwe", "drr", "drr", "drr", "drr", "drr", "drr", "drr", "drr"],
                ["bir", "bir", "bir", "bir", "bir", "bir", "wwe", "wwe", "wwe", "blk", "blk", "blk", "blk", "blk", "wwe", "wwe", "drr", "drr", "drr", "drr", "drr", "drr", "drr", "drr"],
                ["bir", "bir", "bir", "bir", "bir", "bir", "wwe", "wwe", "wwe", "blk", "blk", "blk", "blk", "blk", "wwe", "wwe", "drr", "drr", "drr", "drr", "drr", "drr", "drr", "drr"],
                ["bir", "bir", "bir", "bir", "bir", "bir", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "drr", "drr", "drr", "drr", "drr"],
                ["bir", "bir", "bir", "bir", "bir", "bir", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "blk"],
                ["blk", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "brr", "brr", "brr", "brr", "brr", "brr", "brr", "brr", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe"],
                ["wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "brr", "brr", "brr", "brr", "brr", "brr", "brr", "brr", "wwe", "wwe", "kid", "kid", "kid", "kid", "kid", "brr"],
                ["blk", "cvr", "cvr", "cvr", "cvr", "wwe", "wwe", "wwe", "brr", "brr", "brr", "brr", "brr", "brr", "brr", "brr", "wwe", "wwe", "kid", "kid", "kid", "kid", "kid", "kid"],
                ["cvr", "cvr", "cvr", "cvr", "cvr", "cvr", "wwe", "wwe", "brr", "brr", "brr", "brr", "brr", "brr", "brr", "brr", "wwe", "wwe", "kid", "kid", "kid", "kid", "kid", "kid"],
                ["cvr", "cvr", "cvr", "cvr", "cvr", "cvr", "wwe", "wwe", "brr", "brr", "brr", "brr", "brr", "brr", "brr", "brr", "wwe", "wwe", "kid", "kid", "kid", "kid", "kid", "kid"],
                ["cvr", "cvr", "cvr", "cvr", "cvr", "cvr", "wwe", "wwe", "brr", "brr", "brr", "brr", "brr", "brr", "brr", "brr", "wwe", "wwe", "kid", "kid", "kid", "kid", "kid", "kid"],
                ["cvr", "cvr", "cvr", "cvr", "cvr", "cvr", "blk", "wwe", "wwe", "wwe", "brr", "brr", "brr", "brr", "wwe", "wwe", "wwe", "brr", "kid", "kid", "kid", "kid", "kid", "kid"],
                ["blk", "blk", "blk", "blk", "blk", "blk", "blk", "blk", "blk", "wwe", "blk", "blk", "blk", "blk", "wwe", "brr", "brr", "brr", "kid", "kid", "kid", "kid", "kid", "kid"]]

        if player1 == True:
            grid[0][16] = "ww1"
            
        if player2 == True:
            grid[7][23] = "ww2"
            
        if player3 == True:
            grid[24][14] = "ww3"
            
        if player4 == True:
            grid[24][9] = "ww4"
            
        if player5 == True:
            grid[5][0] = "ww5"
            
        if player6 == True:
            grid[18][0] = "ww6"

        rows, columns = 25, 24

        board = np.empty((rows, columns), dtype = object)

        for row in range(25):
            for column in range(24):
            
                # rooms
                if grid[row][column] == "str":
                    board[row, column] = tile(room = "study")

                if grid[row][column] == "har":
                    board[row, column] = tile(room = "hall")
                    
                if grid[row][column] == "lor":
                    board[row, column] = tile(room = "lounge")

                if grid[row][column] == "drr":
                    board[row, column] = tile(room = "dinning room")
                
                if grid[row][column] == "kir":
                    board[row, column] = tile(room = "kitchen")
                    
                if grid[row][column] == "brr":
                    board[row, column] = tile(room = "ball room")

                if grid[row][column] == "cvr":
                    board[row, column] = tile(room = "conservator")
             
                if grid[row][column] == "bir":
                    board[row, column] = tile(room = "billiards room")
                    
                if grid[row][column] == "lir":
                    board[row, column] = tile(room = "library")

                # doors
                if grid[row][column] == "std":
                    board[row, column] = tile(room = "study", door = True)
                
                if grid[row][column] == "had":
                    board[row, column] = tile(room = "hall", door = True)
                    
                if grid[row][column] == "lod":
                    board[row, column] = tile(room = "lounge", door = True)

                if grid[row][column] == "drd":
                    board[row, column] = tile(room = "dinning room", door = True)
                
                if grid[row][column] == "kid":
                    board[row, column] = tile(room = "kitchen", door = True)
                    
                if grid[row][column] == "brd":
                    board[row, column] = tile(room = "ball room", door = True)

                if grid[row][column] == "cvd":
                    board[row, column] = tile(room = "conservator", door = True)
                
                if grid[row][column] == "bid":
                    board[row, column] = tile(room = "billiards room", door = True)
                    
                if grid[row][column] == "lid":
                    board[row, column] = tile(room = "library", door = True)

                # walkways
                if grid[row][column] == "wwe":
                    board[row, column] = tile(room = "tile", isTile = True)

                if grid[row][column] == "ww1":
                    board[row, column] = tile(room = "tile", isTile = True, player = 1)

                if grid[row][column] == "ww2":
                    board[row, column] = tile(room = "tile", isTile = True, player = 2)
                    
                if grid[row][column] == "ww3":
                    board[row, column] = tile(room = "tile", isTile = True, player = 3)

                if grid[row][column] == "ww4":
                    board[row, column] = tile(room = "tile", isTile = True, player = 4)
                    
                if grid[row][column] == "ww5":
                    board[row, column] = tile(room = "tile", isTile = True, player = 5)

                if grid[row][column] == "ww6":
                    board[row, column] = tile(room = "tile", isTile = True, player = 6)

                # blank cells
                if grid[row][column] == "blk":
                    board[row, column] = tile(blank = True)

        return board
