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

            self.rectg = pg.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)

            if self.text != '':
                font = pg.font.SysFont(None, 40)
                text = font.render(self.text, 1, (0, 0, 0))
                screen.blit(text, (
                self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

        def event(self, screen, event):
            pos = pg.mouse.get_pos()
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.rectg.collidepoint(pos):
                    self.color = (250, 10, 0)
                    self.text = "Confirmed"
                    self.draw(screen, outline=None)
                    return True

            return False
