import pygame as pg
import Deck
import suspect_cards
import room_cards
import weapon_cards
import Player as player
import dropdown
import button

class Guess:
    def __init__(self, players):
        self.players = players
        self.optionRoom = "ROOM"
        self.optionWea = "WEAPON"
        self.optionSus = "SUSPECT"
        self.playerHandover = ""



    def check_for_match(self, list1, list2, list3, screen):
        check = False
        cards = []
        option1 = list1.active_option
        option2 = list2.active_option
        option3 = list3.active_option
        while check == False:
            for player in self.players:
                hand = player.getCards()
                #this if statement checks if the next players have the cards being guessed
                if hand == option1 or hand == option2 or hand == option3:
                    if hand == option1 and hand == option2 or hand == option2 \
                            and hand == option3 or hand == option1 and hand == option3 \
                            or hand == option1 and hand == option2 and hand == option3:
                        #if 2 or more cards are in the next players hand
                        if hand == option1 and hand == option2:
                            cards = cards + option1
                            cards = cards + option2
                            check = True #todo need to pass turn over to that player
                            self.playerHandover = player
                            self.optionRoom = option1
                            self.optionWea = option2
                            self.buttonRoom.draw(screen)
                            self.buttonWea.draw(screen)
                            self.buttonPla.draw(screen)
                        elif hand == option2 and hand == option3:
                            cards = cards + option3
                            cards = cards + option2
                            check = True
                            self.playerHandover = player
                            self.optionSus = option3
                            self.optionWea = option2
                            self.buttonSus.draw(screen)
                            self.buttonWea.draw(screen)
                            self.buttonPla.draw(screen)
                        elif hand == option1 and hand == option3:
                            cards = cards + option1
                            cards = cards + option3
                            check = True
                            self.playerHandover = player
                            self.optionRoom = option1
                            self.optionSus = option3
                            self.buttonRoom.draw(screen)
                            self.buttonSus.draw(screen)
                            self.buttonPla.draw(screen)
                        elif hand == option1 and hand == option2 and hand == option3:
                            cards = cards + option1
                            cards = cards + option2
                            cards = cards + option3
                            check = True
                            self.playerHandover = player
                            self.optionRoom = option1
                            self.optionWea = option2
                            self.optionSus = option3
                            self.buttonRoom.draw(screen)
                            self.buttonWea.draw(screen)
                            self.buttonSus.draw(screen)
                            self.buttonPla.draw(screen)
                    else:# auto show card at the cluedo space on board
                        if hand == option1:
                            cards = cards + option1
                            check = True
                            self.optionRoom = option1
                            self.buttonRoom.draw(screen)
                            self.buttonSeen.draw(screen)
                        if hand == option2:
                            cards = cards + option2
                            check = True
                            self.buttonWea.draw(screen)
                            self.buttonSeen.draw(screen)
                        if hand == option3:
                            cards = cards + option3
                            check = True
                            self.buttonSus.draw(screen)
                            self.buttonSeen.draw(screen)
                else:# no one had the cards chosen or player did not choose cards to guess
                    check = True
                    self.buttonNoToSee.draw(screen)
        return cards #todo next turn, no cards shown

    d = Deck.Deck()
    pg.init()
    font = pg.font.SysFont(None, 30)

    def screenDisplay(self, player):
        clock = pg.time.Clock()
        screen = pg.display.set_mode((960, 950))
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
            "Select Suspect", #sus.getNames(sus))
             player.getRoom()) #this should get the player location and auto select it for the dropdown

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

        #this button is the guess button
        button1 = button.Button(
            COLOR_INACTIVE,
                405, 600,
                150, 50,
                "Guess")

        buttonRoom = button.Button(
            COLOR_INACTIVE,
            300, 300,
            150, 50,
            "" + self.optionRoom
        )

        buttonWea = button.Button(
            COLOR_INACTIVE,
            400, 300,
            150, 50,
            "" + self.optionWea
        )

        buttonSus = button.Button(
            COLOR_INACTIVE,
            500, 300,
            150, 50,
            "" + self.optionSus
        )

        buttonPla = button.Button(
            COLOR_INACTIVE,
            400, 200,
            200, 50,
            "Player " + self.playerHandover + "Choose a card to display"
        )

        buttonSeen = button.Button(
            COLOR_INACTIVE,
            600, 600,
            150, 50,
            "I have seen card"
        )

        buttonNoToSee = button.Button(
            COLOR_INACTIVE,
            600, 600,
            150, 50,
            "No card to be shown, continue"
        )

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
            buttonWea.eventChoose(screen, event)
            buttonPla.eventChoose(screen, event)
            buttonRoom.eventChoose(screen, event)
            buttonSeen.event(screen)
            buttonNoToSee.event(screen)

            if button1.event(screen, event) == True:
                self.check_for_match(self, list1, list2, list3, screen)

            if buttonSus.eventChoose(screen,event) == True:
                buttonSeen.draw(screen)
            if buttonWea.eventChoose(screen,event) == True:
                buttonSeen.draw(screen)
            if buttonRoom.eventChoose(screen,event) == True:
                buttonSeen.draw(screen)

            if buttonNoToSee(screen, event) == True:
                run = False
            if buttonSeen(screen, event) == True:
                run = False


            pg.display.flip()


Guess.screenDisplay(Guess)