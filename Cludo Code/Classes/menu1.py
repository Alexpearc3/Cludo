import pygame
from board import board
from notepad import Notepad
class Menu1:
    def __init__(self, menu_run):
        self.menu_run = menu_run
        self.mid_width, self.mid_height = self.menu_run.Display_Width/2, self.menu_run.Display_Height/2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)#20 x 20 square as cursor
        self.offset = -100
        self.background_image = pygame.image.load("../Image/CluedoMenu.jpg")

    def draw_cursor(self):
        self.menu_run.draw_text('^', 15, self.cursor_rect.x, self.cursor_rect.y)
    def blit_screen(self):
        self.menu_run.window.blit(self.menu_run.display, (0,0))
        pygame.display.update()
        self.menu_run.reset_keys()
    def getBoardType(self, CustoMenu):
        return CustoMenu.boardType


class MainMenu(Menu1):
    def __init__(self, menu_run, CustoMenu):
        Menu1.__init__(self, menu_run) #allows us to use variables from Menu1
        self.CustoMenu = CustoMenu
        self.state = 'Start'  # cursor points at start game when it launches
        self.startx, self.starty = self.mid_width, self.mid_height + 30
        self.optionsx, self.optionsy = self.mid_width, self.mid_height + 70
        self.creditsx, self.creditsy = self.mid_width, self.mid_height + 110
        self.cursor_rect.midtop = (self.startx - 70, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.menu_run.display.fill(self.menu_run.BLACK)
            self.menu_run.display.blit(self.background_image, [-530, 0])
            self.menu_run.check_events()  # gather player inputs
            self.input_check()  # check what the inputs were
            self.menu_run.draw_text('Start Menu', 40, self.menu_run.Display_Width / 2, self.menu_run.Display_Height / 2 - 30)
            self.menu_run.draw_text('Start Game', 20, self.startx, self.starty)
            self.menu_run.draw_text('options', 20, self.optionsx, self.optionsy)
            self.menu_run.draw_text('credits', 20, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()  # put it all on screen

    def cursor_move(self):
        if self.menu_run.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx - 70, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx - 70, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx - 70, self.starty)
                self.state = 'Start'
        if self.menu_run.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx - 70, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionsx - 70, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx - 70, self.starty)
                self.state = 'Start'
    def input_check(self):
        self.cursor_move()
        if self.menu_run.START_KEY:
            if self.state == 'Start':
                #Dice(12, pygame.display.set_mode([950, 960])).rolldice()
                #self.menu_run.playing = True #put in toms code her
                playerList = self.CustoMenu.playerArr
                b = board(playerList, 2).main()
                #self.CustoMenu.boardType
                #print("the board type is " + str(self.CustoMenu.boardType))
                #Notepad.notepad(self)

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
        self.cursor_rect.midtop = (self.savex -77, self.savey)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.menu_run.check_events()
            self.input_check()
            self.menu_run.display.fill(self.menu_run.BLACK)
            self.menu_run.display.blit(self.background_image, [-530, 0])
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
                self.cursor_rect.midtop = (self.loadx - 77, self.loady)
                self.state = 'Load'
            elif self.state == 'Load':
                self.cursor_rect.midtop = (self.custox - 77, self.custoy)
                self.state = 'Custo'
            elif self.state == 'Custo':
                self.cursor_rect.midtop = (self.savex - 77, self.savey)
                self.state = 'Save'
        elif self.menu_run.UP_KEY:
            #cursor is at Save rn
            if self.state == 'Save':
                self.cursor_rect.midtop = (self.custox - 77, self.custoy)
                self.state = 'Custo'
            elif self.state == 'Custo':
                self.cursor_rect.midtop = (self.loadx - 77, self.loady)
                self.state = 'Load'
            elif self.state == 'Load':
                self.cursor_rect.midtop = (self.savex - 77, self.savey)
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
            self.menu_run.display.blit(self.background_image, [-530, 0])
            self.menu_run.draw_text("Credits", 40, self.menu_run.Display_Width/2, self.menu_run.Display_Height - 600)
            self.menu_run.draw_text("Made by:", 20, self.menu_run.Display_Width/2, self.menu_run.Display_Height - 900 + 340)
            self.menu_run.draw_text("Shakir Abdul Aziz", 20, self.menu_run.Display_Width / 2, self.menu_run.Display_Height - 900 + 380)
            self.menu_run.draw_text("Thomas Shoesmith", 20, self.menu_run.Display_Width/2, self.menu_run.Display_Height - 900 + 420)
            self.menu_run.draw_text("Michelle Jones", 20, self.menu_run.Display_Width / 2, self.menu_run.Display_Height - 900 + 460)
            self.menu_run.draw_text("Y Le Tu Thien", 20, self.menu_run.Display_Width / 2, self.menu_run.Display_Height - 900 + 500)
            self.menu_run.draw_text("And reluctantly,", 20, self.menu_run.Display_Width / 2, self.menu_run.Display_Height - 900+ 540)
            self.menu_run.draw_text("Alex Pearce", 20, self.menu_run.Display_Width / 2, self.menu_run.Display_Height - 900 + 580)
            self.blit_screen()
class CustoMenu(Menu1):
    def __init__(self, menu_run):
        Menu1.__init__(self, menu_run)
        self.state = 'one'
        self.onex, self.oney = (self.menu_run.Display_Width/2 + 173, self.menu_run.Display_Height - 860 +330)
        self.twox, self.twoy = (self.menu_run.Display_Width/2 + 173, self.menu_run.Display_Height - 840+330)
        self.threex, self.threey = (self.menu_run.Display_Width/2 + 173, self.menu_run.Display_Height - 820+330)
        self.fourx, self.foury = (self.menu_run.Display_Width / 2 + 173, self.menu_run.Display_Height - 800+330)
        self.fivex, self.fivey = (self.menu_run.Display_Width / 2 + 173, self.menu_run.Display_Height - 780+330)
        self.sixx, self.sixy = (self.menu_run.Display_Width / 2 + 173, self.menu_run.Display_Height - 760+330)
        self.Ax, self.Ay = (self.menu_run.Display_Width / 2 + 95, self.menu_run.Display_Height - 700+330)
        self.Bx, self.By = (self.menu_run.Display_Width / 2 + 95, self.menu_run.Display_Height - 675+360)
        self.changeNamesx, self.changeNamesy = (self.menu_run.Display_Width / 2 + 130, self.menu_run.Display_Height - 575+300)
        self.cursor_rect.midtop = (self.menu_run.Display_Width/2 + 173, self.oney)

        self.boardType = 1
        self.playerArr = ['Miss Scarlet','Mrs White','Colonel Mustard','Reverend Green','Professor Plum','Mrs Peacock']

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.menu_run.check_events()
            self.input_check()
            # if self.menu_run.START_KEY or self.menu_run.BACK_KEY:
            #     self.menu_run.curr_menu = self.menu_run.main_menu
            #     self.run_display = False
            self.menu_run.display.fill(self.menu_run.BLACK)
            self.menu_run.display.blit(self.background_image, [-530, 0])
            self.menu_run.draw_text("Customisation", 40, self.menu_run.Display_Width / 2, self.menu_run.Display_Height - 900+330)
            self.menu_run.draw_text("choose number of players:", 20, self.menu_run.Display_Width / 2, self.menu_run.Display_Height - 860+310)
            self.menu_run.draw_text("1", 20, self.menu_run.Display_Width/2 + 150, self.oney)
            self.menu_run.draw_text("2", 20, self.menu_run.Display_Width / 2 + 150, self.twoy)
            self.menu_run.draw_text("3", 20, self.menu_run.Display_Width / 2 + 150, self.threey)
            self.menu_run.draw_text("4", 20, self.menu_run.Display_Width / 2 + 150, self.foury)
            self.menu_run.draw_text("5", 20, self.menu_run.Display_Width / 2 + 150, self.fivey)
            self.menu_run.draw_text("6", 20, self.menu_run.Display_Width / 2 + 150, self.sixy)
            self.menu_run.draw_text("Board type:", 20, self.menu_run.Display_Width / 2, self.menu_run.Display_Height - 700+290)
            self.menu_run.draw_text("A", 20, self.menu_run.Display_Width / 2 + 70, self.Ay)
            self.menu_run.draw_text("B", 20, self.menu_run.Display_Width / 2 + 70, self.By)
            self.menu_run.draw_text("change player names", 20, self.menu_run.Display_Width / 2, self.changeNamesy)
            self.draw_cursor()
            self.blit_screen()

    def input_check(self):
        if self.menu_run.BACK_KEY:
            self.menu_run.curr_menu = self.menu_run.options
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
            elif self.state == 'changeNames':
                self.cursor_rect.midtop = (self.changeNamesx + 30, self.changeNamesy)
                self.state = 'one'
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
                self.playerArr = ['', False, False, False, False, False]
                print(self.playerNum)
                self.state = 'A'
                self.cursor_rect.midtop = (self.Ax, self.Ay)
            elif self.state == 'two':
                self.playerNum = 2
                self.playerArr = ['', '', False, False, False, False]
                print(self.playerNum)
                self.state = 'A'
                self.cursor_rect.midtop = (self.Ax, self.Ay)
            elif self.state == 'three':
                self.playerNum = 3
                self.playerArr = ['', '', '', False, False, False]
                print(self.playerNum)
                self.state = 'A'
                self.cursor_rect.midtop = (self.Ax, self.Ay)
            elif self.state == 'four':
                self.playerNum = 4
                self.playerArr = ['', '', '', '', False, False]
                print(self.playerNum)
                self.state = 'A'
                self.cursor_rect.midtop = (self.Ax, self.Ay)
            elif self.state == 'five':
                self.playerNum = 5
                self.playerArr = ['', '', '', '', '', False]
                print(self.playerNum)
                self.state = 'A'
                self.cursor_rect.midtop = (self.Ax, self.Ay)
            elif self.state == 'six':
                self.playerNum = 6
                self.playerArr = ['', '', '', '', '', '']
                print(self.playerNum)
                self.state = 'A'
                self.cursor_rect.midtop = (self.Ax, self.Ay)
            elif self.state == 'A':
                self.boardType = 1
                #print(Menu1.getBoardType(self))
                self.cursor_rect.midtop = (self.changeNamesx+ 30, self.changeNamesy)
                self.state = 'changeNames'
            elif self.state == 'B':
                self.boardType = 2
                #print(Menu1.getBoardType(self))
                self.cursor_rect.midtop = (self.changeNamesx+ 30, self.changeNamesy)
                self.state = 'changeNames'
            elif self.state == 'changeNames':
                self.menu_run.curr_menu = self.menu_run.plName
            self.run_display = False


class PlayerNamesMenu(Menu1):
    def __init__(self, menu_run, CustoMenu):
        Menu1.__init__(self, menu_run)
        self.CustoMenu = CustoMenu
        self.plNum = 1
        self.state = 'pl1'
        self.plNameEntry = ''
        #'Miss Scarlet', 'Mrs White', 'Colonel Mustard', 'Reverend Green', 'Professor Plum', 'Mrs Peacock'
        self.name1 = 'Miss Scarlet'
        self.name2 = 'Mrs White'
        self.name3 = 'Colonel Mustard'
        self.name4 = 'Reverend Green'
        self.name5 = 'Professor Plum'
        self.name6 = 'Mrs Peacock'
        self.endMsg = ''
        self.base_font = pygame.font.Font(None, 20)
                                #x,y coordinates. size of rect
        self.inputRect1 = pygame.Rect(self.menu_run.Display_Width / 2 -50, self.menu_run.Display_Height - 450, 140, 32)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.menu_run.check_events()
            self.input_check()
            self.menu_run.display.fill(self.menu_run.BLACK)
            self.menu_run.display.blit(self.background_image, [-530, 0])
            self.menu_run.draw_text("Player Names", 40, self.menu_run.Display_Width / 2, self.menu_run.Display_Height - 500)
            self.menu_run.draw_text(("Enter Player " + str(self.plNum) + " name"), 20, self.menu_run.Display_Width / 2, self.menu_run.Display_Height - 465)
            self.menu_run.draw_text(self.name1, 20, self.menu_run.Display_Width / 2, self.menu_run.Display_Height - 780+500)
            self.menu_run.draw_text(self.name2, 20, self.menu_run.Display_Width / 2, self.menu_run.Display_Height - 750+500)
            self.menu_run.draw_text(self.name3, 20, self.menu_run.Display_Width / 2, self.menu_run.Display_Height - 720+500)
            self.menu_run.draw_text(self.name4, 20, self.menu_run.Display_Width / 2, self.menu_run.Display_Height - 690+500)
            self.menu_run.draw_text(self.name5, 20, self.menu_run.Display_Width / 2, self.menu_run.Display_Height - 660+500)
            self.menu_run.draw_text(self.name6, 20, self.menu_run.Display_Width / 2, self.menu_run.Display_Height - 630+500)
            self.menu_run.draw_text(self.endMsg, 20, self.menu_run.Display_Width / 2, self.menu_run.Display_Height - 600+500)
            pygame.draw.rect(self.menu_run.display, (255, 0, 0), self.inputRect1, 2)
            text_surface1 = self.base_font.render(self.plNameEntry, True, (255, 255, 255))
            self.menu_run.display.blit(text_surface1, (self.inputRect1.x +5, self.inputRect1.y + 5))
            self.inputRect1.w = max(100, text_surface1.get_width() + 10)
            self.blit_screen()

    def input_check(self):
        if self.menu_run.START_KEY and self.state == 'pl1':
            self.name1 = self.plNameEntry[:-1]
            self.CustoMenu.playerArr[0] = self.name1
            self.plNameEntry = ''
            if self.CustoMenu.playerNum == 1:
                self.run_display = False
                self.menu_run.curr_menu = self.menu_run.custo
            else:
                self.plNum = 2
                self.state = 'pl2'
        elif self.menu_run.START_KEY and self.state == 'pl2':
            self.name2 = self.plNameEntry[:-1]
            self.CustoMenu.playerArr[1] = self.name2
            self.plNameEntry = ''
            if self.CustoMenu.playerNum  == 2:
                self.run_display = False
                self.menu_run.curr_menu = self.menu_run.custo
            else:
                self.plNum = 3
                self.state = 'pl3'
        elif self.menu_run.START_KEY and self.state == 'pl3':
            self.name3 = self.plNameEntry[:-1]
            self.CustoMenu.playerArr[2] = self.name3
            self.plNameEntry = ''
            if self.CustoMenu.playerNum  == 3:
                self.run_display = False
                self.menu_run.curr_menu = self.menu_run.custo
            else:
                self.plNum = 4
                self.state = 'pl4'
        elif self.menu_run.START_KEY and self.state == 'pl4':
            self.name4 = self.plNameEntry[:-1]
            self.CustoMenu.playerArr[3] = self.name4
            self.plNameEntry = ''
            if self.CustoMenu.playerNum == 4:
                self.run_display = False
                self.menu_run.curr_menu = self.menu_run.custo
            else:
                self.plNum = 5
                self.state = 'pl5'
        elif self.menu_run.START_KEY and self.state == 'pl5':
            self.name5 = self.plNameEntry[:-1]
            self.CustoMenu.playerArr[4] = self.name5
            self.plNameEntry = ''
            if self.CustoMenu.playerNum  == 5:
                self.run_display = False
                self.menu_run.curr_menu = self.menu_run.custo
            else:
                self.plNum = 6
                self.state = 'pl6'
        elif self.menu_run.START_KEY and self.state == 'pl6':
            self.name6 = self.plNameEntry[:-1]
            self.CustoMenu.playerArr[5] = self.name6
            self.endMsg = 'confirm and exit?'
            self.state ='end'

            # self.menu_run.curr_menu = self.menu_run.custo

        elif self.menu_run.START_KEY and self.state == 'end':
            self.run_display = False
            self.menu_run.curr_menu = self.menu_run.custo
