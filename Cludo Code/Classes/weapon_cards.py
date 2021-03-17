import card as card


class weapon_cards:
    weapon_list = ('wrench', 'candlestick', 'lead_pipe', 'rope', 'revolver', 'knife')
    arr_weapon_cards = []

    def __init__(self):
        for l in self.weapon_list:
            img_name = '../Image/' + l + '.jpg'

            self.arr_weapon_cards.append(card(img_name))

    def get(self):
        return self.arr_weapon_cards

