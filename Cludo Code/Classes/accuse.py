import pygame as pg
import Deck
import suspect_cards
import room_cards
import weapon_cards
import Player as player
import dropdown
import button2


class Accuse:
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
        if (Deck.getEnvelope(Deck) == self.list1.active_option, self.list2.active_option, self.list3.active_option):
            player.Player.setWin(player)
            check = True
        else:
            check = True
            pass #go back to game next players turn
        return check

    def set_chosen_cards(self):
        room = None
        weapon = None
        suspect = None
        if button2.Button.event() == True:
            room = self.list1.active_option
            weapon = self.list2.active_option
            suspect = self.list3.active_option
        return room, weapon, suspect

    list1 = dropdown.DropDown(
        [COLOR_INACTIVE, COLOR_ACTIVE],
        [COLOR_LIST_INACTIVE, COLOR_LIST_ACTIVE],
        650, 100, 200, 50,
        pg.font.SysFont(None, 30),
        "Select Suspect", sus.getNames(sus))

    list2 = dropdown.DropDown(
        [COLOR_INACTIVE, COLOR_ACTIVE],
        [COLOR_LIST_INACTIVE, COLOR_LIST_ACTIVE],
        375, 100, 200, 50,
        pg.font.SysFont(None, 30),
        "Select Weapon", wea.getNames(wea))

    list3 = dropdown.DropDown(
        [COLOR_INACTIVE, COLOR_ACTIVE],
        [COLOR_LIST_INACTIVE, COLOR_LIST_ACTIVE],
        100, 100, 200, 50,
        pg.font.SysFont(None, 30),
        "Select Room", room.getNames(room))

    button1 = button2.Button(
        COLOR_INACTIVE,
        405, 600,
        150, 50,
        "Accuse")



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
        button1.event(screen, event)
        pg.display.flip()

    pg.quit()
    exit()
