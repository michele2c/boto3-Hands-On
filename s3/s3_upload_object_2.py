import boto3

s3 = boto3.client('s3')


s3.put_object(Bucket='costa-boto3-01032024', 
                Key='folder/folder_a/new_text.txt', 
                Body='hey, this is a string', 
                ContentType='text/plain')
