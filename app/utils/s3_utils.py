import boto3
from botocore.exceptions import NoCredentialsError, ClientError
from app.core.settings import settings

class S3Service:
    def __init__(self):
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY,
            aws_secret_access_key=settings.AWS_SECRET_KEY
        )

    def upload_file(self, file_name: str, bucket: str = settings.AWS_S3_BUCKET, object_name=None):
        try:
            if object_name is None:
                object_name = file_name
            self.s3_client.upload_file(file_name, bucket, object_name)
            return {"status": "success", "object_name": object_name}
        except NoCredentialsError:
            return {"status": "error", "message": "Credentials not available"}
        except ClientError as e:
            return {"status": "error", "message": str(e)}
