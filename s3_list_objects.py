import boto3

#save obejct list variable response
#  s3 = boto3.client('s3')
# response = s3.list_objects_v2(Bucket='costa-boto3-01032024',
# Prefix='folder/folder_a/')

# #iterate over the Contents and print out
# for content in response['Contents']:
#     print(content['Key'])
    

"""
Prefix = look for particular path/folder
"""
# s3 = boto3.client('s3')
# response = s3.list_objects_v2(Bucket='costa-boto3-01032024',
# Prefix='folder/folder_a/')

# for content in response['Contents']:
#     print(content['Key'])
    

"""
Look for a particular file extension
"""
# s3 = boto3.client('s3')
# response = s3.list_objects_v2(Bucket='costa-boto3-01032024')

# extension = '.txt'

# for content in response['Contents']:
#     if(extension in content['Key'][-(len(extension)):]):
#         print(content['Key'])

"""
CREATE FUNCTION - filter objects extension
"""
def filter_objects_extension(client, bucket, extension):
    keys = []
    
    response = client.list_objects_v2(Bucket=bucket)
    
    for content in response['Contents']:
        if(extension in content['Key'][-(len(extension)):]):
            keys.append(content['Key'])
    
    return keys

"""
CREATE FUNCTION - list objects keys
"""

def list_objects_keys(client, bucket, prefix=''):
    keys = []
    
    response = client.list_objects_v2(Bucket=bucket, Prefix=prefix)
    
    for content in response['Contents']:
        keys.append(content['Key'])
    
    return keys
    

if __name__ == '__main__': # dont run this if was imported to other code
# call the function 
    s3 = boto3.client('s3')
    
    response = filter_objects_extension(s3, 'costa-boto3-01032024', '.txt')
    print(response)
    
    response = list_objects_keys(s3, 'costa-boto3-01032024', 'folder/')
    print(response)