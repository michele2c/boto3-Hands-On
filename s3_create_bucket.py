"""
Your module description
"""

import boto3

s3 = boto3.client('s3')

response = s3.create_bucket(
    Bucket='costa-boto3-01032024'
)

print(response)