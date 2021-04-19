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
                self.cursor_rect.midtop = (self.creditsx - 100, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionsx - 100, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx - 100, self.starty)
                self.state = 'Start'
    def input_check(self):
        self.cursor_move()
        if self.menu_run.START_KEY:
            if self.state == 'Start':
                self.menu_run.playing = True #put in toms code her
            elif self.state == 'Options':
                self.menu_run.curr_menu = self.menu_run.options
            elif self.state == 'Credits':
                self.menu_run.curr_menu = self.menu_run.credits
            self.run_display = False
class OptionsMenu(Menu1):
    def __init__(self, menu_run):
        Menu1.__init__(self, menu_run)
        self.state = 'Save' # cursor points at Save game when it launches
        self.savex, self.savey = self.mid_width, self.mid_height + 20
        self.loadx, self.loady = self.mid_width, self.mid_height + 40
        self.custox, self.custoy = self.mid_width, self.mid_height + 60
        self.cursor_rect.midtop = (self.savex + self.offset, self.savey)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.menu_run.check_events()
            self.input_check()
            self.menu_run.display.fill(self.menu_run.BLACK)
            self.menu_run.draw_text('Options', 20, self.menu_run.Display_Width / 2, self.menu_run.Display_Height / 2 - 30)
            self.menu_run.draw_text('Save Game', 20, self.savex, self.savey)
            self.menu_run.draw_text('Load Game', 20, self.loadx, self.loady)
            self.menu_run.draw_text('Customisation', 20, self.custox, self.custoy)
            self.draw_cursor()
            self.blit_screen()

    #input check for options menu, also aids in returning to prev menu basically menu movement
    def input_check(self):
        if self.menu_run.BACK_KEY:
            self.menu_run.curr_menu = self.menu_run.main_menu
            self.run_display = False
        elif self.menu_run.DOWN_KEY:
            #cursor is at Save rn
            if self.state == 'Save':
                self.cursor_rect.midtop = (self.loadx - 100, self.loady)
                self.state = 'Load'
            elif self.state == 'Load':
                self.cursor_rect.midtop = (self.custox - 100, self.custoy)
                self.state = 'Custo'
            elif self.state == 'Custo':
                self.cursor_rect.midtop = (self.savex - 100, self.savey)
                self.state = 'Save'
        elif self.menu_run.UP_KEY:
            #cursor is at Save rn
            if self.state == 'Save':
                self.cursor_rect.midtop = (self.custox - 100, self.custoy)
                self.state = 'Custo'
            elif self.state == 'Custo':
                self.cursor_rect.midtop = (self.loadx - 100, self.loady)
                self.state = 'Load'
            elif self.state == 'Load':
                self.cursor_rect.midtop = (self.savex - 100, self.savey)
                self.state = 'Save'
        elif self.menu_run.START_KEY:
            #to do: this is where we delve deeper into the custimisation menu
            pass

class CreditsMenu(Menu1):
    def __init__(self, menu_run):
        Menu1.__init__(self, menu_run)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.menu_run.check_events()
            if self.menu_run.START_KEY or self.menu_run.BACK_KEY:
                self.menu_run.curr_menu = self.menu_run.main_menu
                self.run_display = False
            self.menu_run.display.fill(self.menu_run.BLACK)
            self.menu_run.draw_text("Credits", 20, self.menu_run.Display_Width/2, self.menu_run.Display_Height/2 -20)
            self.menu_run.draw_text("Made by Shakir Abdul Aziz, Thomas Shoesmith, Michelle Jones, Le Tu Thien and reluctantly Alex Pearce")
            self.blit_screen()