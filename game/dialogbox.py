import pygame

class DialogueBox:
    def __init__(self, x, y, width, height, background_color=(0, 0, 0), setting=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.background_color = background_color
        self.name = ""
        self.dialogue = ""
        self.font_name = pygame.font.Font(None, int(4.8*setting.multiplier))
        self.font_dialogue = pygame.font.Font(None, int(3.2*setting.multiplier))
        self.setting = setting
        self.name_position = (self.x + int(1*setting.multiplier), self.y + int(1*setting.multiplier))

    def set_name(self, name):
        self.name = name
    def set_dialogue(self, dialogue):
        self.dialogue = dialogue

    def draw(self, screen):
        # Create a surface with an alpha channel
        background_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        
        # Fill the surface with the background color and set its alpha value
        background_surface.fill((*self.background_color, 100))  # 128 is the alpha value (0-255)
        screen.blit(background_surface, (self.x, self.y))
        
        # Render the name text
        name_surface = self.font_name.render(self.name, True, (255, 255, 255))
        screen.blit(name_surface, self.name_position)  # padding from the top and left
        
        # Render the dialogue text with word wrapping
        dialogue_lines = self.wrap_text(self.dialogue, self.font_dialogue, self.width - int(6*self.setting.multiplier))
        y_offset = self.y + int(6*self.setting.multiplier)  # padding from the top
        for line in dialogue_lines:
            dialogue_surface = self.font_dialogue.render(line, True, (255, 255, 255))
            screen.blit(dialogue_surface, (self.x + int(3*self.setting.multiplier), y_offset))
            y_offset += self.font_dialogue.get_height() + int(1*self.setting.multiplier)  # Move to the next line


    def wrap_text(self, text, font, max_width):
        words = text.split(' ')
        lines = []
        current_line = ''
        for word in words:
            test_line = f'{current_line} {word}'.strip()
            test_width, _ = font.size(test_line)
            if test_width <= max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word
        lines.append(current_line)  # Add the last line
        return lines