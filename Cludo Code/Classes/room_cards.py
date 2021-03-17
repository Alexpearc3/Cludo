import string

import card as card


class room_cards:
    room_list = ('Billiard room', 'Study', 'Hall', 'Lounge', 'Dining room', 'Ballroom', 'Conservatory', 'Library', 'Kitchen')
    #arr_room_cards = []

    def __init__(self):
        self.arr_room_cards = []
        for l in self.room_list:
            img_name = '../Image/' + l + '.jpg'

            self.arr_room_cards.append(card(self.procStr(img_name)))

    def get(self):
        return self.arr_room_cards

    def getRooms(self):
        return self.room_list

    def procStr(self,str):
        newStr = ""
        for c in str:
            if c == " ":
                c = "_"
            newStr += c.lower()
        return newStr

#test/ example implementation
rc = room_cards
for l in rc.getRooms(rc):
    print(l)
