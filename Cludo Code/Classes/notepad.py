import pygame
# import pyttsx3
# import speech_recognition
from numpy.distutils.fcompiler import pg
from pygame import mouse


def notepad():
    # initializing the constructor
    pygame.init()

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
    # import card information from other classes
    import room_cards
    import suspect_cards
    import weapon_cards

    # initialise an object of room_cards and use the method getNames to get room_list
    room_list = room_cards.Room_cards().getNames()  # name of file and name of class
    suspect_list = suspect_cards.Suspect_cards().getNames()  # name of file and name of class
    weapon_list = weapon_cards.Weapon_cards().getNames()  # name of file and name of class

    # font
    card_category_font = pygame.font.SysFont('timesnewroman', 24, bold=1)
    card_name_font = pygame.font.SysFont('timesnewroman', 20)

    # create a list includes suspects, rooms, weapons
    general_list = []
    general_list += suspect_list + weapon_list + room_list
    general_list.insert(0, 'Suspect')
    general_list.insert(len(suspect_list) + 1, 'Weapon')
    general_list.insert(-len(room_list), 'Room')

    # write items on notepad
    spacing = 113
    for item in general_list:
        if (item == 'Suspect') or (item == 'Weapon') or (item == 'Room'):
            screen.blit(card_category_font.render(item, True, gray), (70, spacing))
        else:
            u = screen.blit(card_name_font.render(item, True, gray), (85, spacing))
        spacing += 29
    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                spacing = 154
                Mouse = pygame.mouse.get_pos()
                for item in general_list:
                    if ev.button == 1 and spacing - 10 <= Mouse[1] <= spacing + 10 and not (item == 'Mrs Peacock' or item == 'Knife'):
                        line=pygame.draw.rect(screen, red, [75, spacing, 155, 2])
                    if ev.button == 3 and spacing - 10 <= Mouse[1] <= spacing + 10 and not (item == 'Mrs Peacock' or item == 'Knife'):
                        pygame.draw.rect(screen, white, [75, spacing, 155, 2])
                    spacing += 29
        pygame.display.update()


def innit():
    notepad()