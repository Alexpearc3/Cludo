import Player as player
import Deck

d = Deck.Deck()
d.init()
d.initEnvelope()
d.shuffle()

# test/ example implementation
d = Deck.Deck()
d.init()
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

d.initEnvelope()
print("--enveloped cards--")
for card in d.envelope:
    print(card.card_name)
print(" ")

print("--All remaining cards shuffled --")
d.shuffle()
for card in d.all_cards:
    print(card.card_name)
print(" ")

# print("--draws cards--")
# cards = []
# while d.isCard():
#     cards.append(d.drawCard())
# for card in cards:
#     print(card.card_name)
# print(" ")
#
# print("--all cards after drawing cards--")
# for card in d.all_cards:
#     print(card.card_name)
# print(" ")
#
#
Pl = player.Player
pla = [Pl("Shakir", "bhagdad", 911), Pl("michelle", "shakirs", 1), Pl("Alex", "yourmum", 69), Pl("Tom", "???", 1337),
       Pl("Abby", "Toilet paper", 1234)]
while d.isCard():
    for p in pla:
        if d.isCard():
            p.setCard(d.drawCard())
for p in pla:
    for card in p.cards:
        print(p.name, "has: ", card.card_name)
