import boto3

internet_gateway_id = 'igw-0aaeefb9d2e310b92'
route_table_id = 'rtb-098980634ccb801bf'

ec2 = boto3.client('ec2')

#no expected output, no needed to store in a variable
ec2.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=internet_gateway_id,
    RouteTableId=route_table_id,
)
