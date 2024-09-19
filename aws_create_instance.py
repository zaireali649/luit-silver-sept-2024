"""Create instances in AWS using Python."""

from helpers import *  # Assuming helpers module contains necessary instance creation functions


def create_instances(ec2_client: any, ami_type: str = 'Ubuntu', instance_amount: int = 1) -> None:
    """Creates EC2 instances based on the specified AMI type and number of instances.

    Args:
        ec2_client: The EC2 client object used to interact with AWS EC2 services.
        ami_type (str): The type of AMI to use for the instances. Defaults to 'Ubuntu'.
        instance_amount (int): The number of instances to create. Defaults to 1.

    Returns:
        None: This function doesn't return any values.
    """
    for i in range(instance_amount):
        if ami_type.lower() == 'ubuntu':
            # Creating an Ubuntu EC2 instance
            print("Creating instance with ami type:", ami_type)
            create_ubuntu_instance(ec2_client)
        elif ami_type.lower() == 'linux 2023':
            # Creating an Amazon Linux 2023 EC2 instance
            print("Creating instance with ami type:", ami_type)
            create_amazon_linux_2023_instance(ec2_client)
        elif ami_type.lower() == 'linux 2':
            # Creating an Amazon Linux 2 EC2 instance
            print("Creating instance with ami type:", ami_type)
            create_amazon_linux_2_instance(ec2_client)
        else:
            # If no matching AMI type is found
            print("No AMI Type Found")


# Example usage
ec2_client = get_ec2_client()  # Assume this fetches the appropriate EC2 client
create_instances(ec2_client)
