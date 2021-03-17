import card as card


class weapon_cards:
    weapon_list = ('Wrench', 'Candlestick', 'Lead pipe', 'Rope', 'Revolver', 'Knife')
    arr_weapon_cards = []

    def __init__(self):
        for l in self.weapon_list:
            img_name = '../Image/' + l + '.jpg'

            self.arr_weapon_cards.append(card(self.procStr(img_name)))

    def get(self):
        return self.arr_weapon_cards

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
wc = weapon_cards
for l in wc.getWeapons(wc):
    print(l)
