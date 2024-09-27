"""Lambda to get all instance IDs."""
import json
import boto3
from typing import Any, Dict


def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """AWS Lambda function that retrieves and returns the instance IDs of all EC2 instances.

    Args:
        event (Dict[str, Any]): The event data passed to the Lambda function.
        context (Any): The runtime information of the Lambda function.

    Returns:
        Dict[str, Any]: A dictionary containing the HTTP status code and the list of instance IDs in JSON format.
    """
    # Create an EC2 client
    ec2_client = boto3.client('ec2')

    # Describe EC2 instances
    response = ec2_client.describe_instances()

    # Extract reservations from the response
    reservations = response["Reservations"]

    # Initialize an empty list to store instance IDs
    instance_ids = []

    # Iterate through each reservation
    for reservation in reservations:
        instances = reservation["Instances"]
        # Iterate through each instance in the reservation
        for instance in instances:
            # Get the instance ID
            instance_id = instance["InstanceId"]
            # Append the instance ID to the list
            instance_ids.append(instance_id)

    # Return the response with status code and the list of instance IDs in JSON format
    return {
        'statusCode': 200,
        'body': json.dumps(instance_ids, indent=4)
    }
