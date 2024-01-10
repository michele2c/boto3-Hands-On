import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_security_groups()

for sg in response['SecurityGroups']:
    print(sg['GroupId'], sg['VpcId'], sg['GroupName'], sg['Description'])
        
    for permission in sg['IpPermissions']:
        # maybe not all sg has a port available
        if 'FromPort' in permission:
            print(permission['FromPort'])
        
        if 'IpProtocol' in permission:
            print(permission['IpProtocol'])
        
        if 'ToPort' in permission:
            print(permission['ToPort'])
            
        if 'IpRanges'in permission:
            for ipRange in permission['IpRanges']:
                print(ipRange['CidrIp'])
        
