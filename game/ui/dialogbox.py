import pygame

class DialogBox:

    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(DialogBox, cls).__new__(cls)
        return cls.instance

    def __init__(self, x=0, y=0, width=0, height=0, background_color=(0, 0, 0), setting=None):
        """
        __init__ doesnt have Initialization Guard because the code needs to change 
        the attributes of the instance. By removing the Initialization Guard, the 
        code can change the attributes by trying to create a new instance of the class.
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.background_color = background_color
        self.name = ""
        self.dialog = ""
        self.font_name = pygame.font.SysFont(setting.font, int(5*setting.multiplier))
        self.font_dialog = pygame.font.SysFont(setting.font, int(3.5*setting.multiplier))
        self.setting = setting
        self.name_position = (self.x + int(1*setting.multiplier), self.y + int(1*setting.multiplier))

        DialogBox.instance = self
        print(self)

    def set_name(self, name):
        self.name = name
    def set_dialog(self, dialog):
        self.dialog = dialog

    def draw(self, screen):
        # Create a surface with an alpha channel
        background_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        
        # Fill the surface with the background color and set its alpha value
        background_surface.fill((*self.background_color, 100))  # 128 is the alpha value (0-255)
        screen.blit(background_surface, (self.x, self.y))
        
        # Render the name text
        name_surface = self.font_name.render(self.name, True, (255, 255, 255))
        screen.blit(name_surface, self.name_position)  # padding from the top and left
        
        # Render the dialog text with word wrapping
        dialog_lines = self.wrap_text(self.dialog, self.font_dialog, self.width - int(6*self.setting.multiplier))
        y_offset = self.y + int(8*self.setting.multiplier)  # padding from the top
        for line in dialog_lines:
            dialog_surface = self.font_dialog.render(line, True, (255, 255, 255))
            screen.blit(dialog_surface, (self.x + int(3*self.setting.multiplier), y_offset))
            y_offset += self.font_dialog.get_height() + int(1*self.setting.multiplier)  # Move to the next line


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
    
    def change_font(self):
        self.font_name = pygame.font.SysFont(self.setting.font, int(5*self.setting.multiplier))
        self.font_dialog = pygame.font.SysFont(self.setting.font, int(3.5*self.setting.multiplier))
