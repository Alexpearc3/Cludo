import pygame
class card:
    image_name = ""
    #what properties do i need?
    var1 = 0
    var2 = 0
    var3 = 0
    var4 = 0
    def __init__(self,image_name):
        self.image_name = image_name
        image = pygame.image.load(self.image_name)
