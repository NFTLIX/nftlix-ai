from pydantic import BaseModel, HttpUrl

class ImageResponse(BaseModel):
    def __init__(self, image_url: HttpUrl):
        self.image_url = image_url

    class Config:
        schema_extra = {
            "example": {
                "image_url": "https://example.com/images/uploaded_image.jpg"
            }
        }
