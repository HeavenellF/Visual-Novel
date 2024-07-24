import pygame

class Setting:
    def __init__(self):
        self.screen_width = 0
        self.screen_height = 0
        self.multiplier = 10

        self.update_display_info()

    def update_display_info(self):
        display_info = pygame.display.Info()
        self.screen_width = display_info.current_w
        self.screen_height = display_info.current_h

    def get_dimensions(self):
        return self.screen_width, self.screen_height

    def resize_display(self, width, height):
        self.multiplier = int(self.multiplier * (width / self.screen_width))
        pygame.display.set_mode((width, height), pygame.RESIZABLE)
        self.update_display_info()

    def to_fullscreen(self):
        self.multiplier = 10
        pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.update_display_info()
        