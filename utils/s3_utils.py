import boto3
from botocore.exceptions import NoCredentialsError
from core.settings import settings
from PIL import Image
from io import BytesIO
import uuid

class S3Service:
    def __init__(self):
        self.s3_client = boto3.client(
            's3',\
            aws_access_key_id=settings.AWS_ACCESS_KEY,
            aws_secret_access_key=settings.AWS_SECRET_KEY
        )
        self.bucket_name = settings.AWS_S3_IMAGE_BUCKET

    def upload_image_to_s3(self, image: Image.Image, image_dir: str, image_name: str, bucket: str = settings.AWS_S3_IMAGE_BUCKET, format='PNG'):
        try:
            # 메모리에 이미지를 저장한 후, 이를 s3에 업로드
            buffer = BytesIO()
            image.save(buffer, format=format)
            buffer.seek(0)

            object_name = image_name + '_' + str(uuid.uuid1()) + '.' + format.lower()

            # s3에 업로드
            image_path = f"{image_dir}/{object_name}"
            self.s3_client.upload_fileobj(buffer, bucket, image_path)

            return {"status": "success", "url": f"https://{self.bucket_name}.s3.amazonaws.com/{image_path}"}
        except NoCredentialsError:
            return {"status": "error", "message": "Credentials not available"}
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def upload_metadata_to_s3(self, json_buffer, bucket: str = settings.AWS_S3_METADATA_BUCKET):
        try:
            # TODO: metadata 이름을 특정 이름으로 수정해야할 필요 있을 시 수정
            metadata_name = str(uuid.uuid1()) + '.' + 'json'
            self.s3_client.upload_fileobj(json_buffer, bucket, metadata_name)

            return {"status": "success", "url": f"https://{bucket}.s3.amazonaws.com/{metadata_name}"}
        except NoCredentialsError:
            return {"status": "error", "message": "Credentials not available"}
        except Exception as e:
            return {"status": "error", "message": str(e)}