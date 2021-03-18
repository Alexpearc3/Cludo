import room_cards as roomCards
import suspect_cards as susCards
import weapon_cards as weaponCards
import random
import card as card


class Deck:
    weapon_cards = []
    suspect_cards = []
    room_cards = []
    envelope = []
    all_cards = []
    def init(self):
        print("init")
        rc = roomCards.Room_cards.get(self)
        sc = susCards.Suspect_cards.get(self)
        wc = weaponCards.Weapon_cards.get(self)
        self.room_cards = rc
        self.sus_cards = sc
        self.weapon_cards = wc
        self.initEnvelope(self)
        self.shuffle(self)

    def __init__(self):
        print("init")

        rc = roomCards.Room_cards.get(self)
        sc = susCards.Suspect_cards.get(self)
        wc = weaponCards.Weapon_cards.get(self)
        self.room_cards = rc
        self.sus_cards = sc
        self.weapon_cards = wc


    def initEnvelope(self):
        i = random.randint(0, len(self.weapon_cards))
        print(i)
        self.envelope.append(self.weapon_cards[i])
        self.weapon_cards.remove(i)

        i = random.randint(0, len(self.suspect_cards))
        self.envelope.append(self.suspect_cards[i])
        self.suspect_cards.remove(i)

        i = random.randint(0, len(self.room_cards))
        self.envelope.append(self.room_cards[i])
        self.room_cards.remove(i)

    def shuffle(self):
        while self.weapon_cards != 0 and self.suspect_cards != 0 and self.room_cards != 0:
            if len(self.weapon_cards) != 0:
                i = random.randint(0, len(self.weapon_cards))
                self.all_cards.append(self.weapon_cards[i])
                self.weapon_cards.remove(i)
            if len(self.sus_cards) != 0:
                i = random.randint(0, len(self.suspect_cards))
                self.all_cards.append(self.suspect_cards[i])
                self.suspect_cards.remove(i)
            if len(self.room_cards) != 0:
                i = random.randint(0, len(self.room_cards))
                self.all_cards.append(self.room_cards[i])
                self.room_cards.remove(i)

    def drawCard(self):
        if len(self.all_cards) != 0:
            print(len(self.all_cards))
            i = random.randint(0, len(self.all_cards))
            draw = self.all_cards[i]
            self.all_cards.remove(i)
            return draw
        else:
            return False

    def getAllCards(self):
        return self.all_cards

d = Deck
d.init(d)
print("test")
print("test", d.drawCard(d))