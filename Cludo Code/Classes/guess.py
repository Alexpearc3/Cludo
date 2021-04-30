import pygame as pg
import Deck
import suspect_cards
import room_cards
import weapon_cards
import Player as player
import dropdown
import button

class Guess:
    def __init__(self, players, optionRoom = "Room", optionWea = "weapon", optionSus = "suspect"):
        self.players = players
        self.optionRoom = optionRoom
        self.optionWea = optionWea
        self.optionSus = optionSus
        self.playerHandover = ""
        self.failScreen = False
        self.Senario1 = False
        self.Senario2 = False
        self.Senario3 = False
        self.Senario4 = False
        self.Senario5 = False
        self.Senario6 = False
        self.Senario7 = False
        self.playerNext = player
        self.buttonSeen = False


        cardRoomImage = ""
        cardWeaImage = ""
        cardSusImage = ""


    def check_for_match(self, list1, list2, list3, screen):

        COLOR_INACTIVE = (100, 80, 255)
        COLOR_ACTIVE = (100, 200, 255)
        COLOR_LIST_INACTIVE = (255, 100, 100)
        COLOR_LIST_ACTIVE = (255, 150, 150)
        cards = 0
        hands = []
        sus = suspect_cards.Suspect_cards().getNames()
        room = room_cards.Room_cards().getNames()
        wea = weapon_cards.Weapon_cards().getNames()
        self.option1 = sus[list1.active_option]  # the dropdown for room cards
        self.option2 = wea[list2.active_option]  # the dropdown for weapon cards
        self.option3 = room[list3.active_option] # suspect cards?

        self.buttonRoom = button.Button(
            COLOR_INACTIVE,
            600, 300,
            200, 50,
            str(self.option1)
        )
        # print(str(self.optionRoom))

        # this button shows the guessed weapon card
        self.buttonWea = button.Button(
            COLOR_INACTIVE,
            350, 300,
            200, 50,
            str(self.option2)
        )

        # this button shows the guessed suspect card
        self.buttonSus = button.Button(
            COLOR_INACTIVE,
            100, 300,
            200, 50,
            str(self.option3)
        )

        # this button shows which player needs to choose a card to show
        playerz = self.playerNext
        self.buttonPla = button.Button(
            COLOR_INACTIVE,
            200, 200,
            550, 50,
            "Player " + str(self.playerNext) + " Choose a card to display"
        )

        self.buttonSeenB = button.Button(
            COLOR_INACTIVE,
            450, 700,
            250, 50,
            "I have seen card"
        )

        # this button confirms the player understands no one had a match
        self.buttonNoToSee = button.Button(
            COLOR_INACTIVE,
            600, 600,
            150, 50,
            "No card to be shown, continue"
        )

        self.check = False
        while self.check == False:
            fail = True
            for player in self.players:
                handlist = player.getCards()
                for hand in handlist:
                    print("hello")
                    print(hand.getName())
                    print(self.option1)
                    if hand.getName() == self.option1:
                        hands.append(self.option1)
                        cards = cards + 1
                    elif hand.getName() == self.option2:
                        cards = cards + 1
                        hands.append(self.option2)
                    elif hand.getName() == self.option3:
                        cards = cards + 1
                        hands.append(self.option3)
                if cards == 1:
                    print("hey")
                    if hand.getName() == self.option1:
                        self.Senario1
                    if hand.getName() == self.option2:
                        self.Senario2
                    if hand.getName() == self.option3:
                        self.Senario3
                    self.playerNext = player.getPlayerID
                    self.check = True
                    fail = False
                if cards == 2:
                    print("help")
                    if self.option1 and self.option2 in hands:
                        self.Senario6 = True
                    if self.option1 and self.option3 in hands:
                        self.Senario7 + True
                    if self.option2 and self.option3 in hands:
                        self.Senario5 = True
                    self.playerNext = player.getPlayerID()
                    self.check = True
                    fail = False
                if cards == 3:
                    print("i cry")
                    self.Senario4 = True
                    self.playerNext = player.getPlayerID()
                    self.check = True
                    fail = False
            if fail == True:
                self.failScreen = True
            self.check = True



                #this function is to be used when someone has made a guess. the function goes around the players looking for the
    #guessed cards. once matching cards have been found it will either automatically show the card to the player
    #or give the player who has multiple of the cards the choice of which to choose
    # def check_for_match(self, list1, list2, list3, screen):
    #     check = False
    #     cards = []
    #     sus = suspect_cards.Suspect_cards().getNames()
    #     room = room_cards.Room_cards().getNames()
    #     wea = weapon_cards.Weapon_cards().getNames()
    #     option1 = sus[list1.active_option] #the dropdown for room cards
    #     option2 = wea[list2.active_option] # the dropdown for weapon cards
    #     option3 = room[list3.active_option] # the dropdown for suspect cards
    #
    #     self.option1 = sus[list1.active_option]  # the dropdown for room cards
    #     self.option2 = wea[list2.active_option]  # the dropdown for weapon cards
    #     self.option3 = room[list3.active_option]  # the dropdown for suspect cards
    #
    #
    #     # cardx = sus.getCards()
    #     # for card in cardx:
    #     #     if card.getName() == option3:
    #     #         card.getImgName()
    #     #         self.cardSusImage = pg.image.load(card.getImgName())
    #     #
    #     # cardz = wea.getCards()
    #     # for card in cardz:
    #     #     if card.getName() == option2:
    #     #         card.getImgName()
    #     #         self.cardWeaImage = pg.image.load(card.getImgName())
    #     #
    #     # cardss = room.getCards()
    #     # for card in cardss:
    #     #     if card.getName() == option1:
    #     #         card.getImgName()
    #     #         self.cardRoomImage = pg.image.load(card.getImgName())
    #
    #     #cardRoomImage = pg.image.load("../Image/" + str(option1) + ".png")
    #     #cardWeaImage = pg.image.load("../Image/" + str(option2) + ".png")
    #     #cardSusImage = pg.image.load("../Image/" + str(option3) + ".png")
    #
    #     while check == False:
    #
    #         for player in self.players: # going through all the players
    #             handlist = player.getCards()
    #             for hand in handlist:
    #
    #                 #this if statement checks if the next players have the cards being guessed
    #                 if hand == option1 or hand == option2 or hand == option3:
    #                     if hand == option1 and hand == option2 or hand == option2 \
    #                             and hand == option3 or hand == option1 and hand == option3 \
    #                             or hand == option1 and hand == option2 and hand == option3:
    #                         #if 2 or more cards are in the next players hand
    #                         if hand == option1 and hand == option2:
    #                             cards = cards + option1
    #                             cards = cards + option2
    #
    #                             #this will draw up some buttons for this player to show their card to the original player
    #                             screen.blit(self.cardRoomImage, [200, 100])
    #                             screen.blit(self.cardWeaImage, [100, 100])
    #                             check = True
    #                             # self.playerHandover = player
    #                             # self.optionRoom = option1
    #                             # self.optionWea = option2
    #                             # self.buttonRoom.draw(screen)
    #                             # self.buttonWea.draw(screen)
    #                             # self.buttonPla.draw(screen)
    #                         elif hand == option2 and hand == option3:
    #                             cards = cards + option3
    #                             cards = cards + option2
    #                             screen.blit(self.cardSusImage, [200, 100])
    #                             screen.blit(self.cardWeaImage, [100, 100])
    #                             check = True
    #                             # self.playerHandover = player
    #                             # self.optionSus = option3
    #                             # self.optionWea = option2
    #                             # self.buttonSus.draw(screen)
    #                             # self.buttonWea.draw(screen)
    #                             # self.buttonPla.draw(screen)
    #                         elif hand == option1 and hand == option3:
    #                             cards = cards + option1
    #                             cards = cards + option3
    #
    #                             screen.blit(self.cardRoomImage, [200, 100])
    #                             screen.blit(self.cardSusImage, [100, 100])
    #                             check = True
    #                             # self.playerHandover = player
    #                             # self.optionRoom = option1
    #                             # self.optionSus = option3
    #                             # self.buttonRoom.draw(screen)
    #                             # self.buttonSus.draw(screen)
    #                             # self.buttonPla.draw(screen)
    #                         elif hand == option1 and hand == option2 and hand == option3:
    #                             cards = cards + option1
    #                             cards = cards + option2
    #                             cards = cards + option3
    #
    #                             screen.blit(self.cardRoomImage, [200, 100])
    #                             screen.blit(self.cardWeaImage, [100, 100])
    #                             screen.blit(self.cardSusImage, [300, 100])
    #                             check = True
    #                             # self.playerHandover = player
    #                             # self.optionRoom = option1
    #                             # self.optionWea = option2
    #                             # self.optionSus = option3
    #                             # self.buttonRoom.draw(screen)
    #                             # self.buttonWea.draw(screen)
    #                             # self.buttonSus.draw(screen)
    #                             # self.buttonPla.draw(screen)
    #                     else:# thid auto shows card at the cluedo space on board
    #                         if hand == option1:
    #                             cards = cards + option1
    #
    #                             screen.blit(self.cardRoomImage, [200, 100])
    #                             check = True
    #                             # self.optionRoom = option1
    #                             # self.buttonRoom.draw(screen)
    #                             # self.buttonSeen.draw(screen)
    #                         if hand == option2:
    #                             cards = cards + option2
    #
    #                             check = True
    #                             # self.buttonWea.draw(screen)
    #                             # self.buttonSeen.draw(screen)
    #                         if hand == option3:
    #                             cards = cards + option3
    #                             self.Senario1 = True
    #                             check = True
    #                 else:# no one had the cards chosen or player did not choose cards to guess
    #                     check = True
    #                     self.playerNext = player.getName

    #         return cards # next turn, no cards shown

    d = Deck.Deck()
    pg.init()
    font = pg.font.SysFont(None, 30)

    def showFail(self, screen):
        font = pg.font.Font(None, 60)
        text = font.render('No cards found,please exit', True, (102, 0, 102), (0, 128, 128))
        textRect = text.get_rect()
        textRect.center = (475, 200)
        screen.blit(text, textRect)

    def showSenario1(self, screen):
        screen.blit(self.cardSusImage, [200, 100])
        font = pg.font.Font(None, 60)
        text = font.render('card is shown,please exit', True, (102, 0, 102), (0, 128, 128))
        textRect = text.get_rect()
        textRect.center = (475, 200)
        screen.blit(text, textRect)

    def showSenario2(self, screen):
        screen.blit(self.cardWeaImage, [200, 100])
        font = pg.font.Font(None, 60)
        text = font.render('card is shown,please exit', True, (102, 0, 102), (0, 128, 128))
        textRect = text.get_rect()
        textRect.center = (475, 200)
        screen.blit(text, textRect)

    def showSenario3(self, screen):
        screen.blit(self.cardRoomImage, [200, 100])
        font = pg.font.Font(None, 60)
        text = font.render('card is shown,please exit', True, (102, 0, 102), (0, 128, 128))
        textRect = text.get_rect()
        textRect.center = (475, 200)
        screen.blit(text, textRect)

    def showSenario4(self, screen, event):
        self.buttonRoom.draw(screen)
        self.buttonWea.draw(screen)
        self.buttonSus.draw(screen)
        self.buttonPla.draw(screen)
        if self.buttonSus.eventChoose(screen, event) == True:
            self.buttonSeen = True
        if self.buttonWea.eventChoose(screen, event) == True:
            self.buttonSeen = True
        if self.buttonRoom.eventChoose(screen, event) == True:
            self.buttonSeen = True

    def showSenario5(self, screen, event):
        self.buttonRoom.draw(screen)
        self.buttonWea.draw(screen)
        self.buttonPla.draw(screen)
        if self.buttonWea.eventChoose(screen, event) == True:
            self.buttonSeen = True
        if self.buttonRoom.eventChoose(screen, event) == True:
            self.buttonSeen = True

    def showSenario6(self, screen, event):
        self.buttonSus.draw(screen)
        self.buttonWea.draw(screen)
        self.buttonPla.draw(screen)
        if self.buttonSus.eventChoose(screen, event) == True:
            self.buttonSeen = True
        if self.buttonWea.eventChoose(screen, event) == True:
            self.buttonSeen = True

    def showSenario7(self, screen, event):
        self.buttonSus.draw(screen)
        self.buttonRoom.draw(screen)
        self.buttonPla.draw(screen)
        if self.buttonSus.eventChoose(screen, event) == True:
            self.buttonSeen = True
        if self.buttonRoom.eventChoose(screen, event) == True:
            self.buttonSeen = True

    def showButtonSeen(self, screen, event):
        self.buttonSeenB.draw(screen)
        if self.buttonSeenB.HaveSeenCard(screen, event):
            pass

#this is the function to be used to run the class
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

        susRoom = [player.getRoom()]

#suspect dropdown menu
        list1 = dropdown.DropDown(
            [COLOR_INACTIVE, COLOR_ACTIVE],
            [COLOR_LIST_INACTIVE, COLOR_LIST_ACTIVE],
            650, 100, 200, 50,
            pg.font.SysFont(None, 30),
            "Select Suspect", sus.getNames(sus))
            # susRoom #this should get the player location and auto select it for the dropdown
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

        # #this button shows the guessed room card
        buttonRoom = button.Button(
            COLOR_INACTIVE,
            100, 300,
            150, 50,
            str(self.optionRoom)
        )

        # this button shows the guessed weapon card
        buttonWea = button.Button(
            COLOR_INACTIVE,
            375, 300,
            150, 50,
           str(self.optionWea)
        )

        # this button shows the guessed suspect card
        buttonSus = button.Button(
            COLOR_INACTIVE,
            650, 300,
            150, 50,
            str(self.optionSus)
        )

        # this button shows which player needs to choose a card to show
        buttonPla = button.Button(
            COLOR_INACTIVE,
            400, 200,
            200, 50,
            "Player " + str(self.playerNext) + "Choose a card to display"
        )

        # this button confirms the player has seen the matched guess card


        run = True
        while run:
            background_image = pg.image.load("../Image/clue_back.png")

            clock.tick(30)
            pg.display.update()

            event_list = pg.event.get()
            screen.blit(background_image, [0, 0])
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

            if self.failScreen == True:
                self.showFail(screen)

            if self.Senario1 == True:
                self.showSenario1(screen,event)

            if self.Senario2 == True:
                self.showSenario2(screen, event)

            if self.Senario3 == True:
                self.showSenario3(screen,event)

            if self.Senario4 == True:
                self.showSenario4(screen, event)

            if self.Senario5 == True:
                self.showSenario5(screen, event)

            if self.Senario6 == True:
                self.showSenario6(screen,event)

            if self.Senario7 == True:
                self.showSenario7(screen,event)


            if self.buttonSeen == True:
                self.showButtonSeen(screen, event)

            list1.draw(screen)
            list2.draw(screen)
            list3.draw(screen)
            button1.draw(screen)
            button1.event(screen, event)

            if button1.event(screen, event) == True:
                self.check_for_match( list1, list2, list3, screen)

            # buttonWea.eventChoose(screen, event)
            # buttonPla.eventChoose(screen, event)
            # buttonRoom.eventChoose(screen, event)
            # buttonSeen.event(screen, event)
            # buttonNoToSee.event(screen, event)

            #
            # if buttonNoToSee(screen, event) == True:
            #     run = False
            # if buttonSeen(screen, event) == True:
            #     run = False


            pg.display.flip()


#Guess.screenDisplay(Guess)
