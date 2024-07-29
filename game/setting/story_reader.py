import json
import sys
import os
from game.character import Character

# back 2 directories so that the code can access packages in root directory
# note the ".." twice is the root directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

class StoryReader:
    def __init__(self, path):
        self.path = path
        self.data = self.read()

        self.create_character()

    def read(self):
        with open(self.path, 'r', encoding="utf-8") as file:
            return json.load(file)
        
    def create_character(self):
        for character in self.data["characters"]:
            name = character["name"]
            character_id = character["character_id"]

            char = Character(character_id, name)

            for emotion in character["emotions"]:
                emotion_id = emotion["emotion_id"]
                emotion_name = emotion["name"]
                emotion_image = emotion["image"]
                char.add_emotion(emotion_name, emotion_id,  emotion_image)

