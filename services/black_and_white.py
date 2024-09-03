import cv2
from utils.s3_utils import S3Service
from PIL import Image
from exceptions import ImageException
from schemas import ImageResponse
from core.settings import settings
import numpy as np

class BlackAndWhiteService:
    def __init__(self):
        self.s3_service = S3Service()
        self.image_dir = settings.BLACK_AND_WHITE_DIR

    def convert(self, image: Image.Image, image_name: str):
        image = np.array(image)
        converted_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        upload_result = self.s3_service.upload_image_to_s3(image=Image.fromarray(converted_image), image_dir=self.image_dir, image_name=image_name)

        # s3 업로드 도중 에러 발생 시 ImageException 예외 발생
        # TODO: exception handler 구현 필요
        if upload_result['status'] == 'error':
            raise ImageException(image_name=image_name, message=upload_result['message'])

        return ImageResponse(image_url=upload_result['url'])
