import pygame as pg
import Deck
import suspect_cards
import room_cards
import weapon_cards
import Player as player
import dropdown
import button

class Guess:
    def __init__(self):
        pass


    def check_for_match(list1, list2, list3):
        check = False
        cards = []
        option1 = list1.active_option
        option2 = list2.active_option
        option3 = list3.active_option
        hand = player.getCards(player)
        Pl = player.Player
        pla = [Pl("Shakir", "baghdad", "1"), Pl("michelle", "shakirs", "2"), Pl("Alex", "yourmum", "3"),
            Pl("Tom", "???", "4"),
            Pl("Abby", "Toilet paper", "5"), Pl("King", "best teacher", "6")]
        while check == False:
            for play in pla:
                if hand == option1 or hand == option2 or hand == option3:
                    if hand == option1 and hand == option2 or hand == option2 \
                            and hand == option3 or hand == option1 and hand == option3 \
                            or hand == option1 and hand == option2 and hand == option3:
                        if hand == option1 and hand == option2:
                            cards = cards + option1
                            cards = cards + option2
                            check = True # need to pass turn over to that player
                        elif hand == option2 and hand == option3:
                            cards = cards + option3
                            cards = cards + option2
                            check = True
                        elif hand == option1 and hand == option3:
                            cards = cards + option1
                            cards = cards + option3
                            check = True
                        elif hand == option1 and hand == option2 and hand == option3:
                            cards = cards + option1
                            cards = cards + option2
                            cards = cards + option3
                            check = True
                    else:
                        if hand == option1:
                            cards = cards + option1
                            check = True # auto show card tom?
                        if hand == option2:
                            cards = cards + option2
                            check = True
                        if hand == option3:
                            cards = cards + option3
                            check = True
                else:
                    check = True
        return cards # next turn, no cards shown



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

    list1 = dropdown.DropDown(
        [COLOR_INACTIVE, COLOR_ACTIVE],
        [COLOR_LIST_INACTIVE, COLOR_LIST_ACTIVE],
        650, 100, 200, 50,
        pg.font.SysFont(None, 30),
        "Select Suspect", sus.getNames(sus))
        #player.Player.getLocation(player)) this should theoretically get the player location and auto select it

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

    button1 = button.Button(
        COLOR_INACTIVE,
            405, 600,
            150, 50,
            "Guess")

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

        if button1.event(screen, event) == True:
            check_for_match(list1, list2, list3)

        pg.display.flip()

    pg.quit()
    exit()
