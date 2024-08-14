from game.setting.util import read_json_file
from game.character import Character

# back 2 directories so that the code can access packages in root directory
# note the ".." twice is the root directory
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

class Story:

    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(Story, cls).__new__(cls)
        return cls.instance


    def __init__(self, path):
        print(f"Story : {self}")
        self.path = path
        self.data = self.read()

        self.dialogs = []
        self.create_character()
        self.create_dialog()

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

    def create_dialog(self):
        for dialog in self.data["dialogs"]:

            dialog_entry = {
                "character_id": dialog["character_id"],
                "emotion_id": dialog["emotion_id"],
                "text": dialog["text"]
            }

            self.dialogs.append(dialog_entry)