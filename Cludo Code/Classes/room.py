
class room:
    def __init__(self, name):
        self.name = name
        self.doors = []
        self.players = []

    def getDoors(self):
        return self.doors

    def getName(self):
        return self.name

    def setDoors(self, doorLocationX, doorLocationY):
        self.doors.append([doorLocationX, doorLocationY])

    def getPlayers(self):
        return self.players

    def setPlayers(self, player):
        self.players.append(player)





