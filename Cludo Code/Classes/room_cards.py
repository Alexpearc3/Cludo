import card as card


class room_cards:
    room_list = ('billiard_room', 'study', 'hall', 'lounge', 'dining_room', 'ballroom', 'conservatory', 'library', 'kitchen')
    arr_room_cards = []

    def __init__(self):
        for l in self.room_list:
            img_name = '../Image/' + l + '.jpg'

            self.arr_room_cards.append(card(img_name))



