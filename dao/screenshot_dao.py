import boto3
from botocore.exceptions import NoCredentialsError
import logging


class ScreenshotDao:

    def __init__(self, bucket_name, access_key, secret_key):
        self.bucket_name = bucket_name
        self.s3 = boto3.client('s3', aws_access_key_id=access_key, aws_secret_key_id=secret_key)

    def upload(self, image_file, key):
        try:
            self.s3.upload_file(image_file, self.bucket_name, key)
            logging.debug(f"Upload of image file {image_file} successful.")
        except FileNotFoundError:
            logging.debug(f"Could not find file {image_file}.")
        except NoCredentialsError:
            logging.debug(f"Could not find credentials.")