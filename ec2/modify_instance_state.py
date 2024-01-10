import boto3

def stop_instance(client, instance_id):
    response = client.stop_instances(
        InstanceIds=[
            instance_id
        ],
    )
    
    print(instance_id, 'stopped')

def start_instance(client, instance_id):
    response = client.start_instances(
        InstanceIds=[
            instance_id
        ],
    )
    
    print(instance_id, 'started')

def terminate_instance(client, instance_id):
    response = client.terminate_instances(
        InstanceIds=[
            instance_id
        ],
    )
    
    print(instance_id, 'terminated')


if __name__ == '__main__':
    
    instance_id = 'i-052237f462e4e01e5'
    ec2 = boto3.client('ec2')
    
    terminate_instance(ec2, instance_id)
    