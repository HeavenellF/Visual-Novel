import pygame

from game.ui.dialogbox import DialogueBox

class Setting:

    instance = None

    font_index = pygame.font.get_fonts().index('comicsansms')
    font_max_index = len(pygame.font.get_fonts()) - 1
    print(f"Font Max Index: {font_max_index}")
    font = 'comicsansms'

    def __init__(self):
        self.screen_width = 0
        self.screen_height = 0
        self.multiplier = 10

        self.update_display_info()
        Setting.instance = self

    def update_display_info(self):
        display_info = pygame.display.Info()
        self.screen_width = display_info.current_w
        self.screen_height = display_info.current_h

    def get_dimensions(self):
        return self.screen_width, self.screen_height

    def resize_display(self, width, height):
        self.multiplier = int(self.multiplier * (width / self.screen_width))
        pygame.display.set_mode((width, height))
        self.update_display_info()

    def to_fullscreen(self):
        self.multiplier = 10
        pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.update_display_info()


    def change_font(self):
        cls = self.__class__
        cls.font = pygame.font.get_fonts()[cls.font_index]
        DialogueBox.instance.change_font()

    @classmethod
    def change_font_next(cls):
        cls.font_index += 1
        if cls.font_index > cls.font_max_index:
            cls.font_index = 0
        cls.instance.change_font()

    @classmethod
    def change_font_prev(cls):
        cls.font_index -= 1
        if cls.font_index < 0:
            cls.font_index = cls.font_max_index
        cls.instance.change_font()