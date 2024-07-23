import pygame

class DialogueBox:
    def __init__(self, x, y, width, height, background_color=(0, 0, 0)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.background_color = background_color
        self.name = ""
        self.dialogue = ""
        self.font = pygame.font.Font(None, 32)

    def set_name(self, name):
        self.name = name
    def set_dialogue(self, dialogue):
        self.dialogue = dialogue

    def draw(self, screen):
        # Draw the background box
        pygame.draw.rect(screen, self.background_color, (self.x, self.y, self.width, self.height))
        
        # Render the name text
        name_surface = self.font.render(self.name, True, (255, 255, 255))
        screen.blit(name_surface, (self.x + 10, self.y + 5))  # Example padding
        
        # Render the dialogue text
        dialogue_surface = self.font.render(self.dialogue, True, (255, 255, 255))
        screen.blit(dialogue_surface, (self.x + 10, self.y + 40))  # Adjust as needed