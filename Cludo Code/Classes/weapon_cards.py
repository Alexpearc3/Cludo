import card


class Weapon_cards:
    weapon_list = ('Wrench', 'Candlestick', 'Lead pipe', 'Rope', 'Revolver', 'Knife')
    weapon_cards = []

    def __init__(self):
        for l in self.weapon_list:
            img_name = '../Image/' + self.procStr(l) + '.jpg'
            c = card.Card
            self.weapon_cards.append(c.init(self.procStr(img_name)))

    def get(self):
        return self.weapon_cards

    def getWeapons(self):
        return self.weapon_list

    def procStr(self,str):
        newStr = ""
        for c in str:
            if c == " ":
                c = "_"
            newStr += c.lower()
        return newStr
#test/ example implementation
# wc = Weapon_cards
# for l in wc.getWeapons(wc):
#     print(l)
