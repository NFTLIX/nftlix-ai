import cv2
from app.utils.s3_utils import S3Service
from PIL import Image
from app.exceptions import ImageException
from app.schemas import ImageResponse
from app.core.settings import settings

class CartoonizationService:
    def __init__(self):
        self.s3_service = S3Service()
        self.image_dir = settings.CARTOONIZATION_DIR

    def convert(self, image: Image.Image, image_name: str):
        # sigma_r 값이 줄어들 수록 윤곽이 더 뚜렷해지는 효과
        converted_img = cv2.stylization(image, sigma_s=100, sigma_r=0.5)
        upload_result = self.s3_service.upload_image_to_s3(image=converted_img, image_dir=self.image_dir, image_name=image_name)

        # s3 업로드 도중 에러 발생 시 ImageException 예외 발생
        # TODO: exception handler 구현 필요
        if upload_result['status'] == 'error':
            raise ImageException(image_name=image_name, message=upload_result['message'])

        return ImageResponse(upload_result['url'])
