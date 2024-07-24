import pygame
from game.dialogbox import DialogueBox

class Scene:
    def __init__(self, setting):
        self.setting = setting
        self.dialogue_box = None
        self.background = None
        self.init_dialogueBox()

    def init_dialogueBox(self):
        self.dialogue_box = DialogueBox(50, 700, self.setting.get_dimensions()[0]-100, self.setting.get_dimensions()[1]-750, (100, 100, 100))
        self.dialogue_box.set_name("Character Name")
        self.dialogue_box.set_dialogue("This is a sample dialogue for testing the DialogueBox.")

    def draw(self, screen):
        self.dialogue_box.draw(screen)