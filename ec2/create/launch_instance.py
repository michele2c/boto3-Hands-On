import boto3

def launch_instance(client, ami_id, security_group_id, key_pair_name, user_data=None):
    response = client.run_instances(
        ImageId=ami_id,
        InstanceType='t2.micro',
        KeyName=key_pair_name,
        MaxCount=1,
        MinCount=1,
        SecurityGroupIds=[
            security_group_id
        ],
        UserData=user_data
    )
# print out instance id
    print(response['Instances'][0]['InstanceId'])


ami_id = 'ami-0c7217cdde317cfec'
key_pair_name = 'key from boto3'
security_group_id = 'sg-0baca89e8923bb1f5'

user_data='''#!/bin/bash
    apt update -y
    apt-get install -y apache2
    systemctl start apache2
    systemctl enable apache2'''

ec2 = boto3.client('ec2')

# call function
launch_instance(ec2, ami_id, security_group_id, key_pair_name, user_data)


# ssh -i key-from-boto3.pem ubuntu@<public_ip_address>




# def create_instance(client, ami_id, security_group_id, key_pair_name, user_data=None):
#     response = client.run_instances(
#         ImageId=ami_id,
#         InstanceType='t2.micro',
#         KeyName=key_pair_name,
#         MaxCount=1,
#         MinCount=1,
#         SecurityGroupIds=[
#             security_group_id
#         ],
#         UserData=user_data
#     )
    
#     print(response["Instances"][0]["InstanceId"])

# ami_id = "ami-09e67e426f25ce0d7"
# key_pair_name = "Key from boto3"
# security_group_id = "sg-0fa4109d022d08ebe"

# user_data='''#!/bin/bash
#     apt update -y
#     apt-get install -y apache2
#     systemctl start apache2
#     systemctl enable apache2'''

# ec2 = boto3.client('ec2')
# create_instance(ec2, ami_id, security_group_id, key_pair_name, user_data)
