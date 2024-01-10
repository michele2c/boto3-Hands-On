import boto3

key_pair_name = 'key from boto3'

ec2 = boto3.client('ec2')

response = ec2.delete_key_pair(
    KeyName=key_pair_name,
)

print(response)