import pygame

buttonBack = pygame.image.load("../Image/button_back.png")
buttonBackx, buttonBacky = buttonBack.get_size()
buttonBack = pygame.transform.scale(buttonBack, (int(buttonBackx*.5), int(buttonBacky*.5)))
buttonBackSelected = pygame.image.load("../Image/button_back_selected.png")
buttonBackSelectedx, buttonBackSelectedy = buttonBackSelected.get_size()
buttonBackSelected = pygame.transform.scale(buttonBackSelected, (int(buttonBackSelectedx*.5), int(buttonBackSelectedy*.5)))
background = pygame.image.load("../Image/background_blur.png")
youveRolledA = pygame.image.load("../Image/text_you've_rolled_a.png")
GREEN = (141, 197, 137)

class Dice():
    """
    A Class to display the roll of a dice
    """
    def __init__(self, number, s):
        """
        init for the Dice class.

            Parameters:
                number (int): This is the random number generate on board end
                s (screen): screen for pygame to display to
        """
        self.randomNumber = number
        self.screen = s
        self.done = False


    def isButtonClicked(self, x, y):
        """
        checks to see if button has been clicked.

            Parameters:
                x (int): coordinate of button click
                y (int): coordinate of button click
        """
        if (x >= ((950/2)-((buttonBackx/2)*.5)) and x <= ((950/2)-((buttonBackx/2)*.5)+(buttonBackx * 0.5)) and y >= 750 and y <= (750+(buttonBacky * 0.5))):
            self.done = True


    def isButtonSelected(self, x, y):
        """
        checks to see if button has mouse hovering over.

            Parameters:
                x (int): coordinate of mouse location
                y (int): coordinate of mouse location
        """
        if (x >= ((950/2)-((buttonBackx/2)*.5)) and x <= ((950/2)-((buttonBackx/2)*.5)+(buttonBackx * 0.5)) and y >= 750 and y <= (750+(buttonBacky * 0.5))):
            self.screen.blit(buttonBackSelected, ((950/2)-((buttonBackx/2)*.5), 750))  

    
    def rolldice(self):
        """
        main gameloop of pygame, here pygame displays the buttons and runs
        functionality on the button
        """       
        WHITE = (255, 255, 255)
        imgPlayer1 = pygame.image.load("../Image/player_1.png")

        #loading previous turn font style
        clueFont = pygame.font.SysFont("Segoe UI Black", 300)
        rnumber = clueFont.render(str(self.randomNumber), False, (255, 255, 255))

        clock = pygame.time.Clock()
        pygame.display.set_icon(imgPlayer1)

        #game loop
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # If user clicked close
                    self.done = True  # Flag that we are done so we exit this loop
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # User clicks the mouse. Get the position
                    pos = pygame.mouse.get_pos()
                    self.isButtonClicked(pos[0], pos[1])

            self.screen.fill(GREEN)
            self.screen.blit(background, (0,0))
            self.screen.blit(youveRolledA, (80, 100))
            self.screen.blit(rnumber, (370, 300))
            self.screen.blit(buttonBack, ((950/2)-((buttonBackx/2)*.5), 750))            

            pos = pygame.mouse.get_pos()
            self.isButtonSelected(pos[0], pos[1])

            clock.tick(30)  #set to 30 to half cycle speeds / reduce processing requirements
            pygame.display.flip()
            self.screen.fill(WHITE)
