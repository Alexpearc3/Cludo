import pygame

buttonBack = pygame.image.load("../Image/button_back.png")
buttonBackx, buttonBacky = buttonBack.get_size()
buttonBack = pygame.transform.scale(buttonBack, (int(buttonBackx*.4), int(buttonBacky*.4)))

class Dice():
    def __init__(self, number, s):
        self.randomNumber = number
        self.screen = s

    def isButtonClicked(self, x, y):
        if (x >= 720 and x <= 942 and y >= 400 and y <= 481.6):
            #roll dice class function goes here!
            print("backbutton")
            Dice
    
    
    def rolldice(self):

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
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # User clicks the mouse. Get the position
                    pos = pygame.mouse.get_pos()
            
                    self.isButtonClicked(pos[0], pos[1])

            
            
            #enter body here
            #self.screen.blit(buttonBack, (720, 400))

            self.screen.blit(rolledA, (0, 0))
            self.screen.blit(rnumber, (50, 100))
            
            

            clock.tick(60)  #set to 30 to half cycle speeds / reduce processing requirements
            pygame.display.flip()
            self.screen.fill(WHITE)
        #pygame.display.quit()
