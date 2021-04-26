import string

import card


class Room_cards:
    room_list = (
        'Billiard room',
        'Study',
        'Hall',
        'Lounge',
        'Dining room',
        'Ballroom',
        'Conservatory',
        'Library',
        'Kitchen')

    def __init__(self):
        self.room_cards = []
        for card_name in self.getNames():
            img_name = '../Image/' + self.procStr(card_name) + '.jpg'
            self.setCards(self.procStr(img_name), card_name)

    # returns room_list  'Billiard room', 'Study', 'Hall', 'Lounge', 'Dining room', 'Ballroom', 'Conservatory', 'Library', 'Kitchen'
    def getNames(self):
        return self.room_list

    # returns room card instances
    def getCards(self):
        return self.room_cards

    # sets room card instances
    def setCards(self, img_name, card_name):
        self.room_cards.append(card.Card(img_name, card_name))

    # processes room names into image location for the room card image
    def procStr(self, str):
        newStr = ""
        for c in str:
            if c == " ":
                c = "_"
            newStr += c.lower()
        return newStr

    # removes a card from this instance
    def removeCard(self, i):
        self.room_cards.remove(i)

# test/ example implementation
# rc = Room_cards()
# #rc.init()
# for card in rc.getCards():
#     print(card.image_name, "  ", card.card_name)
