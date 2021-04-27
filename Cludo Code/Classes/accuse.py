import pygame as pg
import Deck
import suspect_cards
import room_cards
import weapon_cards
import Player as player
import dropdown
import button2


class Accuse:
    def __init__(self, player1, envelope):
        self.player = player1
        self.envelope = envelope

    pg.init()
    font = pg.font.SysFont(None, 30)


    def check_envolope(self, button1, list1, list2, list3):
      #  player.Player.accuse(player)
        if button1.pressed == True:
            count = 0
            for card in self.envelope:
                if (card.getName() == list1.active_option or card.getName() == list2.active_option or card.getName() == list3.active_option):
                    count = count + 1
                else:
                    #go back to game next players turn, things did not match
                    pass
        if count == 3:
            player.Player.setWin(player)


    # def ifConfirmed(self):
    #     #return to game screen?
    #     pass

    def displayScreen(self):
        sus = suspect_cards.Suspect_cards
        room = room_cards.Room_cards
        wea = weapon_cards.Weapon_cards

        COLOR_INACTIVE = (100, 80, 255)
        COLOR_ACTIVE = (100, 200, 255)
        COLOR_LIST_INACTIVE = (255, 100, 100)
        COLOR_LIST_ACTIVE = (255, 150, 150)

        COLOR_ACTIVE_CONFIRM = (0, 200, 0)
        COLOR_INACTIVE_CONFIRM = (100, 80, 255)
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
        clock = pg.time.Clock()
        screen = pg.display.set_mode((960, 950))
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

            if button1.event(screen, event) == True:
                self.check_envolope(button1, list1, list2, list3)

            pg.display.flip()



# Accuse.displayScreen(Accuse)