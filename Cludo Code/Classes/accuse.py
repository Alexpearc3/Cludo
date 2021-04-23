import pygame as pg
import Deck
import suspect_cards
import room_cards
import weapon_cards
import Player as player
import dropdown
import button


    # def __init__(self, text, pos, font, bg="black", feedback=""):
    #     self.x, self.y = pos
    #     self.font = pg.font.SysFont(None, font)
    #     if feedback == "":
    #         self.feedback = "text"
    #     else:
    #         self.feedback = feedback
    #     self.change_text(text, bg)
    #
    # d = Deck.Deck()
    # sus = suspect_cards.Suspect_cards
    # room = room_cards.Room_cards
    # wea = weapon_cards.Weapon_cards
    # pg.init()
    # clock = pg.time.Clock()
    # screen = pg.display.set_mode((960, 950))
    #
    # font = pg.font.SysFont(None, 30)
    #
    # COLOR_INACTIVE = (100, 80, 255)
    # COLOR_ACTIVE = (100, 200, 255)
    # COLOR_LIST_INACTIVE = (255, 100, 100)
    # COLOR_LIST_ACTIVE = (255, 150, 150)
    #
    # COLOR_ACTIVE_CONFIRM = (0, 200, 0)
    # COLOR_INACTIVE_CONFIRM = (100, 80, 255)
    #
    # def change_text(self, text, bg="black"):
    #     self.text = self.font.render(text, 1, pg.Color("Black"))
    #     self.size = self.text.get_size()
    #     self.surface = pg.Surface(self.size)
    #     self.surface.fill(bg)
    #     self.surface.blit(self.text, (0, 0))
    #     self.rect = pg.Rect(self.x, self.y, self.size[0], self.size[1])
    #
    # def show(self, screen):
    #     msg =
    #     screen.blit(.surface, (self.x, self.y))
    #
    # def click(self, event):
    #     x, y = pg.mouse.get_pos()
    #     if event.type == pg.MOUSEBUTTONDOWN:
    #         if pg.mouse.get_pressed()[0]:
    #             if self.rect.collidepoint(x, y):
    #                 self.change_text(self.feedback, bg="red")



class Guess:
    def __init__(self):
       pass

    d = Deck.Deck()
    sus = suspect_cards.Suspect_cards
    room = room_cards.Room_cards
    wea = weapon_cards.Weapon_cards
    pg.init()
    clock = pg.time.Clock()
    screen = pg.display.set_mode((960, 950))

    font = pg.font.SysFont(None, 30)

    COLOR_INACTIVE = (100, 80, 255)
    COLOR_ACTIVE = (100, 200, 255)
    COLOR_LIST_INACTIVE = (255, 100, 100)
    COLOR_LIST_ACTIVE = (255, 150, 150)

    COLOR_ACTIVE_CONFIRM = (0, 200, 0)
    COLOR_INACTIVE_CONFIRM = (100, 80, 255)

    def check_envolope(self):
        check = False
        player.Player.accuse(player)
        if (Deck.getEnvelope(Deck) == list1.active_option, list2.active_option, list3.active_option):
            player.Player.setWin(player)
            check = True
        else:
            check = True
            pass #go back to game next players turn
        return check


    list1 = dropdown.DropDown(
        [COLOR_INACTIVE, COLOR_ACTIVE],
        [COLOR_LIST_INACTIVE, COLOR_LIST_ACTIVE],
        500, 50, 200, 50,
        pg.font.SysFont(None, 30),
        "Select Suspect", sus.getNames(sus))

    list2 = dropdown.DropDown(
        [COLOR_INACTIVE, COLOR_ACTIVE],
        [COLOR_LIST_INACTIVE, COLOR_LIST_ACTIVE],
        275, 50, 200, 50,
        pg.font.SysFont(None, 30),
        "Select Weapon", wea.getNames(wea))

    list3 = dropdown.DropDown(
        [COLOR_INACTIVE, COLOR_ACTIVE],
        [COLOR_LIST_INACTIVE, COLOR_LIST_ACTIVE],
        50, 50, 200, 50,
        pg.font.SysFont(None, 30),
        "Select Room", room.getNames(room))

    button1 = button.Button(
        COLOR_INACTIVE,
        500, 500,
        100, 50,
        "Accuse")

        # "Accuse",
        # (600, 700),
        # font=50,
        # bg="blue",
        # feedback="Choice Confirmed")


    run = True
    while run:
        clock.tick(30)
        pg.display.update()

        event_list = pg.event.get()
        for event in event_list:
            if event.type == pg.QUIT:
                run = False

        selected_option = list1.update(event_list)
        if selected_option >= 0:
            list1.main = list1.options[selected_option]

        selected_option = list2.update(event_list)
        if selected_option >= 0:
            list2.main = list2.options[selected_option]

        selected_option = list3.update(event_list)
        if selected_option >= 0:
            list3.main = list3.options[selected_option]


        screen.fill((102, 0, 102))
        list1.draw(screen)
        list2.draw(screen)
        list3.draw(screen)
        button1.draw(screen)
        button1.event(event)
        pg.display.flip()

    pg.quit()
    exit()
