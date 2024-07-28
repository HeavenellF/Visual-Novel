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
            raise ValueError("Emotion needs a name or emotion ID")
        
        if emotion_id is not None:
            if not isinstance(emotion_id, int):
                raise TypeError("Emotion ID must be an integer")
            if emotion_id not in self.EMOTIONS:
                raise ValueError(f"Emotion ID {emotion_id} does not exist")

        if name is not None:
            if not isinstance(name, str):
                raise TypeError("Emotion name must be a string")
            if name not in self.EMOTIONS.values():
                raise ValueError(f"Emotion name '{name}' does not exist")
        
        # Ensure consistency between name and emotion_id
        if name is not None and emotion_id is not None:
            if self.EMOTIONS[emotion_id] != name:
                raise ValueError(f"Emotion ID {emotion_id} and name '{name}' do not match")
        
        # If only one is provided, derive the other
        if name is None:
            name = self.EMOTIONS[emotion_id]
        if emotion_id is None:
            emotion_id = next(key for key, value in self.EMOTIONS.items() if value == name)


        self.name = name
        self.emotion_id = emotion_id
        self.image = None

    def set_image(self, image):
        # Check if image exists
        if not os.path.exists(image):
            raise FileNotFoundError(f"Image {image} does not exist")
        
        self.image = image
