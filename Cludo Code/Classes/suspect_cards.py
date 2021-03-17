import card as card


class suspect_cards:
    suspect_list = ('Miss Scarlet', 'Mrs White', 'Colonel Mustard', 'Reverend Green', 'Professor Plum', 'Mrs Peacock')
    arr_suspect_cards = []

    def __init__(self):
        for l in self.suspect_list:
            img_name = '../Image/' + l + '.jpg'

            self.arr_suspect_cards.append(card(self.procStr(img_name)))

    def get(self):
        return self.arr_suspect_cards

    def getSuspects(self):
        return self.suspect_list

    def procStr(self, str):
        newStr = ""
        for c in str:
            if c == " ":
                c = "_"
            newStr += c.lower()
        return newStr

#test/ example implementation
sc = suspect_cards
for l in sc.getSuspects(sc):
    print(l)

