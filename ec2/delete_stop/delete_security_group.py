import boto3

security_group_id = 'sg-0baca89e8923bb1f5'

ec2 = boto3.client('ec2')

response = ec2.delete_security_group(
    GroupId=security_group_id
)

print(response)