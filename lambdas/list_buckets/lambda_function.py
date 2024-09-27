"""Lambda for getting S3 buckets."""
import json
import boto3
from typing import Any, Dict


def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """AWS Lambda function that lists all S3 bucket names.

    Args:
        event (Dict[str, Any]): The event data passed to the Lambda function.
        context (Any): The runtime information of the Lambda function.

    Returns:
        Dict[str, Any]: A dictionary containing the HTTP status code and the list of bucket names as a string.
    """
    # Create an S3 client
    s3 = boto3.client('s3')

    # Log a message from Lambda
    print('Hello from Lambda!')

    # List all S3 buckets
    response = s3.list_buckets()

    # Extract the list of buckets from the response
    bucket_names = []
    buckets = response["Buckets"]

    # Iterate through each bucket to extract the name
    for bucket in buckets:
        print(bucket["Name"])  # Print each bucket name
        bucket_names.append(bucket["Name"])  # Add the bucket name to the list

    # Return the response with status code and bucket names joined as a string
    return {
        'statusCode': 200,
        'body': '\n'.join(bucket_names)
    }
