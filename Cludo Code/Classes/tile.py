import numpy as np
import pygame as py


class tile(object):
    def __init__(self, player, room, state):
        self.player = player
        self.room = room
        self.state = state

    def initiateTile():
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

        grid = [["str", "str", "str", "str", "str", "str", "str", "wwe", "blk", "blk", "har", "har", "har", "har", "har", "blk", "wwe", 1, 1, 1, 1, 1, 1, 1],
                ["str", "str", "str", "str", "str", "str", "str", "wwe", "wwe", "har", "har", "har", "har", "har", "har", "wwe", "wwe", 1, 1, 1, 1, 1, 1, 1],
                ["str", "str", "str", "str", "str", "str", "str", "wwe", "wwe", "har", "har", "har", "har", "har", "har", "wwe", "wwe", 1, 1, 1, 1, 1, 1, 1],
                ["str", "str", "str", "str", "str", "str", "str", "wwe", "wwe", "har", "har", "har", "har", "har", "har", "wwe", "wwe", 1, 1, 1, 1, 1, 1, 1],
                ["blk", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "har", "har", "har", "har", "har", "har", "wwe", "wwe", 1, 1, 1, 1, 1, 1, 1],
                ["wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "har", "har", "har", "har", "har", "har", "wwe", "wwe", 1, 1, 1, 1, 1, 1, 1],
                ["blk", "lir", "lir", "lir", "lir", "lir", "wwe", "wwe", "wwe", "har", "har", "har", "har", "har", "har", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", v],
                ["lir", "lir", "lir", "lir", "lir", "lir", "lir", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe"],
                ["lir", "lir", "lir", "lir", "lir", "lir", "lir", "wwe", "wwe", 1, 1, 1, 1, 1, "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", 1],
                ["lir", "lir", "lir", "lir", "lir", "lir", "lir", "wwe", "wwe", 1, 1, 1, 1, 1, "wwe", "wwe", 1, 1, 1, 1, 1, 1, 1, 1],
                ["blk", "lir", "lir", "lir", "lir", "lir", "wwe", "wwe", "wwe", 1, 1, 1, 1, 1, "wwe", "wwe", 1, 1, 1, 1, 1, 1, 1, 1],
                ["blk", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", 1, 1, 1, 1, 1, "wwe", "wwe", 1, 1, 1, 1, 1, 1, 1, 1],
                ["bir", "bir", "bir", "bir", "bir", "bir", "wwe", "wwe", "wwe", 1, 1, 1, 1, 1, "wwe", "wwe", 1, 1, 1, 1, 1, 1, 1, 1],
                ["bir", "bir", "bir", "bir", "bir", "bir", "wwe", "wwe", "wwe", 1, 1, 1, 1, 1, "wwe", "wwe", 1, 1, 1, 1, 1, 1, 1, 1],
                ["bir", "bir", "bir", "bir", "bir", "bir", "wwe", "wwe", "wwe", 1, 1, 1, 1, 1, "wwe", "wwe", 1, 1, 1, 1, 1, 1, 1, 1],
                ["bir", "bir", "bir", "bir", "bir", "bir", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", 1, 1, 1, 1, 1],
                ["bir", "bir", "bir", "bir", "bir", "bir", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", 1],
                [1, "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", 1, 1, 1, 1, 1, 1, 1, 1, "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe"],
                ["wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", 1, 1, 1, 1, 1, 1, 1, 1, "wwe", "wwe", 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, "wwe", "wwe", "wwe", 1, 1, 1, 1, 1, 1, 1, 1, "wwe", "wwe", 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, "wwe", "wwe", 1, 1, 1, 1, 1, 1, 1, 1, "wwe", "wwe", 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, "wwe", "wwe", 1, 1, 1, 1, 1, 1, 1, 1, "wwe", "wwe", 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, "wwe", "wwe", 1, 1, 1, 1, 1, 1, 1, 1, "wwe", "wwe", 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, "wwe", "wwe", "wwe", 1, 1, 1, 1, "wwe", "wwe", "wwe", 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, "wwe", 1, 1, 1, 1, "wwe", 1, 1, 1, 1, 1, 1, 1, 1, 1]]
