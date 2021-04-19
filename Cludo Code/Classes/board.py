import pygame
import numpy as np
from random import randrange

from tile import tile
from newDice import Dice
#from notepad import notepad

BOARDWIDTH = 25
BOARDHEIGHT = 24
WINDOWWIDTH = 500
WINDOWHEIGHT = 500
WIDTH = 28
HEIGHT = 28
GRIDBUFFX = 30
GRIDBUFFY = 100

PLAYER1 = True
PLAYER2 = True
PLAYER3 = True
PLAYER4 = True
PLAYER5 = True
PLAYER6 = True

GREEN = (141, 197, 137)

pygame.init()
pygame.font.init()
pygame.display.set_caption("Cludo")
screen = pygame.display.set_mode([960, 950])

#loading previous turn font style
clueFont = pygame.font.SysFont("Segoe UI Black", 20)
textBoxPreviousTurn = clueFont.render("previous turn here", False, (255,255,255))

#loading images for tiles
tileImg = pygame.image.load("../Image/tile_unselected_empty.png")
tileImg = pygame.transform.scale(tileImg, (int(WIDTH), int(HEIGHT)))
tileImgSELECT = pygame.image.load("../Image/tile_unselected_selected.png")
tileImgSELECT = pygame.transform.scale(tileImgSELECT, (int(WIDTH), int(HEIGHT)))
tileImgHover = pygame.image.load("../Image/tile_unselected_hover.png")
tileImgHover = pygame.transform.scale(tileImgHover, (int(WIDTH), int(HEIGHT)))

tileImgP1 = pygame.image.load("../Image/tile_player1.png")
tileImgP1 = pygame.transform.scale(tileImgP1, (int(WIDTH), int(HEIGHT)))

tileImgP2 = pygame.image.load("../Image/tile_player2.png")
tileImgP2 = pygame.transform.scale(tileImgP2, (int(WIDTH), int(HEIGHT)))

tileImgP3 = pygame.image.load("../Image/tile_player3.png")
tileImgP3 = pygame.transform.scale(tileImgP3, (int(WIDTH), int(HEIGHT)))

tileImgP4 = pygame.image.load("../Image/tile_player4.png")
tileImgP4 = pygame.transform.scale(tileImgP4, (int(WIDTH), int(HEIGHT)))

tileImgP5 = pygame.image.load("../Image/tile_player5.png")
tileImgP5 = pygame.transform.scale(tileImgP5, (int(WIDTH), int(HEIGHT)))

tileImgP6 = pygame.image.load("../Image/tile_player6.png")
tileImgP6 = pygame.transform.scale(tileImgP6, (int(WIDTH), int(HEIGHT)))

#loading images for background and title
background = pygame.image.load("../Image/background.png")
backgroundx, backgroundy = background.get_size()
background = pygame.transform.scale(background, (int(backgroundx*.933), int(backgroundy*.933)))
title = pygame.image.load("../Image/cluedo-logo.png")
title = pygame.transform.scale(title, ((int(563*.45)), (int(200*.45))))

#loading images for buttons unselected
buttonAccuse = pygame.image.load("../Image/button_accuse_unselected.png")
buttonAccusex, buttonAccusey = buttonAccuse.get_size()
buttonAccuse = pygame.transform.scale(buttonAccuse, (int(buttonAccusex*.4), int(buttonAccusey*.4)))

buttonGuess = pygame.image.load("../Image/button_guess_unselected.png")
buttonGuessx, buttonGuessy = buttonGuess.get_size()
buttonGuess = pygame.transform.scale(buttonGuess, (int(buttonGuessx*.4), int(buttonGuessy*.4)))

buttonNextTurn = pygame.image.load("../Image/button_next_turn_unselected.png")
buttonNextTurnx, buttonNextTurny = buttonNextTurn.get_size()
buttonNextTurn = pygame.transform.scale(buttonNextTurn, (int(buttonNextTurnx*.4), int(buttonNextTurny*.4)))

buttonRollDice = pygame.image.load("../Image/button_roll_dice_unselected.png")
buttonRollDicex, buttonRollDicey = buttonRollDice.get_size()
buttonRollDice = pygame.transform.scale(buttonRollDice, (int(buttonRollDicex*.4), int(buttonRollDicey*.4)))

buttonMenu = pygame.image.load("../Image/button_menu_unselected.png")
buttonMenux, buttonMenuy = buttonMenu.get_size()
buttonMenu = pygame.transform.scale(buttonMenu, (int(buttonMenux*.4), int(buttonMenuy*.4)))

buttonShowCards = pygame.image.load("../Image/button_show_cards.png")

#loading images for buttons selected
buttonAccuseSelected = pygame.image.load("../Image/button_accuse_selected.png")
buttonAccuseSelectedx, buttonAccuseSelectedy = buttonAccuseSelected.get_size()
buttonAccuseSelected = pygame.transform.scale(buttonAccuseSelected, (int(buttonAccuseSelectedx*.4), int(buttonAccuseSelectedy*.4)))

buttonGuessSelected = pygame.image.load("../Image/button_guess_selected.png")
buttonGuessSelectedx, buttonGuessSelectedy = buttonGuessSelected.get_size()
buttonGuessSelected = pygame.transform.scale(buttonGuessSelected, (int(buttonGuessSelectedx*.4), int(buttonGuessSelectedy*.4)))

buttonNextTurnSelected = pygame.image.load("../Image/button_next_turn_selected.png")
buttonNextTurnSelectedx, buttonNextTurnSelectedy = buttonNextTurnSelected.get_size()
buttonNextTurnSelected = pygame.transform.scale(buttonNextTurnSelected, (int(buttonNextTurnSelectedx*.4), int(buttonNextTurnSelectedy*.4)))

buttonRollDiceSelected = pygame.image.load("../Image/button_roll_dice_selected.png")
buttonRollDiceSelectedx, buttonRollDiceSelectedy = buttonRollDiceSelected.get_size()
buttonRollDiceSelected = pygame.transform.scale(buttonRollDiceSelected, (int(buttonRollDiceSelectedx*.4), int(buttonRollDiceSelectedy*.4)))

buttonMenuSelected = pygame.image.load("../Image/button_menu_selected.png")
buttonMenuSelectedx, buttonMenuSelectedy = buttonMenuSelected.get_size()
buttonMenuSelected = pygame.transform.scale(buttonMenuSelected, (int(buttonMenuSelectedx*.4), int(buttonMenuSelectedy*.4)))

buttonShowCardsSelected = pygame.image.load("../Image/button_show_cards_selected.png")

#loading cards
cardBlank = pygame.image.load("../Image/card_blank.png")

#loading notepad
buttonNotepad = pygame.image.load("../Image/button_notepad.png")
buttonNotepadSelected = pygame.image.load("../Image/button_notepad_selected.png")

#loading previous turn window card
textPreviousTurn = pygame.image.load("../Image/text_previous_move_window.png")
textPreviousTurnx, textPreviousTurny = textPreviousTurn.get_size()
textPreviousTurn = pygame.transform.scale(textPreviousTurn, (int(textPreviousTurnx*.4), int(textPreviousTurny*.4)))


#load players
imgPlayer1 = pygame.image.load("../Image/player_1.png")
imgPlayer1x, imgPlayer1y = imgPlayer1.get_size()
imgPlayer1 = pygame.transform.scale(imgPlayer1, (int(imgPlayer1x*.3), int(imgPlayer1y*.3)))

imgPlayer2 = pygame.image.load("../Image/player_2.png")
imgPlayer2x, imgPlayer2y = imgPlayer2.get_size()
imgPlayer2 = pygame.transform.scale(imgPlayer2, (int(imgPlayer2x*.3), int(imgPlayer2y*.3)))

imgPlayer3 = pygame.image.load("../Image/player_3.png")
imgPlayer3x, imgPlayer3y = imgPlayer3.get_size()
imgPlayer3 = pygame.transform.scale(imgPlayer3, (int(imgPlayer3x*.3), int(imgPlayer3y*.3)))

imgPlayer4 = pygame.image.load("../Image/player_4.png")
imgPlayer4x, imgPlayer4y = imgPlayer4.get_size()
imgPlayer4 = pygame.transform.scale(imgPlayer4, (int(imgPlayer4x*.3), int(imgPlayer4y*.3)))

imgPlayer5 = pygame.image.load("../Image/player_5.png")
imgPlayer5x, imgPlayer5y = imgPlayer5.get_size()
imgPlayer5 = pygame.transform.scale(imgPlayer5, (int(imgPlayer5x*.3), int(imgPlayer5y*.3)))

imgPlayer6 = pygame.image.load("../Image/player_6.png")
imgPlayer6x, imgPlayer6y = imgPlayer6.get_size()
imgPlayer6 = pygame.transform.scale(imgPlayer6, (int(imgPlayer6x*.3), int(imgPlayer6y*.3)))

def grid(x, y):
    screen.blit(tileImg, (x, y))
    

def drawGrid():
    for row in range(BOARDWIDTH):
        for column in range(BOARDHEIGHT):                
            x, y = pygame.mouse.get_pos()
            x = x - GRIDBUFFX
            y = y - GRIDBUFFY

            if grid[row, column].getPlayer() == 1:
                screen.blit(tileImgP1, (column*WIDTH+GRIDBUFFX,HEIGHT*row+GRIDBUFFY))

            elif grid[row, column].getPlayer() == 2:
                screen.blit(tileImgP2, (column*WIDTH+GRIDBUFFX,HEIGHT*row+GRIDBUFFY))

            elif grid[row, column].getPlayer() == 3:
                screen.blit(tileImgP3, (column*WIDTH+GRIDBUFFX,HEIGHT*row+GRIDBUFFY))
                
            elif grid[row, column].getPlayer() == 4:
                screen.blit(tileImgP4, (column*WIDTH+GRIDBUFFX,HEIGHT*row+GRIDBUFFY))
                
            elif grid[row, column].getPlayer() == 5:
                screen.blit(tileImgP5, (column*WIDTH+GRIDBUFFX,HEIGHT*row+GRIDBUFFY))
                
            elif grid[row, column].getPlayer() == 6:
                screen.blit(tileImgP6, (column*WIDTH+GRIDBUFFX,HEIGHT*row+GRIDBUFFY))

            # selected tile
            elif grid[row, column].getSelected() and grid[row, column].getIsTile() :
                screen.blit(tileImgSELECT, (column*WIDTH+GRIDBUFFX,HEIGHT*row+GRIDBUFFY))

            # hover tile
            elif (np.ceil(x/WIDTH) == column+1 and np.ceil(y/WIDTH) == row+1 and grid[row, column].getIsTile()):
                screen.blit(tileImgHover, (column*WIDTH+GRIDBUFFX,HEIGHT*row+GRIDBUFFY))

            # unselected tile
            elif grid[row, column].getIsTile():
                screen.blit(tileImg, (column*WIDTH+GRIDBUFFX,HEIGHT*row+GRIDBUFFY))



def isButtonClicked(x, y):
    if (x >= 720 and x <= 942 and y >= 400 and y <= 481.6):
        #roll dice class function goes here!
        print("roll dice")#222 x 81.6
        number = randrange(12)+1
        diceRoll = Dice(number)
        diceRoll.rolldice()

    if (x >= 720 and x <= 942 and y >= 500 and y <= 581.6):
        print("next turn")#222 x 81.6

    if (x >= 720 and x <= 942 and y >= 600 and y <= 681.6):
        print("guess")#222 x 81.6

    if (x >= 720 and x <= 942 and y >= 700 and y <= 781.6):
        print("accuse")#222 x 81.6

    if (x >= 12 and x <= 92 and y >= 812 and y <= 937):
        print("show cards")

    if (x >= 10 and x <= 142 and y >= 10 and y <= 87.2):
        print("menu")

    if (x >= 860 and x <= 927 and y >= 812 and y <= 937):
        #notepad.notepad()
        print("Notepad")

def isButtonSelected(x, y):
    if (x >= 720 and x <= 942 and y >= 400 and y <= 481.6):
        screen.blit(buttonRollDiceSelected, (720, 400))

    if (x >= 720 and x <= 942 and y >= 500 and y <= 581.6):
        screen.blit(buttonNextTurnSelected, (720, 500))

    if (x >= 720 and x <= 942 and y >= 600 and y <= 681.6):
        screen.blit(buttonGuessSelected, (720, 600))

    if (x >= 720 and x <= 942 and y >= 700 and y <= 781.6):
        screen.blit(buttonAccuseSelected, (720, 700))

    if (x >= 12 and x <= 92 and y >= 812 and y <= 937):
        screen.blit(buttonShowCardsSelected, (12, 812))

    if (x >= 10 and x <= 142 and y >= 10 and y <= 87.2):
        screen.blit(buttonMenuSelected, (10, 10))
    
    if (x >= 860 and x <= 927 and y >= 812 and y <= 937):
        screen.blit(buttonNotepadSelected, (860, 812))
    


grid = tile.initiateBoard(PLAYER1,
                          PLAYER2,
                          PLAYER3,
                          PLAYER4,
                          PLAYER5,
                          PLAYER6)



done = False

clock = pygame.time.Clock()
pygame.display.set_icon(imgPlayer1)

#game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

        if event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = (pos[0] - GRIDBUFFX) // WIDTH
            row = (pos[1] - GRIDBUFFY) // HEIGHT

            isButtonClicked(pos[0], pos[1])
            
            # Changes tile to selected / unselected
            try:
                grid[int(row), int(column)].setSelected(not grid[int(row), int(column)].getSelected())
            except:
                pass
            
    # Set the screen background
    screen.fill(GREEN)
    screen.blit(background, (GRIDBUFFX, GRIDBUFFY))
    screen.blit(title, (((950/2-(int(563*.45)/2))-110), 7))
    screen.blit(textBoxPreviousTurn, (600, 20))

    #v menu
    if PLAYER1 == True:
        screen.blit(imgPlayer1, (730, 100))
    if PLAYER2 == True:
        screen.blit(imgPlayer2, (840, 100))
    if PLAYER3 == True:
        screen.blit(imgPlayer3, (730, 200))
    if PLAYER4 == True:
        screen.blit(imgPlayer4, (840, 200))
    if PLAYER5 == True:
        screen.blit(imgPlayer5, (730, 300))
    if PLAYER6 == True:
        screen.blit(imgPlayer6, (840, 300))
        
    screen.blit(buttonRollDice, (720, 400))
    screen.blit(buttonNextTurn, (720, 500))
    screen.blit(buttonGuess, (720, 600))
    screen.blit(buttonAccuse, (720, 700))
    screen.blit(buttonMenu, (10, 10))
    screen.blit(textPreviousTurn, (550, 10))
    screen.blit(textBoxPreviousTurn, (690, 20))
    

    #h menu
    screen.blit(buttonShowCards, (12, 812))
    screen.blit(cardBlank, (102, 812))  #1
    screen.blit(cardBlank, (185, 812))  #2
    screen.blit(cardBlank, (268, 812))  #3
    screen.blit(cardBlank, (351, 812))  #4
    screen.blit(cardBlank, (434, 812))  #5
    screen.blit(cardBlank, (517, 812))  #6
    screen.blit(cardBlank, (600, 812))  #7
    screen.blit(cardBlank, (683, 812))  #8
    screen.blit(cardBlank, (766, 812))  #9

    #notepad
    screen.blit(buttonNotepad, (860, 812))

    # Change button to hover if mouse if over.
    x, y = pygame.mouse.get_pos()
    isButtonSelected(x, y)
    
    # Draw the grid
    drawGrid()
 
    clock.tick(60)  #set to 30 to half cycle speeds / reduce processing requirements
    pygame.display.flip()
    
pygame.quit()
