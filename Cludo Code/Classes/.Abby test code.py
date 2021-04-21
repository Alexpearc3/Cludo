import os

import pygame
z=154
y = 113
dir = 5
running = 1
width = 400
height = 900
screen = pygame.display.set_mode((width, height))
black = 0, 0, 0
red = 255, 0, 0
pygame.init()
notepad_background_img = "../Image/notepad_background 2.png"
notepad_background = pygame.image.load(notepad_background_img)
screen.blit(notepad_background, (0, 0))

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


# for item in general_list:
#     if (item == 'Suspect') or (item == 'Weapon') or (item == 'Room'):
#         screen.blit(card_category_font.render(item, True, black ), (70, spacing))
#     else:
#         u = screen.blit(card_name_font.render(item, True, black), (85, spacing))
#     spacing += 29
#
#
#     pygame.display.update()



while running:

    # screen.fill(black)
    screen.blit(notepad_background, (0, 0))
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0

    for item in general_list:
        if (item == 'Suspect') or (item == 'Weapon') or (item == 'Room'):
            screen.blit(card_category_font.render(item, True, black), (70, spacing))
        else:
            u = screen.blit(card_name_font.render(item, True, black), (85, spacing))
        spacing += 29

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pygame.draw.rect(screen, red, [75, z, 155, 2])
            if event.button == 3:
                z
        # pygame.display.flip()
            pygame.display.update()

# pygame.display.update()
