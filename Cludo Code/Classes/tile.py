import numpy as np
import pygame as py


class tile(object):
    def __init__(self, player, room, state):
        self.player = player
        self.room = room
        self.state = state

    def initiateTile(self):
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
        #24 * 25
        rows, columns = 24, 25


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
