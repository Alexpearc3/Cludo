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
    def getBoardType(self, CustoMenu):
        return CustoMenu.boardType

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
                #Dice(12, pygame.display.set_mode([950, 960])).rolldice()
                self.menu_run.playing = True #put in toms code her
                #Notepad_Main.notepadRun()
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
            if self.state == 'Custo':
                self.menu_run.curr_menu = self.menu_run.custo
            self.run_display = False


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
            self.menu_run.draw_text("Credits", 40, self.menu_run.Display_Width/2, self.menu_run.Display_Height - 900)
            self.menu_run.draw_text("Made by:", 20, self.menu_run.Display_Width/2, self.menu_run.Display_Height - 900 + 40)
            self.menu_run.draw_text("Shakir Abdul Aziz", 20, self.menu_run.Display_Width / 2, self.menu_run.Display_Height - 900 + 80)
            self.menu_run.draw_text("Thomas Shoesmith", 20, self.menu_run.Display_Width/2, self.menu_run.Display_Height - 900 + 120)
            self.menu_run.draw_text("Michelle Jones", 20, self.menu_run.Display_Width / 2, self.menu_run.Display_Height - 900 + 160)
            self.menu_run.draw_text("Y Le Tu Thien", 20, self.menu_run.Display_Width / 2, self.menu_run.Display_Height - 900 + 200)
            self.menu_run.draw_text("And reluctantly,", 20, self.menu_run.Display_Width / 2, self.menu_run.Display_Height - 900+ 240)
            self.menu_run.draw_text("Alex Pearce", 20, self.menu_run.Display_Width / 2, self.menu_run.Display_Height - 900 + 280)
            self.blit_screen()
class CustoMenu(Menu1):
    def __init__(self, menu_run):
        Menu1.__init__(self, menu_run)
        self.state = 'one'
        self.onex, self.oney = (self.menu_run.Display_Width/2 + 173, self.menu_run.Display_Height - 860)
        self.twox, self.twoy = (self.menu_run.Display_Width/2 + 173, self.menu_run.Display_Height - 840)
        self.threex, self.threey = (self.menu_run.Display_Width/2 + 173, self.menu_run.Display_Height - 820)
        self.fourx, self.foury = (self.menu_run.Display_Width / 2 + 173, self.menu_run.Display_Height - 800)
        self.fivex, self.fivey = (self.menu_run.Display_Width / 2 + 173, self.menu_run.Display_Height - 780)
        self.sixx, self.sixy = (self.menu_run.Display_Width / 2 + 173, self.menu_run.Display_Height - 760)
        self.Ax, self.Ay = (self.menu_run.Display_Width / 2 + 95, self.menu_run.Display_Height - 700)
        self.Bx, self.By = (self.menu_run.Display_Width / 2 + 95, self.menu_run.Display_Height - 675)
        self.cursor_rect.midtop = (self.menu_run.Display_Width/2 + 173, self.menu_run.Display_Height - 860)
        self.playerNum = 6
        self.boardType = 1
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.menu_run.check_events()
            self.input_check()
            # if self.menu_run.START_KEY or self.menu_run.BACK_KEY:
            #     self.menu_run.curr_menu = self.menu_run.main_menu
            #     self.run_display = False
            self.menu_run.display.fill(self.menu_run.BLACK)
            self.menu_run.draw_text("Customisation", 40, self.menu_run.Display_Width / 2, self.menu_run.Display_Height - 900)
            self.menu_run.draw_text("choose number of players:", 20, self.menu_run.Display_Width / 2, self.menu_run.Display_Height - 860)
            self.menu_run.draw_text("1", 20, self.menu_run.Display_Width/2 + 150, self.oney)
            self.menu_run.draw_text("2", 20, self.menu_run.Display_Width / 2 + 150, self.menu_run.Display_Height - 840)
            self.menu_run.draw_text("3", 20, self.menu_run.Display_Width / 2 + 150, self.menu_run.Display_Height - 820)
            self.menu_run.draw_text("4", 20, self.menu_run.Display_Width / 2 + 150, self.menu_run.Display_Height - 800)
            self.menu_run.draw_text("5", 20, self.menu_run.Display_Width / 2 + 150, self.menu_run.Display_Height - 780)
            self.menu_run.draw_text("6", 20, self.menu_run.Display_Width / 2 + 150, self.menu_run.Display_Height - 760)
            self.menu_run.draw_text("Board type:", 20, self.menu_run.Display_Width / 2, self.menu_run.Display_Height - 700)
            self.menu_run.draw_text("A", 20, self.menu_run.Display_Width / 2 + 70, self.menu_run.Display_Height - 700)
            self.menu_run.draw_text("B", 20, self.menu_run.Display_Width / 2 + 70, self.menu_run.Display_Height - 675)
            self.draw_cursor()
            self.blit_screen()
    def input_check(self):
        if self.menu_run.BACK_KEY:
            self.menu_run.curr_menu = self.menu_run.main_menu
            self.run_display = False
        elif self.menu_run.DOWN_KEY:
            #cursor is at one rn
            if self.state == 'one':
                self.cursor_rect.midtop = (self.twox, self.twoy)
                self.state = 'two'
            elif self.state == 'two':
                self.cursor_rect.midtop = (self.threex, self.threey)
                self.state = 'three'
            elif self.state == 'three':
                self.cursor_rect.midtop = (self.fourx, self.foury)
                self.state = 'four'
            elif self.state == 'four':
                self.cursor_rect.midtop = (self.fivex, self.fivey)
                self.state = 'five'
            elif self.state == 'five':
                self.cursor_rect.midtop = (self.sixx, self.sixy)
                self.state = 'six'
            elif self.state == 'six':
                self.cursor_rect.midtop = (self.onex, self.oney)
                self.state = 'one'
            elif self.state == 'A':
                self.cursor_rect.midtop = (self.Bx, self.By)
                self.state = 'B'
            elif self.state == 'B':
                self.cursor_rect.midtop = (self.Ax, self.Ay)
                self.state = 'A'
        elif self.menu_run.UP_KEY:
                # cursor is at one rn
            if self.state == 'one':
                self.cursor_rect.midtop = (self.sixx, self.sixy)
                self.state = 'six'
            elif self.state == 'six':
                self.cursor_rect.midtop = (self.fivex, self.fivey)
                self.state = 'five'
            elif self.state == 'five':
                self.cursor_rect.midtop = (self.fourx, self.foury)
                self.state = 'four'
            elif self.state == 'four':
                self.cursor_rect.midtop = (self.threex, self.threey)
                self.state = 'three'
            elif self.state == 'three':
                self.cursor_rect.midtop = (self.twox, self.twoy)
                self.state = 'two'
            elif self.state == 'two':
                self.cursor_rect.midtop = (self.onex, self.oney)
                self.state = 'one'
            elif self.state == 'A':
                self.cursor_rect.midtop = (self.Bx, self.By)
                self.state = 'B'
            elif self.state == 'B':
                self.cursor_rect.midtop = (self.Ax, self.Ay)
                self.state = 'A'
        #if enter is pressed:
        elif self.menu_run.START_KEY:
            if self.state == 'one':
                self.playerNum = 1
                self.playerArr =['']
                self.state = 'A'
                self.cursor_rect.midtop = (self.Ax, self.Ay)
            elif self.state == 'two':
                self.playerNum = 2
                self.state = 'A'
                self.cursor_rect.midtop = (self.Ax, self.Ay)
            elif self.state == 'three':
                self.playerNum = 3
                self.state = 'A'
                self.cursor_rect.midtop = (self.Ax, self.Ay)
            elif self.state == 'four':
                self.playerNum = 4
                self.state = 'A'
                self.cursor_rect.midtop = (self.Ax, self.Ay)
            elif self.state == 'five':
                self.playerNum = 5
                self.state = 'A'
                self.cursor_rect.midtop = (self.Ax, self.Ay)
            elif self.state == 'six':
                self.playerNum = 6
                self.state = 'A'
                self.cursor_rect.midtop = (self.Ax, self.Ay)

            elif self.state == 'A':
                self.boardType = 1
            elif self.state == 'B':
                self.boardType = 2