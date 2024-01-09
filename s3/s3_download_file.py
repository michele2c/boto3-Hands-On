"""
Your module description
"""

import boto3
import os
from s3_list_objects import list_objects_keys

# download single obejct
def download_single_object(client, bucket, key, filename):
    client.download_file(bucket, key, filename)

if __name__ == '__main__':
    
    bucket = 'costa-boto3-01032024'
    key = 'test_text.txt'
    filename = 'test_text.txt'
    
    s3 = boto3.client('s3')
    
    
    # download all objects
    
    keys = list_objects_keys(s3, bucket)
    
    for key in keys:
        # create the folder
        if '/' == key[-1]:
            try:
                os.mkdir(key)
            except:
                pass
        # downloading all objects
        else:
            download_single_object(s3, bucket, key, key)