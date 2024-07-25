
class Emotion:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.image = None
        
    def set_image(self, image):
        self.image = image