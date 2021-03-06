import pygame
import room_cards
import suspect_cards
import weapon_cards


class Notepad:
    lines = []

    def __init__(self):
        self.lines = []
        self.general_list = []
        # background
        self.notepad_background_img = "../Image/notepad_background 2.png"
        self.notepad_background = pygame.image.load(self.notepad_background_img)

        # initialise an object of room_cards and use the method getNames to get room_list
        room_list = room_cards.Room_cards().getNames()  # name of file and name of class
        suspect_list = suspect_cards.Suspect_cards().getNames()  # name of file and name of class
        weapon_list = weapon_cards.Weapon_cards().getNames()  # name of file and name of class

        # create a list includes suspects, rooms, weapons
        self.general_list += suspect_list + weapon_list + room_list
        self.general_list.insert(0, 'Suspect')
        self.general_list.insert(len(suspect_list) + 1, 'Weapon')
        self.general_list.insert(-len(room_list), 'Room')

    def initNotepad(self):
        # initializing the constructor
        pygame.init()

        # size of window
        x = 960
        y = 960
        screen = pygame.display.set_mode((x, y))

        # title of window
        pygame.display.set_caption('Notepad')
        # icon of window
        # .. go back 1 time directory
        # ... go back 2 time directory
        icon_img = "../Image/Clue_logo.png"
        icon = pygame.image.load(icon_img)
        pygame.display.set_icon(icon)

        self.notepad(screen)

    def notepad(self, screenx):
        '''
             :param screenx: displaying screen of window
             :return: screen
             '''
        red = (255, 0, 0)
        flag = True
        while flag:
            screen = screenx
            screen.blit(self.notepad_background, (960 / 3.5, 0))
            # screen.fill(self.notepad_background)
            screen = self.drawNotePad(self.lines, screen)

            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    # pygame.quit()
                    flag = False
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    spacing = 154
                    Mouse = pygame.mouse.get_pos()
                    for item in self.general_list:
                        if ev.button == 1 and spacing - 10 <= Mouse[1] <= spacing + 10 and not (
                                item == 'Mrs Peacock' or item == 'Knife'):
                            check = True
                            for ln in self.lines:
                                x,xSpacing,z,q = ln
                                if xSpacing == spacing:
                                    check = False
                            if check:
                                self.lines.append([75 + 280, spacing, 155, 2])
                        if ev.button == 3 and spacing - 10 <= Mouse[1] <= spacing + 10 and not (
                                item == 'Mrs Peacock' or item == 'Knife'):
                            if (len(self.lines)) != 0:
                                for j in range(len(self.lines)):
                                    try:
                                        x, Xspacing, y, z = self.lines[j]
                                        if Xspacing == spacing:
                                            print(j)
                                            self.lines.pop(j)
                                    except:
                                        p = ""

                        spacing += 29
                pygame.display.update()

    def drawNotePad(self, lines, screen):
        '''
        :param lines: list
        :param screen: screen of the game window
        :return:screen
        '''
        pygame.display.init()
        # define the RGB value
        gray = (130, 130, 130)
        red = (255, 0, 0)
        white = (255, 255, 255)
        card_category_font = pygame.font.SysFont('timesnewroman', 24, bold=1)
        card_name_font = pygame.font.SysFont('timesnewroman', 20)
        # write items on notepad
        spacing = 113
        for item in self.general_list:
            if (item == 'Suspect') or (item == 'Weapon') or (item == 'Room'):
                screen.blit(card_category_font.render(item, True, gray), (70 + 280, spacing))
            else:
                screen.blit(card_name_font.render(item, True, gray), (85 + 280, spacing))
            spacing += 29

        for line in lines:
            x, y, z, q = line
            ln = pygame.draw.rect(screen, red, [x, y, z, q])
        return screen
