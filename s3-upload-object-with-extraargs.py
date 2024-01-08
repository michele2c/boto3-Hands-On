"""
Upload object using upload_file and ExtraArgs
"""

import boto3

s3 = boto3.client('s3')

#parameters s3.upload_file(Filename, Bucket, Key, ExtraArgs=None, Callback=None, Config=None)
s3.upload_file('test_text.txt', 'costa-boto3-01032024', 'test_text_upload.txt', ExtraArgs={'ContentType':'text/plain'})