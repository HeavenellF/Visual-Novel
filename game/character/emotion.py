import os

class Emotion:
    """
    A class to represent an emotion of a character.
    Emotion contains an image that represents the emotion.
    """
    EMOTIONS = {
        0: "neutral",
        1: "happy",
        2: "sad",
        3: "angry",
        4: "surprised",
        5: "disgusted",
        6: "scared"
    }

    def __init__(self, name=None, emotion_id=None):
        if name is None and emotion_id is None:
            print("Emotion needs a name or emotion ID")
            return
        if emotion_id is not None and emotion_id not in self.EMOTIONS:
            print(f"Emotion ID {emotion_id} does not exist")
            return
        if name is not None and name not in self.EMOTIONS.values():
            print(f"Emotion name '{name}' does not exist")
            return

        self.name = name
        self.emotion_id = emotion_id
        self.image = None

    def set_image(self, image):
        # Check if image exists
        if not os.path.exists(image):
            print(f"Image {image} does not exist for emotion {self.name}")
            return
        self.image = image
