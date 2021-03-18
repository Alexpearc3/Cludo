import string

import card


class Room_cards:
    room_cards = []
    room_list = (
        'Billiard room', 'Study', 'Hall', 'Lounge', 'Dining room', 'Ballroom', 'Conservatory', 'Library', 'Kitchen')

    def init(self):
        for card_name in self.getNames(self):
            # print(card_name)
            img_name = '../Image/' + self.procStr(self, card_name) + '.jpg'
            self.setCards(self, self.procStr(self, img_name), card_name)

    def __init__(self):

        do = "smth"
        # for l in self.getRoomNames():
        #     img_name = '../Image/' + self.procStr(l) + '.jpg'
        #     print(img_name)
        #     c = card.Card
        #     self.room_cards.append(c(self.procStr(img_name)))

    def getNames(self):
        return self.room_list

    def getCards(self):
        return self.room_cards

    def setCards(self, img_name, card_name):
        self.room_cards.append(card.Card(img_name, card_name))

    def procStr(self, str):
        newStr = ""
        for c in str:
            if c == " ":
                c = "_"
            newStr += c.lower()
        return newStr

    def removeCard(self, i):
        self.room_cards.remove(self, i)


# test/ example implementation
# rc = Room_cards
# rc.init(rc)
# for card in rc.getCards(rc):
#     print(card.image_name, "  ", card.card_name)
