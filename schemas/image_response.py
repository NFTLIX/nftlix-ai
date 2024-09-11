from pydantic import BaseModel, HttpUrl

class ImageResponse(BaseModel):
    original_image_url: HttpUrl
    converted_image_url: HttpUrl
    metadata_url: HttpUrl

    class Config:
        schema_extra = {
            "example": {
                "original_image_url": "https://example.com/images/original_image.jpg",
                "converted_image_url": "https://example.com/images/converted_image.jpg",
                "metadata_url": "https://example.com/images/metadata.jpg",
            }
        }
