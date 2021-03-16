import pygame


def notepad():
    # initializing the constructor
    pygame.init()
    # title of window
    pygame.display.set_caption('Notepad')
    # icon of window
    # .. go back 1 time directory
    # ... go back 2 time directory
    icon_img = "../Image/Clue_logo.png"
    icon = pygame.image.load(icon_img)
    pygame.display.set_icon(icon)

    # size of window
    screen = pygame.display.set_mode((400, 900))
    done = False
    while not done:
        for event in pygame.event.get():
            # quit window of room
            if event.type == pygame.QUIT:
                done = True
            pygame.display.flip()

    # background
        notepad_background_img = "../Image/notepad_background.png"
        notepad_background = pygame.image.load(notepad_background_img)
        screen.fill((0, 0, 0))
        screen.blit(notepad_background, (0, 0))


def innit():
    notepad()


class Notepad:
    notepad()
