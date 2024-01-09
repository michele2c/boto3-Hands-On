import boto3

route_table_id = 'rtb-098980634ccb801bf'

ec2 = boto3.client('ec2')

# no expected output 
ec2.delete_route(
    DestinationCidrBlock='0.0.0.0/0',
    RouteTableId=route_table_id,
)