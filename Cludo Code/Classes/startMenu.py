import pygame
import random
import numpy as np



class StartMenu():
    def __init__(self):
        pygame.init()
        self.run_screen = True
        self.cursor = pygame.rect(0, 0, 20, 20)
        self.window = pygame.display.set_mode(((self.display_width, self.display_height)))
        self.display = pygame.Surface((self.display_width, self.display_height))
    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y) #centering text
        #text_surface: actual image
        self.display.blit(text_surface, text_rect)
    def draw_cursor(self):
        self.draw_text('^', 15, self.cursor_rect.x, self.cursor_rect.y)
    def blit_screen(self):
        self.window.blit(self.display, (0,0))
        pygame.display.update()
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False #reset keys
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

class MainMenu(StartMenu):
    def __init__(self):
        StartMenu.__init__(self)
        self.state = 'Start' #cursor points at start game when it launches
        self.startx, self.starty = self.mid_width, self.mid_height + 30
        self.optionsx, self.optionsy = self.mid_width, self.mid_height + 70
        self.creditsx, self.creditsy = self.mid_width, self.mid_height + 110
        self.curor_rect.midtop = (self.startx -20, self.starty)
    def display_startMenu(self):
        self.run_display = True
        while self.run_display:
            self.display.fill(0, 0, 0)
            self.check_events() #gather player inputs
            self.input_check() #check what the inputs were
            self.draw_text('Start Menu', 20, self.display_width/2, self.display_height/2 - 30)
            self.draw_text('Start Game', 20, self.startx, self.starty)
            self.draw_text('Start Game', 20, self.optionsx, self.optionsy)
            self.draw_text('Start Game', 20, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen() # put it all on screen
    def cursor_move(self):
        if self.DOWN_KEY:
            if self.state == 'Start':
                self.curor_rect.midtop = (self.optionsx - 20, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.curor_rect.midtop = (self.creditsx - 20, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.curor_rect.midtop = (self.startx - 20, self.starty)
                self.state = 'Start'
        if self.UP_KEY:
            if self.state == 'Start':
                self.curor_rect.midtop = (self.optionsx - 20, self.optionsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.curor_rect.midtop = (self.startx - 20, self.starty)
                self.state = 'Options'
            elif self.state == 'Options':
                self.curor_rect.midtop = (self.creditsx - 20, self.creditsy)
                self.state = 'Start'
    def input_check(self):
        self.cursor_move()
        if self.START_KEY:
            if self.state == 'Start':
                self.playing = True
            elif self.state == 'Options':
                pass
            elif self.state == 'Credits':
                pass
            self.run_display = False
#need to run display.startmenu somewhere idk where
#i think it needs to be run within a game state