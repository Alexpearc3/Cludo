import room_cards as roomCards
import suspect_cards as susCards
import weapon_cards as weaponCards
import random
import card as card


class Deck:
    weapon_cards = []
    sus_cards = []
    weapon_cards = []
    envelope = []
    all_cards = []

    def __init__(self, roomCards=roomCards, susCards=susCards, weaponCards=weaponCards):
        self.room_cards = roomCards.get()
        self.sus_cards = susCards.get()
        self.weapon_cards = weaponCards.get()
        self.envelope()
        self.shuffle()

    def envelope(self):
        i = random.randint(0, len(self.weapon_cards))
        self.envelope.append(self.weapon_cards[i])
        self.weapon_cards.remove(i)

        i = random.randint(0, len(self.sus_cards))
        self.envelope.append(self.sus_cards[i])
        self.sus_cards.remove(i)

        i = random.randint(0, len(self.room_cards))
        self.envelope.append(self.room_cards[i])
        self.room_cards.remove(i)

    def shuffle(self):
        while self.weapon_cards != 0 and self.sus_cards != 0 and self.room_cards != 0:
            if len(self.weapon_cards) != 0:
                i = random.randint(0, len(self.weapon_cards))
                self.all_cards.append(self.weapon_cards[i])
                self.weapon_cards.remove(i)
            if len(self.sus_cards) != 0:
                i = random.randint(0, len(self.sus_cards))
                self.all_cards.append(self.sus_cards[i])
                self.sus_cards.remove(i)
            if len(self.room_cards) != 0:
                i = random.randint(0, len(self.room_cards))
                self.all_cards.append(self.room_cards[i])
                self.room_cards.remove(i)
    def drawCard(self):
        if len(self.all_Cards) != 0:
            i = random.randint(0, len(self.all_Cards))
            draw = self.all_cards[i]
            self.all_cards.remove(i)
            return draw
