import pygame


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

    # create a font object (font file,size)
    card_category_font = pygame.font.SysFont('timesnewroman', 25, bold=1)
    card_name_font = pygame.font.SysFont('timesnewroman', 20)

    # write text and assign color
    suspects = card_category_font.render('Suspects', True, gray)
    weapons = card_category_font.render('Weapons', True, gray)
    rooms = card_category_font.render('Rooms', True, gray)

    mustard = card_name_font.render('Mustard', True, gray)
    green = card_name_font.render('Green', True, gray)
    peacock = card_name_font.render('Peacock', True, gray)
    scarlett = card_name_font.render('Scarlett', True, gray)
    rose = card_name_font.render('Rose', True, gray)
    azure = card_name_font.render('Azure', True, gray)

    # infinite loop
    while True:
        # background
        notepad_background_img = "../Image/notepad_background.png"
        notepad_background = pygame.image.load(notepad_background_img)
        screen.blit(notepad_background, (0, 0))

        # set up text position and copy the text surface object to the display surface object
        screen.blit(suspects, (58, 115))  # +200
        screen.blit(weapons, (56, 315))
        screen.blit(rooms, (56, 515))

        screen.blit(mustard, (70, 149))  # +29
        screen.blit(green, (70, 178))
        screen.blit(peacock, (70, 207))
        screen.blit(scarlett, (70, 236))
        screen.blit(rose, (70, 265))
        screen.blit(azure, (70, 294))

        ################## event
        clock = pygame.time.Clock()
        loop = True
        press = False
        while loop:
            try:
                # pygame.mouse.set_visible(False)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        loop = False

                px, py = pygame.mouse.get_pos()
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    pygame.draw.rect(screen, red, (px, py, 3, 3))

                if event.type == pygame.MOUSEBUTTONUP:
                    press = False
                pygame.display.update()
                clock.tick(100000)
            except Exception as e:
                print(e)
                pygame.quit()
        pygame.quit()
        pdb.set_trace()
        #################################################################

        # iterate over the list of Event objects that was returned by pygame.event.get() method.
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
