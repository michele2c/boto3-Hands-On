import boto3

s3 = boto3.client('s3')

with open("test_text.txt", 'rb') as f: #loading to the memory
    s3.put_object(
        Bucket="costa-boto3-01032024", Key="test_text.txt", Body=f, 
        ContentType="text/plain")