import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_key_pairs()

for keyPair in response['KeyPairs']:
    print(keyPair['KeyName'], keyPair['KeyPairId'])