import boto3

ec2 = boto3.client('ec2')

response = ec2.create_image(
    Description='Test-Creation',
    InstanceId='i-0c27e303cf939a58c',
    Name='Go to AMI',
)

print(response)