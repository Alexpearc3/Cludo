import card


class Suspect_cards:
    suspect_list = ('Miss Scarlet', 'Mrs White', 'Colonel Mustard', 'Reverend Green', 'Professor Plum', 'Mrs Peacock')
    suspect_cards = []
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
        return self.suspect_list

    def getCards(self):
        return self.suspect_cards

    def setCards(self, img_name, card_name):
        self.suspect_cards.append(card.Card(img_name, card_name))

    def procStr(self, str):
        newStr = ""
        for c in str:
            if c == " ":
                c = "_"
            newStr += c.lower()
        return newStr

    def removeCard(self, i):
        self.suspect_cards.remove(self, i)


# test/ example implementation
# sc = Suspect_cards
# sc.init(sc)
# for card in sc.getCards(sc):
#     print(card.image_name, "  ", card.card_name)
