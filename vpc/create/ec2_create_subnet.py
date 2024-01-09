import boto3

cidr_block = '12.0.2.0/24'
vpc_id = 'vpc-0550957d303b2fc63'

ec2 = boto3.client('ec2')

subnet = ec2.create_subnet(CidrBlock=cidr_block, VpcId=vpc_id)

print(subnet['Subnet']['SubnetId'])