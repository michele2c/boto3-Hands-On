import boto3

internet_gateway_id = 'igw-0aaeefb9d2e310b92'
vpc_id = 'vpc-0550957d303b2fc63'

ec2 = boto3.client('ec2')

attachement = ec2.attach_internet_gateway(
    InternetGatewayId=internet_gateway_id,
    VpcId=vpc_id,
)

print(attachement)