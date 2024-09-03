from pydantic import BaseModel, HttpUrl

class ImageResponse(BaseModel):
    image_url: HttpUrl
    metadata_url: HttpUrl

    class Config:
        schema_extra = {
            "example": {
                "image_url": "https://example.com/images/uploaded_image.jpg",
                "metadata_url": "https://example.com/images/metadata.jpg",
            }
        }
