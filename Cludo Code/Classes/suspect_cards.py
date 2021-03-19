import card


class Suspect_cards:
    suspect_list = ('Miss Scarlet', 'Mrs White', 'Colonel Mustard', 'Reverend Green', 'Professor Plum', 'Mrs Peacock')

    def __init__(self):
        self.suspect_cards = []
        for card_name in self.getNames():
            img_name = '../Image/' + self.procStr(card_name) + '.jpg'
            self.setCards(self.procStr(img_name), card_name)

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
        self.suspect_cards.remove(i)


# test/ example implementation
# sc = Suspect_cards
# sc.init(sc)
# for card in sc.getCards(sc):
#     print(card.image_name, "  ", card.card_name)
