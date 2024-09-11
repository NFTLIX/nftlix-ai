import cv2
from utils.s3_utils import S3Service
from PIL import Image
from exceptions import ImageException
from schemas import ImageResponse
from core.settings import settings
import numpy as np
from utils.json_utils import dump_to_json

class CartoonizationService:
    def __init__(self):
        self.s3_service = S3Service()
        self.image_dir = settings.CARTOONIZATION_DIR
        self.original_dir = settings.ORIGINAL_DIR

    def convert(self, image: Image.Image, image_name: str, description: str, name: str, token_id: str):
        # 1. 원본 이미지 저장
        upload_result = self.s3_service.upload_image_to_s3(image=image, image_dir=self.original_dir, image_name=image_name)

        # s3 업로드 도중 에러 발생 시 ImageException 예외 발생
        if upload_result['status'] == 'error':
            raise ImageException(image_name=image_name, message=upload_result['message'])

        # 2. 변환된 이미지 저장
        # sigma_r 값이 줄어들 수록 윤곽이 더 뚜렷해지는 효과
        converted_img = cv2.stylization(np.array(image), sigma_s=100, sigma_r=0.5)
        upload_result = self.s3_service.upload_image_to_s3(image=Image.fromarray(converted_img), image_dir=self.image_dir, image_name=image_name)

        # s3 업로드 도중 에러 발생 시 ImageException 예외 발생
        if upload_result['status'] == 'error':
            raise ImageException(image_name=image_name, message=upload_result['message'])

        # metadata 업로드
        metadata_upload_result = self.s3_service.upload_metadata_to_s3(dump_to_json(description, upload_result['url'], name, token_id, 'cartoonization'))

        if metadata_upload_result['status'] == 'error':
            raise ImageException(image_name=image_name, message=upload_result['message'])

        return ImageResponse(image_url=upload_result['url'], metadata_url=metadata_upload_result['url'])
