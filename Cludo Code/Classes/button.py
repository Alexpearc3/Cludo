import pygame as pg
import Deck
import suspect_cards
import room_cards
import weapon_cards
import Player as player
import dropdown


class Button:
        def __init__(self, color, x, y, width, height, text=''):
            self.color = color
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.text = text

        def draw(self, screen, outline=None):
        # Call this method to draw the button on the screen
            if outline:
                pg.draw.rect(screen, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

            pg.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)

            if self.text != '':
                font = pg.font.SysFont(None, 40)
                text = font.render(self.text, 1, (0, 0, 0))
                screen.blit(text, (
                self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

        def event(self, event):
            # Pos is the mouse position or a tuple of (x,y) coordinates
            x, y = pg.mouse.get_pos()
            if event.type == pg.MOUSEBUTTONDOWN:
                if pg.mouse.get_pressed()[0]:
                    self.size = self.text.get_size()
                    self.rect = pg.Rect(self.x, self.y, self.size[0], self.size[1])
                    if self.rect.collidepoint(x, y):
                        if pos[0] > self.x and pos[0] < self.x + self.width:
                            if pos[1] > self.y and pos[1] < self.y + self.height:
                                self.color = (0, 0, 0)
                                self.text = "confirmed"
                                self.draw(screen, outline=None)
                                return True

            return False


# def change_text(self, text, bg="black"):
    #     self.text = self.font.render(text, 1, pg.Color("Black"))
    #     self.size = self.text.get_size()
    #     self.surface = pg.Surface(self.size)
    #     self.surface.fill(bg)
    #     self.surface.blit(self.text, (0, 0))
    #     self.rect = pg.Rect(self.x, self.y, self.size[0], self.size[1])

# def click(self, event):
    #     x, y = pg.mouse.get_pos()
    #     if event.type == pg.MOUSEBUTTONDOWN:
    #         if pg.mouse.get_pressed()[0]:
    #             if self.rect.collidepoint(x, y):
    #                 self.change_text(self.feedback, bg="red")
