import pygame

class Button:

    instances = []

    def __init__(self, name, x, y, image, action=None, setting=None):
        self.name = name
        self.image = image
        self.rect = image.get_rect()
        self.rect.topleft = (x, y)
        self.action = action
        self.setting = setting

        Button.instances.append(self)

    def draw(self, screen):
        font = pygame.font.SysFont(self.setting.instance.font, int(2*self.setting.multiplier))
        text_surf  = font.render(self.name, True, (0,0,0))
        text_rect = text_surf.get_rect(center = self.rect.center)
        screen.blit(self.image, self.rect)
        screen.blit(text_surf, text_rect)
        
    def handle(self):
        if self.action: 
            self.action()