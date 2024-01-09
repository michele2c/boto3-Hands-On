import boto3

vpc_id = 'vpc-0550957d303b2fc63'

ec2 = boto3.client('ec2')

ec2.delete_vpc(
    VpcId=vpc_id,
)