import pygame

class Menu1:
    def __init__(self, menu_run):
        self.menu_run = menu_run
        self.mid_width, self.mid_height = self.menu_run.Display_Width/2, self.menu_run.Display_Height/2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)#20 x 20 square as cursor
        self.offset = -100

    def draw_cursor(self):
        self.menu_run.draw_text('^', 15, self.cursor_rect.x, self.cursor_rect.y)
    def blit_screen(self):
        self.menu_run.window.blit(self.menu_run.display, (0,0))
        pygame.display.update()
        self.menu_run.reset_keys()
class MainMenu(Menu1):
    def __init__(self, menu_run):
        Menu1.__init__(self, menu_run) #allows us to use variables from Menu1
        self.state = 'Start'  # cursor points at start game when it launches
        self.startx, self.starty = self.mid_width, self.mid_height + 30
        self.optionsx, self.optionsy = self.mid_width, self.mid_height + 70
        self.creditsx, self.creditsy = self.mid_width, self.mid_height + 110
        self.cursor_rect.midtop = (self.startx - 100, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.menu_run.display.fill(self.menu_run.BLACK)
            self.menu_run.check_events()  # gather player inputs
            self.input_check()  # check what the inputs were
            self.menu_run.draw_text('Start Menu', 20, self.menu_run.Display_Width / 2, self.menu_run.Display_Height / 2 - 30)
            self.menu_run.draw_text('Start Game', 20, self.startx, self.starty)
            self.menu_run.draw_text('options', 20, self.optionsx, self.optionsy)
            self.menu_run.draw_text('credits', 20, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()  # put it all on screen
    def cursor_move(self):
        if self.menu_run.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx - 100, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx - 100, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx - 100, self.starty)
                self.state = 'Start'
        if self.menu_run.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx - 100, self.optionsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx - 100, self.starty)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx - 100, self.creditsy)
                self.state = 'Start'
    def input_check(self):
        self.cursor_move()
        if self.menu_run.START_KEY:
            if self.state == 'Start':
                self.menu_run.playing = True
            elif self.state == 'Options':
                pass
            elif self.state == 'Credits':
                pass
            self.run_display = False