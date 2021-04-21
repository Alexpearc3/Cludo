import pygame

pygame.init()  # initializes the graphics module
window = pygame.display.set_mode((800, 600))  # define window size
pygame.display.set_caption('Intro to PyGame')  # title of program that appears on window frame

# COLOURS
green = (0, 250, 0)
red = (0, 255, 255)
black = (0, 0, 0)
white = (255, 255, 255)


# DRAWS SCREEN 1
def screen1():
    window.fill(black)
    pygame.draw.rect(window, green, (200, 300, 100, 100))


# DRAWS SCREEN 2
def screen2():
    window.fill(black)
    pygame.draw.rect(window, red, (200, 300, 100, 100))


# CHANGES SCREENS
screens = [screen1(), screen2()]
current_screen = 0

clock = pygame.time.Clock()  # used to track time within the game (FPS)
quit = False
while not quit:  # main program loop
    for event in pygame.event.get():  # check if there were any events
        if event.type == pygame.QUIT:  # check if user clicked the upper
            quit = True  # right quit button your code that draws to the window goes here
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                current_screen += 1
                screens[current_screen]()

    pygame.display.update()  # refresh your display
    clock.tick(60)  # wait a certain amount of time that ensures a frame rate of 60 fps

pygame.quit()  # shutdown module
