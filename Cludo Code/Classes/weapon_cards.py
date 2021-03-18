import card


class Weapon_cards:
    weapon_list = ('Wrench', 'Candlestick', 'Lead pipe', 'Rope', 'Revolver', 'Knife')

    #def init(self):


    def __init__(self):
        self.weapon_cards = []
        for card_name in self.getNames():
            # print(card_name)
            img_name = '../Image/' + self.procStr(card_name) + '.jpg'

            self.setCards(self.procStr(img_name), card_name)
        do = "smth"
        # for l in self.getRoomNames():
        #     img_name = '../Image/' + self.procStr(l) + '.jpg'
        #     print(img_name)
        #     c = card.Card
        #     self.room_cards.append(c(self.procStr(img_name)))

    def getNames(self):
        return self.weapon_list

    def getCards(self):
        return self.weapon_cards

    def setCards(self, img_name, card_name):
        self.weapon_cards.append(card.Card(img_name, card_name))

    def procStr(self, str):
        newStr = ""
        for c in str:
            if c == " ":
                c = "_"
            newStr += c.lower()
        return newStr

    def removeCard(self, i):
        self.weapon_cards.remove(i)

# test/ example implementation
# wc = Weapon_cards
# wc.init(wc)
# for card in wc.getCards(wc):
#     print(card.image_name, "  ", card.card_name)
