import card as card


class suspect_cards:
    suspect_list = ('miss_scarlet', 'mrs_white', 'colonel_mustard', 'reverend_green', 'professor_plum', 'mrs_peacock')
    arr_suspect_cards = []

    def __init__(self):
        for l in self.suspect_list:
            img_name = '../Image/' + l + '.jpg'

            self.arr_suspect_cards.append(card(img_name))



