import pygame
import pyttsx3
import speech_recognition

def notepad():
    # initializing the constructor
    pygame.init()

    # size of window
    x = 400
    y = 900
    screen = pygame.display.set_mode((x, y))
    # title of window
    pygame.display.set_caption('Notepad')
    # icon of window
    # .. go back 1 time directory
    # ... go back 2 time directory
    icon_img = "../Image/Clue_logo.png"
    icon = pygame.image.load(icon_img)
    pygame.display.set_icon(icon)

    # define the RGB value
    gray = (130, 130, 130)
    red = (255, 0, 0)
    white = (255, 255, 255)

    # background
    notepad_background_img = "../Image/notepad_background 2.png"
    notepad_background = pygame.image.load(notepad_background_img)
    screen.blit(notepad_background, (0, 0))

    # create red line
    # import card information from other classes
    import room_cards
    import suspect_cards
    import weapon_cards

    # initialise an object of room_cards and use the method getNames to get room_list
    room_list = room_cards.Room_cards().getNames()  # name of file and name of class
    suspect_list = suspect_cards.Suspect_cards().getNames()  # name of file and name of class
    weapon_list = weapon_cards.Weapon_cards().getNames()  # name of file and name of class

    # font
    card_category_font = pygame.font.SysFont('timesnewroman', 24, bold=1)
    card_name_font = pygame.font.SysFont('timesnewroman', 20)

    # create a list includes suspects, rooms, weapons
    general_list = []
    general_list += suspect_list + weapon_list + room_list
    general_list.insert(0, 'Suspect')
    general_list.insert(len(suspect_list) + 1, 'Weapon')
    general_list.insert(-len(room_list), 'Room')

    # write items on notepad
    spacing = 113
    for item in general_list:
        if (item == 'Suspect') or (item == 'Weapon') or (item == 'Room'):
            screen.blit(card_category_font.render(item, True, gray), (70, spacing))
        else:
            u=screen.blit(card_name_font.render(item, True, gray), (85, spacing))
        spacing += 29

    # text to speech
    while True:
        pygame.display.update()
        robot_ear = speech_recognition.Recognizer()
        robot_mouth = pyttsx3.init()
        robot_brain = ''

        robot_mouth.say("You can click on the card names to take note")
        if pygame.init():
            robot_mouth.runAndWait()
            break


        with speech_recognition.Microphone() as mic:
            audio = robot_ear.listen(mic)
        try:
            you = robot_ear.recognize_google(audio)
        except:
            you == ""
        print(you)

        if you == "Hello":
            robot_brain == "Hi"
        elif you == "What's your name?":
            robot_brain == "My name is Cluedo"
        else:
            robot_brain == "I don't understand what you say"
        print(robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()

    # quit button
    while True:
        spacing_2 = 153
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                pygame.quit()

            # button
            a = 145
            b = 166
            pos = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if even.type == pygame.MOUSEBUTTONDOWN:
                for i in u:
                    # if pos == i.__pos__():
                    if x/5.3 < pos[1] < x/2 and a < pos[1] < b:
                        pygame.draw.rect(screen, red, (85, spacing_2, 145, 2))
                # spacing_2 += 29
                # break
        pygame.display.update()

        # click button - red line
        #     spacing_2 = 153
        # #         pygame.draw.rect(screen, red, (x/5, y/5.9, 145, 2))
        #     for element in general_list:
        #         pygame.draw.rect(screen, red, (85, spacing_2, 145, 2))
        #         spacing_2 += 29
        # if ev.type == pygame.MOUSEBUTTONDOWN:
        #     spacing = 159
        #     for i in card_name_font:
        #         if spacing - 10 <= mouse[1] <= spacing + 10:
        #             #
        #             pygame.draw.rect(screen, red, [70, spacing, 70, 2])
        # #
        #         pygame.draw.rect(screen, red, [70, 162, 70, 2])
        #         if 110 <= mouse[0] <= 210:
        #             pygame.draw.rect(screen, red, [70, 191, 70, 2])
        #         if 58 <= mouse[2] <= 125:
        #             pygame.draw.rect(screen, gray, [58, 125, 150, 2])
        #     if ev.type == pygame.MOUSEBUTTONUP:
        #         if x / 2 <= mouse[0] <= x / 2 + 140 and y / 2 <= mouse[3] <= y / 2 + 40:
        #             pygame.draw.rect(screen, red, [x / 2, y / 2, 140, 40])
        # mouse = pygame.mouse.get_pos()
        # if x/2 <= mouse[0] <= x/2+140 and y/2 <= mouse[1] <= y/2+40:
        #     pygame.draw.rect(screen,red,[x/2,y/2,140,40])
        # else:
        #     pygame.draw.rect(screen,red,[x/2,y/2,140,40])


# # iterate over the list of Event objects that was returned by pygame.event.get() method.
# for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#         pygame.quit()
#         # quit the program.
#         quit()
#
#     # Draws the surface object to the screen.
#     pygame.display.update()


def innit():
    notepad()


class Notepad:
    notepad()
