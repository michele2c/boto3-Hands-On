import boto3

ec2 = boto3.client('ec2')

route_table_id = 'rtb-098980634ccb801bf'
subnet_id = 'subnet-09f9f04656dc1af35'

association = ec2.associate_route_table(
    RouteTableId=route_table_id,
    SubnetId=subnet_id,
)

print(association['AssociationId'])
