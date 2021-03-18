import pygame


class Card:
    # what attributes do i need?
    image_name = ""
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0

    def init(self, image_name):
        self.image_name = image_name

    def __init__(self):
        self.image_name = "blank"
        # image = pygame.image.load(self.image_name)
