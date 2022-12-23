import boto3
import os
import tempfile

from PIL import Image

def handler(event, context):
    s3 = boto3.client('s3')
bucket = event['Records'][0]['s3']['bucket']['name']
bucket = 'my-upload-bucket'
key = event['Records'][0]['s3']['object']['key']
with tempfile.TemporaryDirectory() as tmpdir:
    file_path = os.path.join(tmpdir, key)
    s3.download_file(bucket, key, file_path)
    with Image.open(file_path) as image:
        image = image.resize((128, 128))
        target_bucket = 'my-resized-bucket'