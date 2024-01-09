import boto3

subnet_id = 'subnet-09f9f04656dc1af35'

ec2 = boto3.client('ec2')

ec2.delete_subnet(
    SubnetId=subnet_id,
)