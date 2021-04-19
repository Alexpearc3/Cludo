from tile import tile
import numpy as np
from array import *
import pandas as pd

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

board = np.empty((25, 24), dtype = object)

#board[0][1] = tile(player = 1)
#print(board[0][1].getPlayer())

count = 0

        
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

        # blank cells
        if grid[row][column] == "blk":
            board[row, column] = tile(blank = True)


array = tile.initiateBoard()

print(array[0, 0].getRoom())
