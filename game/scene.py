from game.ui import DialogBox
from game.story import Story
from game.character import Character

class Scene:

    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(Scene, cls).__new__(cls)
        return cls.instance

    def __init__(self, setting, path=None):
        print(f"Scene : {self}")
        self.index = 0
        self.setting = setting
        self.background = None

        self.story_path = path
        self.story = None
        self.init_story()

        self.dialog_box = None
        self.dialog_box_background = (255, 255, 255)
        self.init_dialog_box()

        Scene.instance = self

    def init_dialog_box(self):
        if self.story is None:
            return
        self.dialog_box_x = int(5*self.setting.multiplier)
        self.dialog_box_y = int(70*self.setting.multiplier)
        self.dialog_box_width = self.setting.get_dimensions()[0]- int(10*self.setting.multiplier)
        self.dialog_box_height = self.setting.get_dimensions()[1]- int(75*self.setting.multiplier)
        self.dialog_box = DialogBox(self.dialog_box_x, self.dialog_box_y, self.dialog_box_width, self.dialog_box_height, self.dialog_box_background, self.setting)

        self.insert_dialog()
    
    def init_story(self):
        if self.story_path is None:
            return
        self.story = Story(self.story_path)

    def set_background(self, background):
        self.background = background

    def next_dialog(self):
        if self.index == len(self.story.dialogs)-1:
            return
        self.index += 1
        self.insert_dialog()

    def prev_dialog(self):
        if self.index <= 0:
            return
        self.index -= 1
        self.insert_dialog()

    def insert_dialog(self):
        current_dialog = self.story.dialogs[self.index]
        for character in Character.instances:
            if character.character_id == current_dialog.get("character_id"):
                self.dialog_box.set_name(character.name)
                break
        self.dialog_box.set_dialog(current_dialog.get("text"))

    def draw(self, screen):
        self.dialog_box.draw(screen)