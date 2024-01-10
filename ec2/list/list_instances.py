import boto3 

ec2 = boto3.client('ec2')


response = ec2.describe_instances()

for reservation in response['Reservations']:
    # iterate over values stored in response and store values of 'Reservations' key
    # in reservation
    for instance in reservation['Instances']:
         # iterate over values stored in reservation and store values of 'Instances' key
         # in instance
        print(instance['InstanceId'], instance['InstanceType'], instance['ImageId'],
                instance['VpcId'], instance['SubnetId'], instance['State']['Name'])
        
        #check if the key "Tags" exist in instance
        if 'Tags' in instance:
            # then find the name of the instance
            for tag in instance['Tags']:
                if tag['Key'] == 'Name':
                    print(tag['Value'])
        
        # get security group
        for sg in instance['SecurityGroups']:
            print(sg['GroupId'], sg['GroupName'])
        
        # get information may not available in all instaces
        if 'PublicIpAddress' in instance:
            print(instance['PublicIpAddress'])
        
        if 'KeyName' in instance: # key pair name
            print(instance['KeyName'])
        
        if 'IamInstanceProfile' in instance:
            print(instance['IamInstanceProfile']['Arn'], instance['IamInstanceProfile']['Id'])

# print(response)
