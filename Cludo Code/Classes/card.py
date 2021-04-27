class Card:
    def __init__(self, image_name, card_name):
        self.image_name = image_name
        self.card_name = card_name

    def getName(self):
        return self.card_name

    def getImgName(self):
        return self.image_name