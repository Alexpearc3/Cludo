import pygame as pg
import sys
#import accuse
import button

class loseScreen:

    def __init__(self):
        pass

    def has_lost(self):

        clock = pg.time.Clock()
        screen = pg.display.set_mode((960, 950))


        buttonNewGame = button.Button(
            (0, 128, 128),
            550, 600,
            350, 50,
            "Press to exit"
        )

        run = True
        while run:
            clock.tick(30)
            pg.display.update()
            event_list = pg.event.get()
            for event in event_list:
                if event.type == pg.QUIT:
                    run = False

            pg.init()

            display_surface = pg.display.set_mode((960, 950))
            pg.display.set_caption('BIG LOSE')
            font = pg.font.Font(None, 200)
            text = font.render('BIG LOSE', True, (102, 0, 102), (0, 128, 128))
            textRect = text.get_rect()
            textRect.center = (475, 200)


            myfont = pg.font.SysFont(None, 60)
            #
            #winText = myfont.render('BIG WIN', False, (0, 0, 0))
            background_image = pg.image.load("../Image/winPic.png")
            screen.fill((102, 0, 102))
            screen.blit(background_image, [0, 0])
            display_surface.blit(text, textRect)

            buttonNewGame.draw(screen)
            buttonNewGame.eventWin(screen, event)
            pg.display.update()

#loseScreen.has_lost(loseScreen)