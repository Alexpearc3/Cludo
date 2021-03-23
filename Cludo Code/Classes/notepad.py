import pygame
from pygame import mouse


def notepad():
    # initializing the constructor
    pygame.init()
    import pdb

    # size of window
    x = 400
    y = 900
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
    white = (255, 255, 255)

    # background
    notepad_background_img = "../Image/notepad_background 2.png"
    notepad_background = pygame.image.load(notepad_background_img)
    screen.blit(notepad_background, (0, 0))

    # create red line
    # import fucking room card of fucking stupid Alex
    import room_cards
    import suspect_cards
    import weapon_cards

    # initialise an object of room_cards and use the method getNames to get room_list
    room_list = room_cards.Room_cards().getNames() # name of file and name of class
    suspect_list = suspect_cards.Suspect_cards().getNames() # name of file and name of class
    weapon_list = weapon_cards.Weapon_cards().getNames() # name of file and name of class

    # font
    card_category_font = pygame.font.SysFont('timesnewroman', 24, bold=1)
    card_name_font = pygame.font.SysFont('timesnewroman', 20)

    # create a list includes suspects, rooms, weapons
    general_list = []
    general_list += suspect_list + weapon_list + room_list
    general_list.insert(0, 'Suspect')
    general_list.insert(len(suspect_list)+1, 'Weapon')
    general_list.insert(-len(room_list), 'Room')

    # write items on notepad
    spacing = 113
    for item in general_list:
        if item == 'Suspect':
            screen.blit(card_category_font.render(item, True, gray), (70, spacing))
        elif item == 'Weapon':
            screen.blit(card_category_font.render(item, True, gray), (70, spacing))
        elif item == 'Room':
            screen.blit(card_category_font.render(item, True, gray), (70, spacing))
        else:
            screen.blit(card_name_font.render(item, True, gray), (85, spacing))
        spacing += 29

    # quit button
    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()

    # click button - red line
            # # pygame.draw.rect(screen, red, (x/7, y/5.5, 90, 25))
            # if ev.type == pygame.MOUSEBUTTONDOWN:
            #     spacing = 159
            #     for i in card_name_font:
            #         if spacing - 10 <= mouse[1] <= spacing + 10:
            #             #
            #             pygame.draw.rect(screen, red, [70, spacing, 70, 2])
            # #
            #         pygame.draw.rect(screen, red, [70, 162, 70, 2])
        #         if 110 <= mouse[0] <= 210:
        #             pygame.draw.rect(screen, red, [70, 191, 70, 2])
        #         if 58 <= mouse[2] <= 125:
        #             pygame.draw.rect(screen, gray, [58, 125, 150, 2])
        #     if ev.type == pygame.MOUSEBUTTONUP:
        #         if x / 2 <= mouse[0] <= x / 2 + 140 and y / 2 <= mouse[3] <= y / 2 + 40:
        #             pygame.draw.rect(screen, red, [x / 2, y / 2, 140, 40])
        # mouse = pygame.mouse.get_pos()
        # if x/2 <= mouse[0] <= x/2+140 and y/2 <= mouse[1] <= y/2+40:
        #     pygame.draw.rect(screen,red,[x/2,y/2,140,40])
        # else:
        #     pygame.draw.rect(screen,red,[x/2,y/2,140,40])

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
