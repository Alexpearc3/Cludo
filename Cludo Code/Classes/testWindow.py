import pygame
from pygame.event import Event
from pygame.rect import Rect

from src import Constants
from src.Interfaces.RenderObject import RenderObject
from src.Scenes import Scene
from src.UI.MultilineTextLabel import MultilineTextLabel


class PopupNotify(RenderObject):
    __slots__ = ("_bg_image", "_time_to_kill", "__start_time", "__text_label")

    def __init__(self, parent: Scene, time_to_kill: int = 3, text: str = "") -> None:
        self._rect = PopupNotify._check_position()
        RenderObject.__init__(self, parent=parent, position=(self._rect.x, self._rect.y))
        self._bg_image = None
        self.set_background("{0}/popup1.png".format(self._res_dir))
        self._time_to_kill = time_to_kill
        self.__start_time = pygame.time.get_ticks()
        self.__text_label = MultilineTextLabel(parent=self, text=text, position=(20, 20), font_size=14, bold=True,
                                               line_length=self.bg_rect.width - 20 * 2)
        self.set_text(text=text)
        self.show()

    @staticmethod
    def _check_position() -> Rect:
        popup_width = 200
        popup_height = 70
        mouse_pos = pygame.mouse.get_pos()
        popup_pos = [0, 0]
        if mouse_pos[0] + popup_width + 20 > Constants.WINDOW_W:
            popup_pos[0] = mouse_pos[0] - popup_width
        else:
            popup_pos[0] = mouse_pos[0]

        popup_pos[1] = mouse_pos[1] - popup_height
        if popup_pos[1] < 0:
            popup_pos[1] += popup_height

        correct_position = Rect(popup_pos[0], popup_pos[1], popup_width, popup_height)
        return correct_position

    @property
    def bg_rect(self) -> Rect:
        return self._bg_image.get_rect()

    def set_background(self, path_to_image: str) -> None:
        self._bg_image = pygame.image.load(path_to_image).convert_alpha()
        self._rect.width = self._bg_image.get_rect().width
        self._rect.height = self._bg_image.get_rect().height

    def set_text(self, text: str) -> None:
        self.__text_label.set_position((self.position[0] + 15, self.position[1] + 10))
        self.__text_label.set_text(text)

    def show(self) -> None:
        super().show()
        self.parent.add_render(self)

    def destroy(self) -> None:
        self.parent.remove_render(self)

    def handle_event(self, event: Event) -> None:
        pass

    def update(self, dt: float) -> None:
        if self._time_to_kill != 0:
            mills = (pygame.time.get_ticks() - self.__start_time) / 1000
            if mills >= self._time_to_kill:
                self.destroy()

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self._bg_image, self._rect)
        self.__text_label.draw(screen)
