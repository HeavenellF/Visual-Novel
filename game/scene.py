from game.dialogbox import DialogueBox
from game.setting import StoryReader
from game.character import Character

class Scene:
    def __init__(self, setting, path):
        self.INDEX = 0
        self.setting = setting
        self.background = None

        self.story_path = path
        self.story = None
        self.init_story()

        self.dialogue_box = None
        self.dialogue_box_background = (255, 255, 255)
        self.init_dialogue_box()

    def init_dialogue_box(self):
        self.dialogue_box_x = int(5*self.setting.multiplier)
        self.dialogue_box_y = int(70*self.setting.multiplier)
        self.dialogue_box_width = self.setting.get_dimensions()[0]- int(10*self.setting.multiplier)
        self.dialogue_box_height = self.setting.get_dimensions()[1]- int(75*self.setting.multiplier)
        self.dialogue_box = DialogueBox(self.dialogue_box_x, self.dialogue_box_y, self.dialogue_box_width, self.dialogue_box_height, self.dialogue_box_background, self.setting)

        self.insert_dialogue()
    
    def init_story(self):
        self.story = StoryReader(self.story_path)

    def set_background(self, background):
        self.background = background

    def next_dialogue(self):
        if self.INDEX == len(self.story.dialogues)-1:
            return
        self.INDEX += 1
        self.insert_dialogue()

    def prev_dialogue(self):
        if self.INDEX <= 0:
            return
        self.INDEX -= 1
        self.insert_dialogue()

    def insert_dialogue(self):
        current_dialogue = self.story.dialogues[self.INDEX]
        for character in Character.instances:
            if character.character_id == current_dialogue.get("character_id"):
                self.dialogue_box.set_name(character.name)
                break
        self.dialogue_box.set_dialogue(current_dialogue.get("text"))

    def draw(self, screen):
        self.dialogue_box.draw(screen)

    def change_font_next(self):
        DialogueBox.change_font_next()

    def change_font_prev(self):
        DialogueBox.change_font_prev()