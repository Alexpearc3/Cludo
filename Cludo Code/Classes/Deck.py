import room_cards as roomCards
import suspect_cards as susCards
import weapon_cards as weaponCards
import random
import card as card


class Deck:
    suspect_cards = []
    room_cards = []
    weapon_cards = []
    envelope = []
    all_cards = []

    def init(self):
        rc = roomCards.Room_cards()
        sc = susCards.Suspect_cards()
        wc = weaponCards.Weapon_cards()
        self.room_cards = roomCards.Room_cards.getCards(rc)
        self.suspect_cards = susCards.Suspect_cards.getCards(sc)
        self.weapon_cards = weaponCards.Weapon_cards.getCards(wc)

    def __init__(self):
        self.rc = roomCards.Room_cards
        self.weapon_cards = []
        self.suspect_cards = []
        self.room_cards = []
        self.envelope = []
        self.all_cards = []

    def initEnvelope(self):
        i = random.randint(1, len(self.weapon_cards)) - 1
        self.envelope.append(self.weapon_cards[i])
        self.weapon_cards.pop(i)

        i = random.randint(1, len(self.suspect_cards)) - 1
        self.envelope.append(self.suspect_cards[i])
        self.suspect_cards.pop(i)

        i = random.randint(1, len(self.room_cards)) - 1
        self.envelope.append(self.room_cards[i])
        self.room_cards.pop(i)

    def shuffle(self):
        while len(self.weapon_cards) != 0 and len(self.suspect_cards) != 0 and len(self.room_cards) != 0:
            if len(self.weapon_cards) != 0:
                i = random.randint(1, len(self.weapon_cards)) - 1
                self.all_cards.append(self.weapon_cards[i])
                self.weapon_cards.pop(i)

            if len(self.suspect_cards) != 0:
                i = random.randint(1, len(self.suspect_cards)) - 1
                self.all_cards.append(self.suspect_cards[i])
                self.suspect_cards.pop(i)

            if len(self.room_cards) != 0:
                i = random.randint(1, len(self.room_cards)) - 1
                self.all_cards.append(self.room_cards[i])
                self.room_cards.pop(i)

    def drawCard(self):
        i = random.randint(1, len(self.all_cards)) - 1
        draw = self.all_cards[i]
        self.all_cards.pop(i)
        return draw

    def isCard(self):
        if len(self.all_cards) == 0:
            return False
        return True

    def getAllCards(self):
        return self.all_cards

# test/ example implementation
d = Deck
d.init(d)
print("--room cards--")
for card in d.room_cards:
    print(card.card_name)
print(" ")

print("--suspect cards--")
for card in d.suspect_cards:
    print(card.card_name)
print(" ")

print("--weapon cards--")
for card in d.weapon_cards:
    print(card.card_name)
print(" ")

d.initEnvelope(d)
print("--enveloped cards--")
for card in d.envelope:
    print(card.card_name)
print(" ")

print("--All remaining cards shuffled --")
d.shuffle(d)
for card in d.all_cards:
    print(card.card_name)
print(" ")

print("--draws cards--")
cards = [d.drawCard(d),d.drawCard(d),d.drawCard(d),d.drawCard(d)]
for card in cards:
    print(card.card_name)
print(" ")

print("--all cards after drawing cards--")
for card in d.all_cards:
    print(card.card_name)
print(" ")
