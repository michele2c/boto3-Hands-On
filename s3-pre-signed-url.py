"""
Generate a pre-signed URLs
grant temporary access to objects
"""

import boto3

s3 = boto3.client('s3')

response = s3.generate_presigned_url('get_object', Params={'Bucket': 'costa-boto3-01032024', 'Key': 'test_text_upload.txt'}, ExpiresIn=300)

print(response)