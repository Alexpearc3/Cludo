import pygame as pg
import Deck
import suspect_cards
import room_cards
import weapon_cards
import Player as player
import dropdown
import button2
import winScreen
import loseScreen


class Accuse:
    def __init__(self,  player1, envelope):

        self.player = player1
        self.envelope = envelope
        self.lost = False

    pg.init()
    font = pg.font.SysFont(None, 30)

    #this function compares the cards in the envelope to the cards the player has accused
    def check_envolope(self, button1, list1, list2, list3, screen):
        if button1.pressed == True:
            count = 0
            for card in self.envelope:
                if (card.getName() == list1.active_option or card.getName() == list2.active_option or card.getName() == list3.active_option):
                    count = count + 1
                else:
                    #go back to game next players turn, things did not match
                    self.lost = True
                    self.player.accuse()
                    loseScreen.loseScreen.has_lost(loseScreen)
        if count == 3:
            player.Player.setWin(player)
            #the player is taken to winscreen
            winScreen.winScreen.has_won(winScreen)

#this shows when the player made a wrong accusation
    def lostAccuse(self, screen):
        font = pg.font.Font(None, 60)
        text = font.render('Your accusation was wrong', True, (102, 0, 102), (0, 128, 128))
        textRect = text.get_rect()
        textRect.center = (475, 200)
        screen.blit(text, textRect)

#similar to guess, this also runs the class and displays the screen
    def displayScreen(self):
        sus = suspect_cards.Suspect_cards
        room = room_cards.Room_cards
        wea = weapon_cards.Weapon_cards
        screen = pg.display.set_mode([960, 950])

        COLOR_INACTIVE = (100, 80, 255)
        COLOR_ACTIVE = (100, 200, 255)
        COLOR_LIST_INACTIVE = (255, 100, 100)
        COLOR_LIST_ACTIVE = (255, 150, 150)

        COLOR_ACTIVE_CONFIRM = (0, 200, 0)
        COLOR_INACTIVE_CONFIRM = (100, 80, 255)
        # suspect dropdown menu
        list1 = dropdown.DropDown(
            [COLOR_INACTIVE, COLOR_ACTIVE],
            [COLOR_LIST_INACTIVE, COLOR_LIST_ACTIVE],
            650, 100, 200, 50,
            pg.font.SysFont(None, 30),
            "Select Suspect", sus.getNames(sus))
        # weapon dropdown menu
        list2 = dropdown.DropDown(
            [COLOR_INACTIVE, COLOR_ACTIVE],
            [COLOR_LIST_INACTIVE, COLOR_LIST_ACTIVE],
            375, 100, 200, 50,
            pg.font.SysFont(None, 30),
            "Select Weapon", wea.getNames(wea))
        # room dropdown menu
        list3 = dropdown.DropDown(
            [COLOR_INACTIVE, COLOR_ACTIVE],
            [COLOR_LIST_INACTIVE, COLOR_LIST_ACTIVE],
            100, 100, 200, 50,
            pg.font.SysFont(None, 30),
            "Select Room", room.getNames(room))
        # this button is the guess button
        button1 = button2.Button(
            COLOR_INACTIVE,
            405, 600,
            150, 50,
            "Accuse")
        run = True
        clock = pg.time.Clock()
        while run:
            clock.tick(30)
            pg.display.update()

            event_list = pg.event.get()
            for event in event_list:
                if event.type == pg.QUIT:
                    run = False

#these change the top of dropdown to the selected options
            selected_option = list1.update(event_list)
            if selected_option >= 0:
                list1.main = list1.options[selected_option]

            selected_option = list2.update(event_list)
            if selected_option >= 0:
                list2.main = list2.options[selected_option]

            selected_option = list3.update(event_list)
            if selected_option >= 0:
                list3.main = list3.options[selected_option]


            background_image = pg.image.load("../Image/accuseBack1.png")

            screen.fill((102, 0, 102))
            screen.blit(background_image, [0, 0])

            if self.lost == True:
                self.lostAccuse(screen)

            list1.draw(screen)
            list2.draw(screen)
            list3.draw(screen)
            button1.draw(screen)
            button1.event(screen, event)
#calls check envelope when the player has made an accusation

            if button1.event(screen, event) == True:
                self.check_envolope(button1, list1, list2, list3, screen)

            pg.display.flip()



#Accuse.displayScreen(Ac cuse)
