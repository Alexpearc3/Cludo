import pygame
from pygame import mouse


def notepad():
    # initializing the constructor
    pygame.init()
    import pdb

    # size of window
    x = 400
    y = 800
    screen = pygame.display.set_mode((x, y))
    # title of window
    pygame.display.set_caption('Notepad')
    # icon of window
    # .. go back 1 time directory
    # ... go back 2 time directory
    icon_img = "../Image/Clue_logo.png"
    icon = pygame.image.load(icon_img)
    pygame.display.set_icon(icon)

    # define the RGB value
    gray = (130, 130, 130)
    red = (255, 0, 0)


    # # create a font object (font file,size)
    # card_category_font = pygame.font.SysFont('timesnewroman', 25, bold=1)
    # card_name_font = pygame.font.SysFont('timesnewroman', 20)
    #
    # # write text and assign color
    # # category
    # suspects = card_category_font.render('Suspects', True, gray)
    # weapons = card_category_font.render('Weapons', True, gray)
    # rooms = card_category_font.render('Rooms', True, gray)
    #
    # # suspects
    # mustard = card_name_font.render('Mustard', True, gray)
    # green = card_name_font.render('Green', True, gray)
    # peacock = card_name_font.render('Peacock', True, gray)
    # scarlett = card_name_font.render('Scarlett', True, gray)
    # rose = card_name_font.render('Rose', True, gray)
    # azure = card_name_font.render('Azure', True, gray)
    # # weapons
    # candlestick = card_name_font.render('Candlestick', True, gray)
    # dagger = card_name_font.render('Dagger', True, gray)
    # lead_pipe = card_name_font.render('Lead Pipe', True, gray)
    # revolver = card_name_font.render('Revolver', True, gray)
    # rope = card_name_font.render('Rope', True, gray)
    # wrench = card_name_font.render('Wrench', True, gray)
    #
    # # rooms
    # ballroom = card_name_font.render('Ballroom', True, gray)
    # billiard_room = card_name_font.render('Billiard Room', True, gray)
    # conservatory = card_name_font.render('Conservatory', True, gray)
    # dinning_room = card_name_font.render('Dinning Room', True, gray)
    # hall = card_name_font.render('Hall', True, gray)
    # kitchen = card_name_font.render('Kitchen', True, gray)
    # library = card_name_font.render('Library', True, gray)
    #
    # # infinite loop
    # while True:
    #     # background
    #     notepad_background_img = "../Image/notepad_background.png"
    #     notepad_background = pygame.image.load(notepad_background_img)
    #     screen.blit(notepad_background, (0, 0))
    #
    #     # set up text position and copy the text surface object to the display surface object
    #     screen.blit(suspects, (58, 115))  # +200
    #     screen.blit(weapons, (56, 315))
    #     screen.blit(rooms, (56, 515))
    #
    #     screen.blit(mustard, (70, 149))  # +29
    #     screen.blit(green, (70, 178))
    #     screen.blit(peacock, (70, 207))
    #     screen.blit(scarlett, (70, 236))
    #     screen.blit(rose, (70, 265))
    #     screen.blit(azure, (70, 294))
    #
    #     screen.blit(candlestick, (70, 349))  # +29
    #     screen.blit(dagger, (70, 378))
    #     screen.blit(lead_pipe, (70, 407))
    #     screen.blit(revolver, (70, 436))
    #     screen.blit(rope, (70, 465))
    #     screen.blit(wrench, (70, 494))
    #
    #     screen.blit(ballroom, (70, 549))  # +29
    #     screen.blit(billiard_room, (70, 578))
    #     screen.blit(conservatory, (70, 607))
    #     screen.blit(dinning_room, (70, 636))
    #     screen.blit(hall, (70, 665))
    #     screen.blit(kitchen, (70, 694))
    #     screen.blit(library, (70, 723))
    #
    #     # drawing event
    #     clock = pygame.time.Clock()
    #     loop = True
    #     press = False
    #     while loop:
    #         try:
    #             # pygame.mouse.set_visible(False)
    #             for event in pygame.event.get():
    #                 if event.type == pygame.QUIT:
    #                     loop = False
    #
    #             px, py = pygame.mouse.get_pos()
    #             if pygame.mouse.get_pressed() == (1, 0, 0):
    #                 pygame.draw.rect(screen, red, (px, py, 3, 3))
    #
    #             if event.type == pygame.MOUSEBUTTONUP:
    #                 press = False
    #             pygame.display.update()
    #             clock.tick(100000)
    #         except Exception as e:
    #             print(e)
    #             pygame.quit()
    #     pygame.quit()
    #     pdb.set_trace()

    # button
    # background
    notepad_background_img = "../Image/notepad_background 2.png"
    notepad_background = pygame.image.load(notepad_background_img)
    screen.blit(notepad_background, (0, 0))

    # light shade of the button
    color_light = (170, 170, 170)
    color = (255, 255, 255)

    # dark shade of the button
    color_dark = (100, 100, 100)


    # create a font object (font file,size)
    card_category_font = pygame.font.SysFont('timesnewroman', 25, bold=1)
    card_name_font = pygame.font.SysFont('timesnewroman', 20)
    # smallfont = pygame.font.SysFont('Corbel',35)
    # suspects = smallfont.render('suspects' , True , gray)
    suspects = screen.blit(card_category_font.render('Suspects', True, gray), (58, 115))
    mustard = screen.blit(card_name_font.render('Mustard', True, gray), (70, 149))
    green = screen.blit(card_name_font.render('Green', True, gray), (70, 178))

    red_line = [58, 115]
    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 80 <= mouse[0] <= 175 :
                    pygame.draw.rect(screen, red, [70, 162, 70, 2])
                if 110 <= mouse[0] <= 210:
                    pygame.draw.rect(screen, red, [70, 191, 70, 2])
                # if 58 <= mouse[2] <= 125:
                #     pygame.draw.rect(screen, gray, [58, 125, 150, 2])
            # if ev.type == pygame.MOUSEBUTTONUP:
            #     if x / 2 <= mouse[0] <= x / 2 + 140 and y / 2 <= mouse[3] <= y / 2 + 40:
            #         pygame.draw.rect(screen, red, [x / 2, y / 2, 140, 40])
        mouse = pygame.mouse.get_pos()
        # if x/2 <= mouse[0] <= x/2+140 and y/2 <= mouse[1] <= y/2+40:
        #     pygame.draw.rect(screen,color_light,[x/2,y/2,140,40])
        # else:
        #     pygame.draw.rect(screen,color_dark,[x/2,y/2,140,40])

        pygame.display.update()

# # iterate over the list of Event objects that was returned by pygame.event.get() method.
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         pygame.quit()
    #         # quit the program.
    #         quit()
    #
    #     # Draws the surface object to the screen.
    #     pygame.display.update()


def innit():
    notepad()


class Notepad:
    notepad()
