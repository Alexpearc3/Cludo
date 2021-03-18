import string

import card


class Room_cards:
    room_list = ('Billiard room', 'Study', 'Hall', 'Lounge', 'Dining room', 'Ballroom', 'Conservatory', 'Library', 'Kitchen')
    room_cards = []

    def __init__(self):
        self.room_cards = []
        for l in self.room_list:
            img_name = '../Image/' + self.procStr(l) + '.jpg'
            c = card.Card
            self.room_cards.append(c.init(self.procStr(img_name)))

    def get(self):
        return self.room_cards

    def getRooms(self):
        return self.room_list

    def procStr(self, str):
        newStr = ""
        for c in str:
            if c == " ":
                c = "_"
            newStr += c.lower()
        return newStr

#test/ example implementation
# rc = Room_cards
# for l in rc.getRooms(rc):
#     print(l)
