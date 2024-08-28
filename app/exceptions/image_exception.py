class ImageException(Exception):
    def __init__(self, image_name: str, message: str):
        self.image_name = image_name
        self.message = message
        super().__init__(self.message)
