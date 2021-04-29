import pygame as pg
import Deck
import suspect_cards
import room_cards
import weapon_cards
import Player as player
import dropdown
import button

class Guess:
    def __init__(self, screen, players):
        self.screen = screen
        self.players = players
        self.optionRoom = "ROOM"
        self.optionWea = "WEAPON"
        self.optionSus = "SUSPECT"
        self.playerHandover = ""


#this function is to be used when someone has made a guess. the function goes around the players looking for the
    #guessed cards. once matching cards have been found it will either automatically show the card to the player
    #or give the player who has multiple of the cards the choice of which to choose
    def check_for_match(self, list1, list2, list3, screen):
        self.screen = screen
        check = False
        cards = []
        option1 = list1.active_option #the dropdown for room cards
        option2 = list2.active_option # the dropdown for weapon cards
        option3 = list3.active_option # the dropdown for suspect cards
        while check == False:
            for player in self.players: # going through all the players
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
                            check = True
                            #this will draw up some buttons for this player to show their card to the original player
                            self.playerHandover = player
                            self.optionRoom = option1
                            self.optionWea = option2
                            self.buttonRoom.draw(self.screen)
                            self.buttonWea.draw(self.screen)
                            self.buttonPla.draw(self.screen)
                        elif hand == option2 and hand == option3:
                            cards = cards + option3
                            cards = cards + option2
                            check = True
                            self.playerHandover = player
                            self.optionSus = option3
                            self.optionWea = option2
                            self.buttonSus.draw(self.screen)
                            self.buttonWea.draw(self.screen)
                            self.buttonPla.draw(self.screen)
                        elif hand == option1 and hand == option3:
                            cards = cards + option1
                            cards = cards + option3
                            check = True
                            self.playerHandover = player
                            self.optionRoom = option1
                            self.optionSus = option3
                            self.buttonRoom.draw(self.screen)
                            self.buttonSus.draw(self.screen)
                            self.buttonPla.draw(self.screen)
                        elif hand == option1 and hand == option2 and hand == option3:
                            cards = cards + option1
                            cards = cards + option2
                            cards = cards + option3
                            check = True
                            self.playerHandover = player
                            self.optionRoom = option1
                            self.optionWea = option2
                            self.optionSus = option3
                            self.buttonRoom.draw(self.screen)
                            self.buttonWea.draw(self.screen)
                            self.buttonSus.draw(self.screen)
                            self.buttonPla.draw(self.screen)
                    else:# thid auto shows card at the cluedo space on board
                        if hand == option1:
                            cards = cards + option1
                            check = True
                            self.optionRoom = option1
                            self.buttonRoom.draw(self.screen)
                            self.buttonSeen.draw(self.screen)
                        if hand == option2:
                            cards = cards + option2
                            check = True
                            self.buttonWea.draw(self.screen)
                            self.buttonSeen.draw(self.screen)
                        if hand == option3:
                            cards = cards + option3
                            check = True
                            self.buttonSus.draw(self.screen)
                            self.buttonSeen.draw(self.screen)
                else:# no one had the cards chosen or player did not choose cards to guess
                    check = True
                    self.buttonNoToSee.draw(self.screen)
        return cards # next turn, no cards shown

    d = Deck.Deck()
    pg.init()
    font = pg.font.SysFont(None, 30)

#this is the function to be used to run the class
    def screenDisplay(self, player):
        clock = pg.time.Clock()
        
        sus = suspect_cards.Suspect_cards
        room = room_cards.Room_cards
        wea = weapon_cards.Weapon_cards
        COLOR_INACTIVE = (100, 80, 255)
        COLOR_ACTIVE = (100, 200, 255)
        COLOR_LIST_INACTIVE = (255, 100, 100)
        COLOR_LIST_ACTIVE = (255, 150, 150)

        COLOR_ACTIVE_CONFIRM = (0, 200, 0)
        COLOR_INACTIVE_CONFIRM = (100, 80, 255)

#suspect dropdown menu
        list1 = dropdown.DropDown(
            [COLOR_INACTIVE, COLOR_ACTIVE],
            [COLOR_LIST_INACTIVE, COLOR_LIST_ACTIVE],
            650, 100, 200, 50,
            pg.font.SysFont(None, 30),
            "Select Suspect", #sus.getNames(sus))
             player.getRoom()) #this should get the player location and auto select it for the dropdown
#weapon dropdown menu
        list2 = dropdown.DropDown(
            [COLOR_INACTIVE, COLOR_ACTIVE],
            [COLOR_LIST_INACTIVE, COLOR_LIST_ACTIVE],
            375, 100, 200, 50,
            pg.font.SysFont(None, 30),
            "Select Weapon", wea.getNames(wea))
#room dropdown menu
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

        #this button shows the guessed room card
        buttonRoom = button.Button(
            COLOR_INACTIVE,
            100, 300,
            150, 50,
            "" + self.optionRoom
        )

        # this button shows the guessed weapon card
        buttonWea = button.Button(
            COLOR_INACTIVE,
            375, 300,
            150, 50,
            "" + self.optionWea
        )

        # this button shows the guessed suspect card
        buttonSus = button.Button(
            COLOR_INACTIVE,
            650, 300,
            150, 50,
            "" + self.optionSus
        )

        # this button shows which player needs to choose a card to show
        buttonPla = button.Button(
            COLOR_INACTIVE,
            400, 200,
            200, 50,
            "Player " + self.playerHandover + "Choose a card to display"
        )

        # this button confirms the player has seen the matched guess card
        buttonSeen = button.Button(
            COLOR_INACTIVE,
            600, 600,
            150, 50,
            "I have seen card"
        )

        # this button confirms the player understands no one had a match
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

            background_image = pg.image.load("../Image/clue_back.png")

            self.screen.fill((102, 0, 102))

            self.screen.blit(background_image, [0, 0])

            list1.draw(self.screen)
            list2.draw(self.screen)
            list3.draw(self.screen)
            button1.draw(self.screen)
            button1.event(self.screen, event)
            buttonWea.eventChoose(self.screen, event)
            buttonPla.eventChoose(self.screen, event)
            buttonRoom.eventChoose(self.screen, event)
            buttonSeen.event(self.screen)
            buttonNoToSee.event(self.screen)

            if button1.event(self.screen, event) == True:
                self.check_for_match(self, list1, list2, list3, self.screen)

            if buttonSus.eventChoose(self.screen,event) == True:
                buttonSeen.draw(self.screen)
            if buttonWea.eventChoose(self.screen,event) == True:
                buttonSeen.draw(self.screen)
            if buttonRoom.eventChoose(self.screen,event) == True:
                buttonSeen.draw(self.screen)

            if buttonNoToSee(self.screen, event) == True:
                run = False
            if buttonSeen(self.screen, event) == True:
                run = False


            pg.display.flip()


#Guess.screenDisplay(Guess)
