import card


class Suspect_cards:
    suspect_list = ('Miss Scarlet', 'Mrs White', 'Colonel Mustard', 'Reverend Green', 'Professor Plum', 'Mrs Peacock')
    suspect_cards = []

    def __init__(self):
        for l in self.suspect_list:
            img_name = '../Image/' + self.procStr(l) + '.jpg'
            c = card.Card
            self.suspect_cards.append(c.init())

    def get(self):
        return self.suspect_cards

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
# sc = Suspect_cards
# for l in sc.getSuspects(sc):
#     print(l)

