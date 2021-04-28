
class Player:

    def __init__(self, player_name, player_ID, notepad):
        do = "what a player do"
        self.cards = []
        self.name = player_name
        self.locationX = 0 #start_location #2d array value e.g. [0][0] can find room details from tile details
        self.locationY = 0
        self.pId = player_ID
        self.accusations = 1
        self.hasWon = False
        self.moves = -1
        self.hasRolled = False
        self.notepad = notepad
        self.room = False


    def setCard(self, card):
        self.cards.append(card)

    def getCards(self):
        return self.cards

    def setLocation(self, x, y):
        self.locationX = x
        self.locationY = y

    def accuse(self):
        #check envelope
        self.accusations = self.accusations - 1

    def getName(self):
        return self.name

    def hasWon(self):
        return self.hasWon

    def setWin(self):
        self.hasWon = True

    def getLocation(self):
        return self.locationX, self.locationY

    def getPlayerID(self):
        return self.pId

    def setMoves(self, moves):
        self.moves = moves

    def getMoves(self):
        return self.moves

    def setRolled(self, rolled):
        self.hasRolled = rolled

    def getRolled(self):
        return self.hasRolled

    def getNotepad(self):
        return self.notepad

    def getRoom(self):
        return self.room

    def setRoom(self, room):
        self.room = room