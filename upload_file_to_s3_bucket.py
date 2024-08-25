import boto3
import os
from botocore.exceptions import NoCredentialsError
import argparse

def upload_to_s3(file_name, bucket_name, s3_client: boto3.client, object_name):
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    try:
        s3_client.upload_file(file_name, bucket_name, object_name)
        print(f"{file_name} uploaded successfully to {bucket_name}/{object_name}")
    except NoCredentialsError as e:
        print("Credentials not provided. Set the ACCESS_KEY and SECRET_KEY environment variables.")
        print(e)

if __name__ == "__main__":
    client = boto3.client(
        's3',
        aws_access_key_id=os.getenv("ACCESS_KEY"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    )

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', default=None, help="Path of the file to upload to s3 bucket")
    parser.add_argument('-n', '--bucket-name', default=None, help="Name of the bucket to upload the file into")
    parser.add_argument('-o', '--object-name', default=None, help="Name of the uploaded object on the s3 bucket. Default: filename")

    args = parser.parse_args()

    upload_to_s3(args.filename, args.bucket_name, client, args.object_name)
