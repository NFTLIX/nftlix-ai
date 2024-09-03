from utils.s3_utils import S3Service
from PIL import Image
from exceptions import ImageException
from schemas import ImageResponse
from core.settings import settings
import numpy as np
from rembg import remove
from utils.json_utils import dump_to_json

class NukkiService:
    def __init__(self):
        self.s3_service = S3Service()
        self.image_dir = settings.NUKKI_DIR

    def convert(self, image: Image.Image, image_name: str, description: str, name: str, token_id: str):
        converted_img = remove(np.array(image))

        upload_result = self.s3_service.upload_image_to_s3(image=Image.fromarray(converted_img), image_dir=self.image_dir, image_name=image_name, format='PNG')

        # s3 업로드 도중 에러 발생 시 ImageException 예외 발생
        if upload_result['status'] == 'error':
            raise ImageException(image_name=image_name, message=upload_result['message'])

        # metadata 업로드
        metadata_upload_result = self.s3_service.upload_metadata_to_s3(
            dump_to_json(description, upload_result['url'], name, token_id, 'nukki'))

        if metadata_upload_result['status'] == 'error':
            raise ImageException(image_name=image_name, message=upload_result['message'])

        return ImageResponse(image_url=upload_result['url'], metadata_url=metadata_upload_result['url'])
