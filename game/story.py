from game.setting.util import read_json_file
from game.character import Character

# back 2 directories so that the code can access packages in root directory
# note the ".." twice is the root directory
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

class Story:
    def __init__(self, path):
        self.path = path
        self.data = self.read()

        self.dialogues = []
        self.create_character()
        self.create_dialogue()

    def read(self):
        return read_json_file(self.path)
        
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

    def create_dialogue(self):
        for dialogue in self.data["dialogues"]:

            dialogue_entry = {
                "character_id": dialogue["character_id"],
                "emotion_id": dialogue["emotion_id"],
                "text": dialogue["text"]
            }

            self.dialogues.append(dialogue_entry)