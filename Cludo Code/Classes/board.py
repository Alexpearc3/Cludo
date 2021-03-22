import pygame
import numpy as np

BOARDWIDTH = 25
BOARDHEIGHT = 24
WINDOWWIDTH = 500
WINDOWHEIGHT = 500
WIDTH = 40
HEIGHT = 40

BLACK = (141, 197, 137)

pygame.init()
pygame.display.set_caption("Cludo")

tileImg = pygame.image.load("../Image/tile_unselected_empty.png")
tileImg = pygame.transform.scale(tileImg, (int(WIDTH), int(HEIGHT)))
tileImgSELECT = pygame.image.load("../Image/tile_unselected_selected.png")
tileImgSELECT = pygame.transform.scale(tileImgSELECT, (int(WIDTH), int(HEIGHT)))
tileImgHover = pygame.image.load("../Image/tile_unselected_hover.png")
tileImgHover = pygame.transform.scale(tileImgHover, (int(WIDTH), int(HEIGHT)))

background = pygame.image.load("../Image/background.png")


screen = pygame.display.set_mode([960, 1000])


def grid(x, y):
    screen.blit(tileImg, (x,y))
    


def cludo():
    grid(10,20)
    grid(40, 50)


grid = [[1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1], 
        [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1], 
        [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1], 
        [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1], 
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1], 
        [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
        [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
        [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1], 
        [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1], 
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1], 
        [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1], 
        [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1], 
        [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1], 
        [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1], 
        [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1], 
        [1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1], 
        [1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1], 
        [1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1], 
        [1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1], 
        [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1], 
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]]



done = False

clock = pygame.time.Clock()


while not done:
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH)
            row = pos[1] // (HEIGHT)
            # Set that location to one
            try:
                if (grid[int(row)][int(column)]) == 0:
                    grid[int(row)][int(column)] = 2
                elif (grid[int(row)][int(column)]) == 2:
                    grid[int(row)][int(column)] = 0
            except:
                print("outside grid") 
            
    # Set the screen background
    #screen.fill(BLACK)
    screen.blit(background, (0, 0))

     
    # Draw the grid
    for row in range(BOARDWIDTH):
        for column in range(BOARDHEIGHT):
            x, y = pygame.mouse.get_pos()
            if (np.ceil(x/40) == column+1 and np.ceil(y/40) == row+1 and grid[row][column] == 0 and pygame.mouse.get_pressed()[0] == 1):
                screen.blit(tileImgSELECT, (column*WIDTH,HEIGHT*row))
            elif (np.ceil(x/40) == column+1 and np.ceil(y/40) == row+1 and grid[row][column] == 0):
                screen.blit(tileImgHover, (column*WIDTH,HEIGHT*row))
            elif grid[row][column] == 0:
                screen.blit(tileImg, (column*WIDTH,HEIGHT*row))
            elif grid[row][column] == 2:
                screen.blit(tileImgSELECT, (column*WIDTH,HEIGHT*row))
 
    clock.tick(60)
    pygame.display.flip()
pygame.quit()
