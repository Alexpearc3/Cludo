import pygame
import numpy as np
from random import randrange
import Deck
from tile import tile
import Player
import room
import notepad

# from newDice import Dice
# from notepad import notepad


class board():
    player = Player.Player
    Players = []
    deck = Deck.Deck()
    rooms = []

    # passing through players array as well as customisation setting (1 or 2)
    def __init__(self, Players, customNo):
        self.customNo = customNo
        self.PLAYER1 = Players[0]
        self.PLAYER2 = Players[1]
        self.PLAYER3 = Players[2]
        self.PLAYER4 = Players[3]
        self.PLAYER5 = Players[4]
        self.PLAYER6 = Players[5]
        self.possibleMoves = []
        self.playersTurn = 0
        self.board = np.empty((25, 24), dtype=object)
        newNotepad = notepad.Notepad()
        playerTList = Players
        count = 0
        for player in Players:
            self.Players.append(self.player(player, count + 1,newNotepad))
            count += 1

    BOARDWIDTH = 25
    BOARDHEIGHT = 24
    WINDOWWIDTH = 500
    WINDOWHEIGHT = 500
    WIDTH = 28
    HEIGHT = 28
    GRIDBUFFX = 30
    GRIDBUFFY = 100

    GREEN = (141, 197, 137)

    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("Cludo")
    screen = pygame.display.set_mode([960, 950])

    # loading previous turn font style
    clueFont = pygame.font.SysFont("Segoe UI Black", 20)
    textBoxPreviousTurn = clueFont.render("previous turn here", False, (255, 255, 255))

    # loading images for tiles
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

    # loading images for background
    background = pygame.image.load("../Image/background.png")
    backgroundx, backgroundy = background.get_size()
    background = pygame.transform.scale(background, (int(backgroundx * .933), int(backgroundy * .933)))

    # loading images for alt background
    background_alt = pygame.image.load("../Image/background_alternative.png")
    background_altx, background_alty = background_alt.get_size()
    background_alt = pygame.transform.scale(background_alt, (int(background_altx * .933), int(background_alty * .933)))

    # loading image for logo
    title = pygame.image.load("../Image/cluedo-logo.png")
    title = pygame.transform.scale(title, ((int(563 * .45)), (int(200 * .45))))

    # loading images for buttons unselected
    buttonAccuse = pygame.image.load("../Image/button_accuse_unselected.png")
    buttonAccusex, buttonAccusey = buttonAccuse.get_size()
    buttonAccuse = pygame.transform.scale(buttonAccuse, (int(buttonAccusex * .4), int(buttonAccusey * .4)))

    buttonGuess = pygame.image.load("../Image/button_guess_unselected.png")
    buttonGuessx, buttonGuessy = buttonGuess.get_size()
    buttonGuess = pygame.transform.scale(buttonGuess, (int(buttonGuessx * .4), int(buttonGuessy * .4)))

    buttonNextTurn = pygame.image.load("../Image/button_next_turn_unselected.png")
    buttonNextTurnx, buttonNextTurny = buttonNextTurn.get_size()
    buttonNextTurn = pygame.transform.scale(buttonNextTurn, (int(buttonNextTurnx * .4), int(buttonNextTurny * .4)))

    buttonRollDice = pygame.image.load("../Image/button_roll_dice_unselected.png")
    buttonRollDicex, buttonRollDicey = buttonRollDice.get_size()
    buttonRollDice = pygame.transform.scale(buttonRollDice, (int(buttonRollDicex * .4), int(buttonRollDicey * .4)))

    buttonMenu = pygame.image.load("../Image/button_menu_unselected.png")
    buttonMenux, buttonMenuy = buttonMenu.get_size()
    buttonMenu = pygame.transform.scale(buttonMenu, (int(buttonMenux * .4), int(buttonMenuy * .4)))

    buttonShowCards = pygame.image.load("../Image/button_show_cards.png")

    # loading images for buttons selected
    buttonAccuseSelected = pygame.image.load("../Image/button_accuse_selected.png")
    buttonAccuseSelectedx, buttonAccuseSelectedy = buttonAccuseSelected.get_size()
    buttonAccuseSelected = pygame.transform.scale(buttonAccuseSelected,
                                                  (int(buttonAccuseSelectedx * .4), int(buttonAccuseSelectedy * .4)))

    buttonGuessSelected = pygame.image.load("../Image/button_guess_selected.png")
    buttonGuessSelectedx, buttonGuessSelectedy = buttonGuessSelected.get_size()
    buttonGuessSelected = pygame.transform.scale(buttonGuessSelected,
                                                 (int(buttonGuessSelectedx * .4), int(buttonGuessSelectedy * .4)))

    buttonNextTurnSelected = pygame.image.load("../Image/button_next_turn_selected.png")
    buttonNextTurnSelectedx, buttonNextTurnSelectedy = buttonNextTurnSelected.get_size()
    buttonNextTurnSelected = pygame.transform.scale(buttonNextTurnSelected, (
        int(buttonNextTurnSelectedx * .4), int(buttonNextTurnSelectedy * .4)))

    buttonRollDiceSelected = pygame.image.load("../Image/button_roll_dice_selected.png")
    buttonRollDiceSelectedx, buttonRollDiceSelectedy = buttonRollDiceSelected.get_size()
    buttonRollDiceSelected = pygame.transform.scale(buttonRollDiceSelected, (
        int(buttonRollDiceSelectedx * .4), int(buttonRollDiceSelectedy * .4)))

    buttonMenuSelected = pygame.image.load("../Image/button_menu_selected.png")
    buttonMenuSelectedx, buttonMenuSelectedy = buttonMenuSelected.get_size()
    buttonMenuSelected = pygame.transform.scale(buttonMenuSelected,
                                                (int(buttonMenuSelectedx * .4), int(buttonMenuSelectedy * .4)))

    buttonShowCardsSelected = pygame.image.load("../Image/button_show_cards_selected.png")

    # loading cards
    cardBlank = pygame.image.load("../Image/card_blank.png")

    # loading notepad
    buttonNotepad = pygame.image.load("../Image/button_notepad.png")
    buttonNotepadSelected = pygame.image.load("../Image/button_notepad_selected.png")

    # loading previous turn window card
    textPreviousTurn = pygame.image.load("../Image/text_previous_move_window.png")
    textPreviousTurnx, textPreviousTurny = textPreviousTurn.get_size()
    textPreviousTurn = pygame.transform.scale(textPreviousTurn,
                                              (int(textPreviousTurnx * .4), int(textPreviousTurny * .4)))

    # load players
    imgPlayer1 = pygame.image.load("../Image/player_1.png")
    imgPlayer1x, imgPlayer1y = imgPlayer1.get_size()
    imgPlayer1 = pygame.transform.scale(imgPlayer1, (int(imgPlayer1x * .3), int(imgPlayer1y * .3)))

    imgPlayer2 = pygame.image.load("../Image/player_2.png")
    imgPlayer2x, imgPlayer2y = imgPlayer2.get_size()
    imgPlayer2 = pygame.transform.scale(imgPlayer2, (int(imgPlayer2x * .3), int(imgPlayer2y * .3)))

    imgPlayer3 = pygame.image.load("../Image/player_3.png")
    imgPlayer3x, imgPlayer3y = imgPlayer3.get_size()
    imgPlayer3 = pygame.transform.scale(imgPlayer3, (int(imgPlayer3x * .3), int(imgPlayer3y * .3)))

    imgPlayer4 = pygame.image.load("../Image/player_4.png")
    imgPlayer4x, imgPlayer4y = imgPlayer4.get_size()
    imgPlayer4 = pygame.transform.scale(imgPlayer4, (int(imgPlayer4x * .3), int(imgPlayer4y * .3)))

    imgPlayer5 = pygame.image.load("../Image/player_5.png")
    imgPlayer5x, imgPlayer5y = imgPlayer5.get_size()
    imgPlayer5 = pygame.transform.scale(imgPlayer5, (int(imgPlayer5x * .3), int(imgPlayer5y * .3)))

    imgPlayer6 = pygame.image.load("../Image/player_6.png")
    imgPlayer6x, imgPlayer6y = imgPlayer6.get_size()
    imgPlayer6 = pygame.transform.scale(imgPlayer6, (int(imgPlayer6x * .3), int(imgPlayer6y * .3)))

    def grid(self, x, y):
        self.screen.blit(self.tileImg, (x, y))

    def drawGrid(self, board):
        for row in range(self.BOARDWIDTH):
            for column in range(self.BOARDHEIGHT):
                x, y = pygame.mouse.get_pos()
                x = x - self.GRIDBUFFX
                y = y - self.GRIDBUFFY

                if board[row, column].getPlayer() == 1:
                    self.screen.blit(self.tileImgP1,
                                     (column * self.WIDTH + self.GRIDBUFFX, self.HEIGHT * row + self.GRIDBUFFY))

                elif board[row, column].getPlayer() == 2:
                    self.screen.blit(self.tileImgP2,
                                     (column * self.WIDTH + self.GRIDBUFFX, self.HEIGHT * row + self.GRIDBUFFY))

                elif board[row, column].getPlayer() == 3:
                    self.screen.blit(self.tileImgP3,
                                     (column * self.WIDTH + self.GRIDBUFFX, self.HEIGHT * row + self.GRIDBUFFY))

                elif board[row, column].getPlayer() == 4:
                    self.screen.blit(self.tileImgP4,
                                     (column * self.WIDTH + self.GRIDBUFFX, self.HEIGHT * row + self.GRIDBUFFY))

                elif board[row, column].getPlayer() == 5:
                    self.screen.blit(self.tileImgP5,
                                     (column * self.WIDTH + self.GRIDBUFFX, self.HEIGHT * row + self.GRIDBUFFY))

                elif board[row, column].getPlayer() == 6:
                    self.screen.blit(self.tileImgP6,
                                     (column * self.WIDTH + self.GRIDBUFFX, self.HEIGHT * row + self.GRIDBUFFY))

                # selected tile
                elif board[row, column].getSelected() and board[row, column].getIsTile():
                    self.screen.blit(self.tileImgSELECT,
                                     (column * self.WIDTH + self.GRIDBUFFX, self.HEIGHT * row + self.GRIDBUFFY))

                # hover tile
                elif (np.ceil(x / self.WIDTH) == column + 1 and np.ceil(y / self.WIDTH) == row + 1 and board[
                    row, column].getIsTile()):
                    self.screen.blit(self.tileImgHover,
                                     (column * self.WIDTH + self.GRIDBUFFX, self.HEIGHT * row + self.GRIDBUFFY))

                # unselected tile
                elif board[row, column].getIsTile():
                    self.screen.blit(self.tileImg,
                                     (column * self.WIDTH + self.GRIDBUFFX, self.HEIGHT * row + self.GRIDBUFFY))


    #selects tiles and sets possiblemove on tiles where a player can move to
    def selectTiles(self, possibleMoves, x, y):
        print(possibleMoves)
        for i in range(len(possibleMoves)):
            if possibleMoves[i] != False:
                if i <= 1:  # check if possible move is in x direction
                    tile = self.getTile(possibleMoves[i], y)
                    tile.setPossibleMove(True)
                    tile.setSelected(True)
                    self.setTile(tile, possibleMoves[i], y)
                else:  # possible move is in y direction
                    print(i)
                    tile = self.getTile(x, possibleMoves[i])
                    tile.setPossibleMove(True)
                    tile.setSelected(True)
                    self.setTile(tile, x, possibleMoves[i])

    #check tiles around a player, return a list of moves [x-1,x+1,y-1,y+1] [False,False,False,False] when not possible
    def lookAround(self, x, y):
        possibleMoves = [x - 1, x + 1, y - 1, y + 1]
        print(possibleMoves)
        if possibleMoves[0] < 0 or not self.getTile(possibleMoves[0], y).getIsTile():  # cant go left
            if not self.getTile(possibleMoves[0], y).getDoor():
                possibleMoves[0] = False
        test = True
        if int(possibleMoves[1]) > 23:  # cant go right
            possibleMoves[1] = False
            test = False
        if test:
            if not self.getTile(possibleMoves[1], y).getIsTile():
                if not self.getTile(possibleMoves[1], y).getDoor():
                    possibleMoves[1] = False

        if possibleMoves[2] < 0 or not self.getTile(x, possibleMoves[2]).getIsTile():  # cant go up
            if not self.getTile(x, possibleMoves[2]).getDoor():
                possibleMoves[2] = False
        test = True
        if possibleMoves[3] > 24:  # cant go down
            possibleMoves[3] = False
        test = False
        if test:
            if not self.getTile(possibleMoves[3], y).getIsTile():
                if not self.getTile(possibleMoves[3], y).getDoor():
                    possibleMoves[3] = False
        self.possibleMoves = possibleMoves
        return possibleMoves

    #return a tile fromm board
    def getTile(self, x, y):
        return self.board[y, x]

    #set a tile to board
    def setTile(self, tile, x, y):
        self.board[y, x] = tile

    def isButtonClicked(self, x, y):
        isTurnComplete = False
        if (x >= 720 and x <= 942 and y >= 400 and y <= 481.6):
            # roll dice class function goes here!
            currentPlayer = self.getCurrentPlayer()
            if not currentPlayer.getRolled():
                print("roll dice")  # 222 x 81.6
                number = randrange(12) + 1

                moves = number  # Dice(number, self.screen).rolldice()

                print("current Player ", currentPlayer.getPlayerID())
                currentPlayer.setMoves(moves)
                self.setPlayer(currentPlayer)
                self.movePlayer()
                currentPlayer = self.getCurrentPlayer()
                currentPlayer.setRolled(True)
                self.setPlayer(currentPlayer)

        if (x >= 720 and x <= 942 and y >= 500 and y <= 581.6):
            print("next turn")  # 222 x 81.6
            player = self.getCurrentPlayer()
            x, y = player.getLocation()
            self.possibleMoves = self.lookAround(x, y)
            self.unsetPossibleMoves(x, y)
            currentPlayer = self.getCurrentPlayer()
            currentPlayer.setRolled(False)
            self.setPlayer(currentPlayer)
            isTurnComplete = True

        if (x >= 720 and x <= 942 and y >= 600 and y <= 681.6):
            print("guess")  # 222 x 81.6
            player = self.getCurrentPlayer()
            x, y = player.getLocation()
            if self.getTile(x,y).getRoom() != "tile":
                #call guess
                g = "guess"

        if (x >= 720 and x <= 942 and y >= 700 and y <= 781.6):
            print("accuse")  # 222 x 81.6

        if (x >= 12 and x <= 92 and y >= 812 and y <= 937):
            print("show cards")

        if (x >= 10 and x <= 142 and y >= 10 and y <= 87.2):
            print("menu")
            done = True

        if (x >= 860 and x <= 927 and y >= 812 and y <= 937):
            # notepad.notepad()
            currentPlayer = self.getCurrentPlayer()
            notepad = currentPlayer.getNotepad()
            notepad.initNotepad()
            print("Notepad")
        return isTurnComplete

    def isButtonSelected(self, x, y):
        if (x >= 720 and x <= 942 and y >= 400 and y <= 481.6):
            self.screen.blit(self.buttonRollDiceSelected, (720, 400))

        if (x >= 720 and x <= 942 and y >= 500 and y <= 581.6):
            self.screen.blit(self.buttonNextTurnSelected, (720, 500))

        if (x >= 720 and x <= 942 and y >= 600 and y <= 681.6):
            self.screen.blit(self.buttonGuessSelected, (720, 600))

        if (x >= 720 and x <= 942 and y >= 700 and y <= 781.6):
            self.screen.blit(self.buttonAccuseSelected, (720, 700))

        if (x >= 12 and x <= 92 and y >= 812 and y <= 937):
            self.screen.blit(self.buttonShowCardsSelected, (12, 812))

        if (x >= 10 and x <= 142 and y >= 10 and y <= 87.2):
            self.screen.blit(self.buttonMenuSelected, (10, 10))

        if (x >= 860 and x <= 927 and y >= 812 and y <= 937):
            self.screen.blit(self.buttonNotepadSelected, (860, 812))

    #Return the current player
    def getCurrentPlayer(self):
        return self.Players[self.playersTurn]

    #set a player to the Players array
    def setPlayer(self, player):
        for i in range(len(self.Players)):
            if self.Players[i].getPlayerID() == player.getPlayerID():
                print("success")
                self.Players[i] = player

    #Unset the selected tiles after a move and at end of the time
    def unsetPossibleMoves(self, x, y):
        possibleMoves = self.possibleMoves
        for i in range(len(possibleMoves)):
            if possibleMoves[i] != False:
                if i <= 1:  # check if possible move is in x direction
                    tile = self.getTile(possibleMoves[i], y)
                    tile.setPossibleMove(False)
                    tile.setSelected(False)
                    self.setTile(tile, possibleMoves[i], y)
                else:  # possible move is in y direction
                    print(i)
                    tile = self.getTile(x, possibleMoves[i])
                    tile.setPossibleMove(False)
                    tile.setSelected(False)
                    self.setTile(tile, x, possibleMoves[i])
        for r in self.board:
            for c in r:
                c.setSelected(False)
                c.setPossibleMove(False)

    #mov
    def movePlayer(self):
        player = self.getCurrentPlayer()
        x, y = player.getLocation()
        if self.getTile(x, y).getRoom() == "tile":
            possibleMoves = self.lookAround(x, y)
            self.selectTiles(possibleMoves, x, y)
            self.setPlayer(player)

            print(possibleMoves)
        else:
            for rooms in self.rooms:
                print("motherfucker")
                if rooms.getName() == self.getTile(x, y).getRoom():
                    for door in rooms.getDoors():
                        j, k = door
                        possibleMoves = self.lookAround(j, k)
                        self.selectTiles(possibleMoves, j, k)

    def movePlayerTile(self, x, y):
        currentPlayer = self.getCurrentPlayer()
        j, k = currentPlayer.getLocation()
        if self.getTile(j, k).getRoom() == "tile": # check player is not in a room
            #check if its a possible move, and not a player and if a player has moves
            if self.getTile(x, y).getPossibleMove() == True and self.getTile(x,y).getPlayer() == 0 and currentPlayer.getMoves() >= 1:
                #check if target is a door
                if self.getTile(x, y).getPossibleMove() and not self.getTile(x, y).getDoor():
                    j, k = currentPlayer.getLocation()  # j,k = players x y coords. actual x y is where we are moving to/ target destination
                    tile = self.getTile(j, k)
                    tile.setSelected(False)
                    tile.setPossibleMove(False)
                    tile.setPlayer(0)
                    self.setTile(tile, j, k)
                    self.unsetPossibleMoves(j, k)

                    tile = self.getTile(x, y)
                    tile.setPlayer(currentPlayer.getPlayerID())
                    tile.setSelected(False)
                    tile.setPossibleMove(False)
                    print(self.getTile(x, y).getPlayer())
                    self.setTile(tile, x, y)
                    currentPlayer.setMoves(currentPlayer.getMoves() - 1)
                    currentPlayer.setLocation(x, y)
                    self.setPlayer(currentPlayer)
                    self.movePlayer()
                else:  # door, move player off board into rooms[player,player,player...]
                    if self.getTile(x, y).getDoor():
                        tile = self.getTile(j, k)
                        tile.setSelected(False)
                        tile.setPossibleMove(False)
                        tile.setPlayer(0)
                        self.setTile(tile, j, k)
                        self.unsetPossibleMoves(j, k)

                        currentPlayer.setLocation(x, y)
                        self.setPlayer(currentPlayer)
                        for rooms in self.rooms:
                            if rooms.getName() == self.getTile(x, y).getRoom():

                                rooms.setPlayer(self.playersTurn)

            if currentPlayer.getMoves() == 0:
                player = self.getCurrentPlayer()
                x, y = player.getLocation()
                self.possibleMoves = self.lookAround(x, y)
                self.unsetPossibleMoves(x, y)
        else: # player is in a room move to a tile
            if self.getTile(x, y).getPossibleMove() == True and self.getTile(x,y).getPlayer() == 0 and currentPlayer.getMoves() >= 1:
                tile = self.getTile(x, y)
                tile.setPlayer(currentPlayer.getPlayerID())
                tile.setSelected(False)
                tile.setPossibleMove(False)
                print(self.getTile(x, y).getPlayer())
                self.setTile(tile, x, y)
                currentPlayer.setMoves(currentPlayer.getMoves() - 1)
                currentPlayer.setLocation(x, y)
                self.setPlayer(currentPlayer)
                self.movePlayer()


    def main(self):
        done = False
        clock = pygame.time.Clock()
        pygame.display.set_icon(self.imgPlayer1)
        playerIds = []
        for p in self.Players:
            if p.getName() != False:
                playerIds.append(p.getPlayerID())
        for p in playerIds:
            print(p)
        self.deck.init()
        self.deck.initEnvelope()
        self.deck.shuffle()
        while self.deck.isCard():
            for p in self.Players:
                if p.getName() != False:  # or can use if p.getPlayerID() in playerIds:
                    if self.deck.isCard():
                        p.setCard(self.deck.drawCard())
        for p in self.Players:
            for card in p.cards:
                print(p.name, "has: ", card.card_name)

        self.board = self.initiateBoard()

        turnComplete = False
        turnCount = 0
        player = 0
        maxPlayer = len(playerIds) - 1

        # game loop
        while not done:
            playerObj = self.getCurrentPlayer()
            if playerObj.getName() == False:
                turnComplete = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # If user clicked close
                    done = True  # Flag that we are done so we exit this loop

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # User clicks the mouse. Get the position
                    pos = pygame.mouse.get_pos()
                    # Change the x/y screen coordinates to grid coordinates
                    row = (pos[0] - self.GRIDBUFFX) // self.WIDTH
                    column = (pos[1] - self.GRIDBUFFY) // self.HEIGHT
                    turnComplete = self.isButtonClicked(pos[0], pos[1])
                    currentPlayer = self.getCurrentPlayer()

                    if currentPlayer.getMoves() == 0:
                        x, y = currentPlayer.getLocation()
                        self.unsetPossibleMoves(x, y)
                    # Changes tile to selected / unselected
                    try:
                        self.movePlayerTile(int(row), int(column))

                        # self.board[int(column), int(row)].setSelected(not self.board[int(column), int(row)].getSelected())

                    except:
                        pass

            # Set the screen background
            self.screen.fill(self.GREEN)
            self.screen.blit(self.background, (self.GRIDBUFFX, self.GRIDBUFFY))
            self.screen.blit(self.title, (((950 / 2 - (int(563 * .45) / 2)) - 110), 7))
            self.screen.blit(self.textBoxPreviousTurn, (600, 20))

            # v menu
            if self.PLAYER1 != False:
                self.screen.blit(self.imgPlayer1, (730, 100))
            if self.PLAYER2 != False:
                self.screen.blit(self.imgPlayer2, (840, 100))
            if self.PLAYER3 != False:
                self.screen.blit(self.imgPlayer3, (730, 200))
            if self.PLAYER4 != False:
                self.screen.blit(self.imgPlayer4, (840, 200))
            if self.PLAYER5 != False:
                self.screen.blit(self.imgPlayer5, (730, 300))
            if self.PLAYER6 != False:
                self.screen.blit(self.imgPlayer6, (840, 300))

            self.screen.blit(self.buttonRollDice, (720, 400))
            self.screen.blit(self.buttonNextTurn, (720, 500))
            self.screen.blit(self.buttonGuess, (720, 600))
            self.screen.blit(self.buttonAccuse, (720, 700))
            self.screen.blit(self.buttonMenu, (10, 10))
            self.screen.blit(self.textPreviousTurn, (550, 10))
            self.screen.blit(self.textBoxPreviousTurn, (690, 20))

            # h menu
            self.screen.blit(self.buttonShowCards, (12, 812))
            self.screen.blit(self.cardBlank, (102, 812))  # 1
            self.screen.blit(self.cardBlank, (185, 812))  # 2
            self.screen.blit(self.cardBlank, (268, 812))  # 3
            self.screen.blit(self.cardBlank, (351, 812))  # 4
            self.screen.blit(self.cardBlank, (434, 812))  # 5
            self.screen.blit(self.cardBlank, (517, 812))  # 6
            self.screen.blit(self.cardBlank, (600, 812))  # 7
            self.screen.blit(self.cardBlank, (683, 812))  # 8
            self.screen.blit(self.cardBlank, (766, 812))  # 9

            # notepad
            self.screen.blit(self.buttonNotepad, (860, 812))

            # Change button to hover if mouse if over.
            x, y = pygame.mouse.get_pos()
            self.isButtonSelected(x, y)

            # Draw the grid
            self.drawGrid(self.board)

            clock.tick(60)  # set to 30 to half cycle speeds / reduce processing requirements
            pygame.display.flip()

            if turnComplete:
                turnCount += 1
                if self.playersTurn > maxPlayer:
                    self.playersTurn = 0
                else:
                    self.playersTurn += 1

                print("current Player ", turnCount)
                turnComplete = False

        # pygame.quit()

    def initiateBoard(self):
        # player1 = players[0]
        # player2 = players[1]
        # player3 = players[2]
        # player4 = players[3]
        # player5 = players[4]
        # player6 = players[5]

        """
            there are 27 possible tile states.
            str = study (room)
            har = hall (room)
            lor = lounge (room)
            drr = dining room (room)
            kir = kitchen (room)
            brr = ball room (room)
            cvr = conservatory (room)
            bir = billiards room (room)
            lir = library (room)
            std = study (door)
            had = hall (door)
            lod = lounge (door)
            drd = dining room (door)
            kid = kitchen (door)
            brd = ball room (door)
            cvd = conservatory (door)
            bid = billiards room (door)
            lid = library (door)
            wwe = walkway empty
            wwh = walkway hover
            wws = walkway select
            blk = blank
            ww1 = walkway player 1
            ww2 = walkway player 2
            ww3 = walkway player 3
            ww4 = walkway player 4
            ww5 = walkway player 5
            ww6 = walkway player 6
            """

        grid = [
            ["str", "str", "str", "str", "str", "str", "str", "wwe", "blk", "blk", "har", "har", "har", "har", "har",
             "blk", "wwe", "lor", "lor", "lor", "lor", "lor", "lor", "lor"],
            ["str", "str", "str", "str", "str", "str", "str", "wwe", "wwe", "har", "har", "har", "har", "har", "har",
             "wwe", "wwe", "lor", "lor", "lor", "lor", "lor", "lor", "lor"],
            ["str", "str", "str", "str", "str", "str", "str", "wwe", "wwe", "har", "har", "har", "har", "har", "har",
             "wwe", "wwe", "lor", "lor", "lor", "lor", "lor", "lor", "lor"],
            ["str", "str", "str", "str", "str", "str", "std", "wwe", "wwe", "har", "har", "har", "har", "har", "har",
             "wwe", "wwe", "lor", "lor", "lor", "lor", "lor", "lor", "lor"],
            ["blk", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "had", "har", "har", "har", "har", "har",
             "wwe", "wwe", "lor", "lor", "lor", "lor", "lor", "lor", "lor"],
            ["wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "har", "har", "har", "har", "har", "har",
             "wwe", "wwe", "lod", "lor", "lor", "lor", "lor", "lor", "lor"],
            ["blk", "lir", "lir", "lir", "lir", "lir", "wwe", "wwe", "wwe", "har", "har", "had", "had", "har", "har",
             "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "blk"],
            ["lir", "lir", "lir", "lir", "lir", "lir", "lir", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe",
             "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe"],
            ["lir", "lir", "lir", "lir", "lir", "lir", "lid", "wwe", "wwe", "blk", "blk", "blk", "blk", "blk", "wwe",
             "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "blk"],
            ["lir", "lir", "lir", "lir", "lir", "lir", "lir", "wwe", "wwe", "blk", "blk", "blk", "blk", "blk", "wwe",
             "wwe", "drr", "drd", "drr", "drr", "drr", "drr", "drr", "drr"],
            ["blk", "lir", "lir", "lid", "lir", "lir", "wwe", "wwe", "wwe", "blk", "blk", "blk", "blk", "blk", "wwe",
             "wwe", "drr", "drr", "drr", "drr", "drr", "drr", "drr", "drr"],
            ["blk", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "blk", "blk", "blk", "blk", "blk", "wwe",
             "wwe", "drr", "drr", "drr", "drr", "drr", "drr", "drr", "drr"],
            ["bir", "bid", "bir", "bir", "bir", "bir", "wwe", "wwe", "wwe", "blk", "blk", "blk", "blk", "blk", "wwe",
             "wwe", "drd", "drr", "drr", "drr", "drr", "drr", "drr", "drr"],
            ["bir", "bir", "bir", "bir", "bir", "bir", "wwe", "wwe", "wwe", "blk", "blk", "blk", "blk", "blk", "wwe",
             "wwe", "drr", "drr", "drr", "drr", "drr", "drr", "drr", "drr"],
            ["bir", "bir", "bir", "bir", "bir", "bir", "wwe", "wwe", "wwe", "blk", "blk", "blk", "blk", "blk", "wwe",
             "wwe", "drr", "drr", "drr", "drr", "drr", "drr", "drr", "drr"],
            ["bir", "bir", "bir", "bir", "bir", "bid", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe",
             "wwe", "wwe", "wwe", "wwe", "drr", "drr", "drr", "drr", "drr"],
            ["bir", "bir", "bir", "bir", "bir", "bir", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe",
             "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "blk"],
            ["blk", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "brr", "brd", "brr", "brr", "brr", "brr", "brd",
             "brr", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe"],
            ["wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "wwe", "brr", "brr", "brr", "brr", "brr", "brr", "brr",
             "brr", "wwe", "wwe", "kir", "kid", "kir", "kir", "kir", "brr"],
            ["blk", "cvr", "cvr", "cvr", "cvd", "wwe", "wwe", "wwe", "brd", "brr", "brr", "brr", "brr", "brr", "brr",
             "brd", "wwe", "wwe", "kir", "kir", "kir", "kir", "kir", "kir"],
            ["cvr", "cvr", "cvr", "cvr", "cvr", "cvr", "wwe", "wwe", "brr", "brr", "brr", "brr", "brr", "brr", "brr",
             "brr", "wwe", "wwe", "kir", "kir", "kir", "kir", "kir", "kir"],
            ["cvr", "cvr", "cvr", "cvr", "cvr", "cvr", "wwe", "wwe", "brr", "brr", "brr", "brr", "brr", "brr", "brr",
             "brr", "wwe", "wwe", "kir", "kir", "kir", "kir", "kir", "kir"],
            ["cvr", "cvr", "cvr", "cvr", "cvr", "cvr", "wwe", "wwe", "brr", "brr", "brr", "brr", "brr", "brr", "brr",
             "brr", "wwe", "wwe", "kir", "kir", "kir", "kir", "kir", "kir"],
            ["cvr", "cvr", "cvr", "cvr", "cvr", "cvr", "blk", "wwe", "wwe", "wwe", "brr", "brr", "brr", "brr", "wwe",
             "wwe", "wwe", "brr", "kir", "kir", "kir", "kir", "kir", "kir"],
            ["blk", "blk", "blk", "blk", "blk", "blk", "blk", "blk", "blk", "wwe", "blk", "blk", "blk", "blk", "wwe",
             "brr", "brr", "brr", "kir", "kir", "kir", "kir", "kir", "kir"]]

        for p in self.Players:

            if p.getName() != False and p.getPlayerID() == 1:
                grid[0][16] = "ww1"
                p.setLocation(16, 0)

            if p.getName() != False and p.getPlayerID() == 2:
                grid[7][23] = "ww2"
                p.setLocation(23, 7)

            if p.getName() != False and p.getPlayerID() == 3:
                grid[24][14] = "ww3"
                p.setLocation(14, 24)

            if p.getName() != False and p.getPlayerID() == 4:
                grid[24][9] = "ww4"
                p.setLocation(9, 24)

            if p.getName() != False and p.getPlayerID() == 5:
                grid[5][0] = "ww5"
                p.setLocation(0, 5)

            if p.getName() != False and p.getPlayerID() == 6:
                grid[18][0] = "ww6"
                p.setLocation(0, 18)

        rows, columns = 25, 24

        board = np.empty((rows, columns), dtype=object)
        r = room.room
        roomList = []  # ez fix ignore bs
        for row in range(25):
            for column in range(24):

                # rooms
                if grid[row][column] == "str":
                    board[row, column] = tile(room="study")
                    if not grid[row][column] in roomList:
                        roomList.append(grid[row][column])
                        self.rooms.append(r(board[row, column].getRoom()))

                if grid[row][column] == "har":
                    board[row, column] = tile(room="hall")
                    if not grid[row][column] in roomList:
                        roomList.append(grid[row][column])
                        self.rooms.append(r(board[row, column].getRoom()))

                if grid[row][column] == "lor":
                    board[row, column] = tile(room="lounge")
                    if not grid[row][column] in roomList:
                        roomList.append(grid[row][column])
                        self.rooms.append(r(board[row, column].getRoom()))

                if grid[row][column] == "drr":
                    board[row, column] = tile(room="dinning room")
                    if not grid[row][column] in roomList:
                        roomList.append(grid[row][column])
                        self.rooms.append(r(board[row, column].getRoom()))

                if grid[row][column] == "kir":
                    board[row, column] = tile(room="kitchen")
                    if not grid[row][column] in roomList:
                        roomList.append(grid[row][column])
                        self.rooms.append(r(board[row, column].getRoom()))

                if grid[row][column] == "brr":
                    board[row, column] = tile(room="ball room")
                    if not grid[row][column] in roomList:
                        roomList.append(grid[row][column])
                        self.rooms.append(r(board[row, column].getRoom()))

                if grid[row][column] == "cvr":
                    board[row, column] = tile(room="conservatory")
                    if not grid[row][column] in roomList:
                        roomList.append(grid[row][column])
                        self.rooms.append(r(board[row, column].getRoom()))

                if grid[row][column] == "bir":
                    board[row, column] = tile(room="billiards room")
                    if not grid[row][column] in roomList:
                        roomList.append(grid[row][column])
                        self.rooms.append(r(board[row, column].getRoom()))

                if grid[row][column] == "lir":
                    board[row, column] = tile(room="library")
                    if not grid[row][column] in roomList:
                        roomList.append(grid[row][column])
                        self.rooms.append(r(board[row, column].getRoom()))

        for row in range(25):
            for column in range(24):
                # doors
                print(row, column)
                if grid[row][column] == "std":
                    board[row, column] = tile(room="study", door=True, isTile=False)

                    for rooms in self.rooms:
                        print(rooms.getName())
                        if rooms.getName() == board[row, column].getRoom():
                            print("setdoor")
                            rooms.setDoors(column, row)

                if grid[row][column] == "had":
                    board[row, column] = tile(room="hall", door=True, isTile=False)
                    for rooms in self.rooms:
                        print(rooms.getName())
                        if rooms.getName() == board[row, column].getRoom():
                            print("setdoor")
                            rooms.setDoors(column, row)

                if grid[row][column] == "lod":
                    board[row, column] = tile(room="lounge", door=True, isTile=False)
                    for rooms in self.rooms:
                        print(rooms.getName())
                        if rooms.getName() == board[row, column].getRoom():
                            print("setdoor")
                            rooms.setDoors(column, row)

                if grid[row][column] == "drd":
                    board[row, column] = tile(room="dinning room", door=True, isTile=False)
                    for rooms in self.rooms:
                        print(rooms.getName())
                        if rooms.getName() == board[row, column].getRoom():
                            print("setdoor")
                            rooms.setDoors(column, row)

                if grid[row][column] == "kid":
                    board[row, column] = tile(room="kitchen", door=True, isTile=False)
                    for rooms in self.rooms:
                        print(rooms.getName())
                        if rooms.getName() == board[row, column].getRoom():
                            print("setdoor")
                            rooms.setDoors(column, row)

                if grid[row][column] == "brd":
                    board[row, column] = tile(room="ball room", door=True, isTile=False)
                    for rooms in self.rooms:
                        print(rooms.getName())
                        if rooms.getName() == board[row, column].getRoom():
                            print("setdoor")
                            rooms.setDoors(column, row)

                if grid[row][column] == "cvd":
                    board[row, column] = tile(room="conservatory", door=True, isTile=False)
                    for rooms in self.rooms:
                        print(rooms.getName())
                        if rooms.getName() == board[row, column].getRoom():
                            print("setdoor")
                            rooms.setDoors(column, row)

                if grid[row][column] == "bid":
                    board[row, column] = tile(room="billiards room", door=True, isTile=False)
                    for rooms in self.rooms:
                        print(rooms.getName())
                        if rooms.getName() == board[row, column].getRoom():
                            print("setdoor")
                            rooms.setDoors(column, row)

                if grid[row][column] == "lid":
                    board[row, column] = tile(room="library", door=True, isTile=False)
                    for rooms in self.rooms:
                        print(rooms.getName())
                        if rooms.getName() == board[row, column].getRoom():
                            print("setdoor")
                            rooms.setDoors(column, row)

                # walkways
                if grid[row][column] == "wwe":
                    board[row, column] = tile(room="tile", isTile=True)

                if grid[row][column] == "ww1":
                    board[row, column] = tile(room="tile", isTile=True, player=1)

                if grid[row][column] == "ww2":
                    board[row, column] = tile(room="tile", isTile=True, player=2)

                if grid[row][column] == "ww3":
                    board[row, column] = tile(room="tile", isTile=True, player=3)

                if grid[row][column] == "ww4":
                    board[row, column] = tile(room="tile", isTile=True, player=4)

                if grid[row][column] == "ww5":
                    board[row, column] = tile(room="tile", isTile=True, player=5)

                if grid[row][column] == "ww6":
                    board[row, column] = tile(room="tile", isTile=True, player=6)

                # blank cells
                if grid[row][column] == "blk":
                    board[row, column] = tile(blank=True)

        for r in self.rooms:
            print(r.getName(), " doors:", r.getDoors())
        return board


playerList = ["shakir", "bob", "abby", "tom", "alex", False, ]
b = board(playerList, 2).main()
