from game.character.emotion import Emotion

class Character:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.emotions = []

    def add_emotion(self, emotion_name, emotion_id, image=None):
        emotion = Emotion(emotion_name, emotion_id)
        emotion.set_image(image)
        self.emotions.append(emotion)