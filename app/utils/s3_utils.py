import boto3
from botocore.exceptions import NoCredentialsError, ClientError
from app.core.settings import settings
from PIL import Image
from io import BytesIO
import uuid

class S3Service:
    def __init__(self):
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY,
            aws_secret_access_key=settings.AWS_SECRET_KEY
        )

    def upload_image_to_s3(self, image: Image.Image, bucket: str = settings.AWS_S3_BUCKET, object_name=None, format='JPEG'):
        try:
            # 메모리에 이미지를 저장한 후, 이를 s3에 업로드
            buffer = BytesIO()
            image.save(buffer, format=format)
            buffer.seek(0)

            if object_name is None:
                object_name = str(uuid.uuid1()) + format.lower()

            # s3에 업로드
            self.s3_client.upload_fileobj(buffer, bucket, object_name)

            return {"status": "success", "object_name": object_name}
        except NoCredentialsError:
            return {"status": "error", "message": "Credentials not available"}
        except Exception as e:
            return {"status": "error", "message": str(e)}
