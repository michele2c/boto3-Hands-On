import boto3

internet_gateway_id = 'igw-0aaeefb9d2e310b92'

ec2 = boto3.client('ec2')

# no Expected Output
ec2.delete_internet_gateway(
    InternetGatewayId=internet_gateway_id,
)