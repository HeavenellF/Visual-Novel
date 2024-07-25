from game.character.emotion import Emotion

class Character:
    """
    A class to represent a character in the game.
    """
    def __init__(self, character_id, name):
        self.character_id = character_id
        self.name = name
        self.emotions = []

    def add_emotion(self, emotion_name, emotion_id, image=None):
        # Check if emotion already exists
        for emotion in self.emotions:
            if emotion.emotion_id == emotion_id or emotion.name == emotion_name:
                print(f"Emotion with id {emotion_id} or name {emotion_name} already exists for character {self.name}")
                return

        # Create a new emotion
        emotion = Emotion(emotion_name, emotion_id)
        emotion.set_image(image)
        self.emotions.append(emotion)
