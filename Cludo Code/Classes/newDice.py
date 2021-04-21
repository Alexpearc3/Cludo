import pygame
import numpy as np
from random import randrange

class Dice():
    def __init__(self, number):
        self.randomNumber = number
    
    
    def rolldice(self):
        pygame.init()
        pygame.font.init()

        pygame.display.set_caption("Cludo")
        screen = pygame.display.set_mode([500, 500])

        WHITE = (255, 255, 255)
        imgPlayer1 = pygame.image.load("../Image/player_1.png")

        #loading previous turn font style
        clueFont = pygame.font.SysFont("Segoe UI Black", 50)
        rolledA = clueFont.render("YOU ROLLED A:", False, (50, 50, 50))
        rnumber = clueFont.render(str(self.randomNumber), False, (50, 50, 50))

        clock = pygame.time.Clock()
        pygame.display.set_icon(imgPlayer1)

        done = False

        #game loop
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop
                    

            
            
            #enter body here

            screen.blit(rolledA, (0, 0))
            screen.blit(rnumber, (50, 100))
            
            

            clock.tick(60)  #set to 30 to half cycle speeds / reduce processing requirements
            pygame.display.flip()
            screen.fill(WHITE)
        pygame.quit()
        

new = Dice(12)
new.rolldice()
