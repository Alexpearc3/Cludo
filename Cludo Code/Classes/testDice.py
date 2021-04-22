import pygame
import numpy as np
from random import randrange

from testMultipleWindows2 import Dice


pygame.init()
pygame.font.init()

pygame.display.set_caption("Cludo")
screen = pygame.display.set_mode([950, 960])


        
class Dice2():
    #loading images for buttons unselected
    buttonBack = pygame.image.load("../Image/button_back.png")
    buttonBackx, buttonBacky = buttonBack.get_size()
    buttonBack = pygame.transform.scale(buttonBack, (int(buttonBackx*.4), int(buttonBacky*.4)))
    def __init__(self, number):
        self.randomNumber = number

    def isButtonClicked(self, x, y):
        if (x >= 720 and x <= 942 and y >= 400 and y <= 481.6):
            #roll dice class function goes here!
            print("backbutton")
            Dice(12, screen).rolldice()
    
    
    def rolldice(self):

        WHITE = (255, 255, 255)
        imgPlayer1 = pygame.image.load("../Image/player_1.png")

        #loading previous turn font style
        clueFont = pygame.font.SysFont("Segoe UI Black", 50)
        rolledA = clueFont.render("YOU ROLLED A TEST:", False, (50, 50, 50))
        rnumber = clueFont.render(str(self.randomNumber), False, (50, 50, 50))

        clock = pygame.time.Clock()
        pygame.display.set_icon(imgPlayer1)

        done = False

        #game loop
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # User clicks the mouse. Get the position
                    pos = pygame.mouse.get_pos()
            
                    self.isButtonClicked(pos[0], pos[1])

            
            
            #enter body here
            screen.blit(self.buttonBack, (720, 400))

            screen.blit(rolledA, (0, 0))
            screen.blit(rnumber, (50, 100))
            
            

            clock.tick(60)  #set to 30 to half cycle speeds / reduce processing requirements
            pygame.display.flip()
            screen.fill(WHITE)
        pygame.quit()
        

new = Dice2(randrange(100)+1)
new.rolldice()
