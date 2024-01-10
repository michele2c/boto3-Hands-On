import boto3

ami_id = 'ami-0debde08544b9bc55'

ec2 = boto3.client('ec2')

response = ec2.deregister_image(
    ImageId=ami_id
)