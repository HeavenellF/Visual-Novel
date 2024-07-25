import os

class Emotion:
    """
    A class to represent an emotion of a character.
    Emotion contains an image that represents the emotion.
    """
    def __init__(self, name, emotion_id):
        self.name = name
        self.emotion_id = emotion_id
        self.image = None

    def set_image(self, image):
        # Check if image exists
        if not os.path.exists(image):
            print(f"Image {image} does not exist for emotion {self.name}")
            return
        self.image = image
