import boto3

route_table_id = 'rtb-098980634ccb801bf'

ec2 = boto3.client('ec2')

# get route table association id
response = ec2.describe_route_tables(
    RouteTableIds=[
        route_table_id,
    ],
)
# index 0 because it's only one route table
for association in response['RouteTables'][0]['Associations']:
    # if main is not True (main route twble is created by default)
    if not association['Main']:
        # get association id
        association_id = association['RouteTableAssociationId']
        print(association_id)

        ec2.disassociate_route_table(
            AssociationId=association_id,
        )