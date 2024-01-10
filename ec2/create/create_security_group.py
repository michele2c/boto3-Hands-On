import boto3

sg_description='Security group from boto3'
sg_group_name='boto3-security-group'
vpc_id='vpc-0fb73703b42911725'

ec2 = boto3.client('ec2')

response = ec2.create_security_group(
    Description=sg_description,
    GroupName=sg_group_name,
    VpcId=vpc_id,
)

print(response['GroupId'])