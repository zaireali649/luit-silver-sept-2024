"""Listing resources from AWS using Python."""

from helpers import *  # Assuming helpers contain functions to get AWS clients and list resources


def print_bucket_names(s3_client) -> None:
    """Prints the names of all S3 buckets available to the provided S3 client.

    Args:
        s3_client: The S3 client object used to interact with AWS S3.
    """
    bucket_names = list_buckets(s3_client)  # Fetch the list of bucket names using a helper function

    # Iterate through each bucket name and print it
    # Note: Could also use print('\n'.join(bucket_names)) to print all at once
    for bucket_name in bucket_names:
        print(bucket_name)


def print_instance_ids(ec2_client) -> None:
    """Prints the IDs of all EC2 instances available to the provided EC2 client.

    Args:
        ec2_client: The EC2 client object used to interact with AWS EC2.
    """
    instances = describe_instances(ec2_client)  # Fetch the list of instances using a helper function
    instance_ids = []

    # Collect instance IDs from the response
    for instance in instances:
        instance_ids.append(instance['InstanceId'])

    # Print each instance ID
    for instance_id in instance_ids:
        print(instance_id)


# Initialize AWS clients for EC2 and S3
ec2_client = get_ec2_client()
s3_client = get_s3_client()

# Print the names of S3 buckets and EC2 instance IDs
print_bucket_names(s3_client)
print_instance_ids(ec2_client)
