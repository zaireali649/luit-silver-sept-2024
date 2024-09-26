import json
import boto3


def lambda_handler(event, context):
    ec2_client = boto3.client('ec2')
    
    response = ec2_client.describe_instances()
    
    reservations = response["Reservations"]
    
    instanceIds = []
    
    for reservation in reservations:
        instances = reservation["Instances"]
        for instance in instances:
            instanceId = instance["InstanceId"]
            
            instanceIds.append(instanceId)
    
    
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps(instanceIds, indent=4)
    }
