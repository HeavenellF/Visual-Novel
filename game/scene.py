from game.dialogbox import DialogueBox

class Scene:
    def __init__(self, setting):
        self.setting = setting
        self.background = None

        self.dialogue_box = None
        self.dialogue_box_background = (255, 255, 255)
        self.dialogue_box_x = int(5*self.setting.multiplier)
        self.dialogue_box_y = int(70*self.setting.multiplier)
        self.dialogue_box_width = self.setting.get_dimensions()[0]- int(10*self.setting.multiplier)
        self.dialogue_box_height = self.setting.get_dimensions()[1]- int(75*self.setting.multiplier)
        self.init_dialogue_box()

    def init_dialogue_box(self):
        self.dialogue_box = DialogueBox(self.dialogue_box_x, self.dialogue_box_y, self.dialogue_box_width, self.dialogue_box_height, self.dialogue_box_background, self.setting)

        # for testing purposes
        # self.dialogue_box.set_name("Character Name")
        # self.dialogue_box.set_dialogue("This is a sample dialogue for testing the DialogueBox. A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A A ")
    
    def set_background(self, background):
        self.background = background

    def next_dialogue(self):
        pass

    def prev_dialogue(self):
        pass

    def draw(self, screen):
        self.dialogue_box.draw(screen)