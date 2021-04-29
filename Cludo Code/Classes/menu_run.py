import pygame
from menu1 import *


class Menu_Run():
    def __init__(self):
        pygame.init()
        self.running = True #true when game is on
        self.playing = False #when the player is playing the game
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False  # reset keys
        self.Display_Width = 960
        self.Display_Height = 950
        self.display = pygame.Surface((self.Display_Width, self.Display_Height))#creates the canvas
        self.window = pygame.display.set_mode(((self.Display_Width, self.Display_Height))) #to allow player to see what is drawn
        self.font_name = pygame.font.get_default_font()
        self.BLACK =(0,0,0)
        self.WHITE = (255, 255, 255)

        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.custo = CustoMenu(self)
        self.main_menu = MainMenu(self, self.custo)
        self.plName = PlayerNamesMenu(self, self.custo)
        self.curr_menu = self.main_menu #Menu_Run passes itself into the MainMenu class

    def menu_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False
            self.display.fill((0, 0, 0)) #resets canvas
            self.draw_text('gg bro', 20, self.Display_Width/2, self.Display_Height/2)
            self.window.blit(self.display, (0,0)) #aliging display with the window
            pygame.display.update()
            self.reset_keys()
    #checks the events in terms of what keypresses are taken in
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False #stop any menu thats currently being run from being run
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if self.curr_menu == self.plName:
                    if event.key == pygame.K_BACKSPACE:
                        #get all the characters - 1
                        self.plName.plNameEntry = self.plName.plNameEntry[:-1]
                    else:
                        self.plName.plNameEntry += event.unicode

    def reset_keys(self): #self is reference to menu_run so we have access to all the variables
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
    def draw_text(self, text, size, x, y):
        font = pygame.font.Font("../Image/slkscr.ttf", size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect() #rectangle of text
        text_rect.center = (x, y) #centering text
        #text_surface: actual image
        self.display.blit(text_surface, text_rect)