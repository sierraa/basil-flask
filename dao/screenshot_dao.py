import boto3
from botocore.exceptions import NoCredentialsError
import logging
import urllib.parse


class ScreenshotDao:

    def __init__(self, bucket_name, access_key, secret_key, region="us-west-2"):
        self.bucket_name = bucket_name
        self.s3 = boto3.client('s3')
        self.base_url = f"https://{bucket_name}.s3-{region}.amazonaws.com/"

    def upload(self, image_file, title):
        try:
            key = f"{title}.png"
            self.s3.upload_fileobj(image_file, self.bucket_name, key)
            logging.debug(f"Upload of image file {image_file} successful.")
            return self.get_url(title)
        except FileNotFoundError:
            logging.debug(f"Could not find file {image_file}.")
        except NoCredentialsError:
            logging.debug(f"Could not find credentials.")

    def get_url(self, key):
        url_encoded_key = urllib.parse.quote(key)
        return self.base_url + url_encoded_key