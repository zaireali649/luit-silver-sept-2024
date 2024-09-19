"""Placeholder helpers.py."""

def create_ubuntu_instance(ec2_client: any, instance_type: str = 't3.micro') -> dict:
    """Creates an EC2 instance configuration for an Ubuntu instance.

    Args:
        ec2_client: The EC2 client object used to interact with AWS EC2 services.
        instance_type (str): The instance type for the EC2 instance. Defaults to 't3.micro'.

    Returns:
        dict: A dictionary containing the AMI ID and instance type.
    """
    instance = {}
    ami = 'ami-0e86e20dae9224db8'  # Hardcoded AMI ID for Ubuntu
    instance['ami'] = ami
    instance['instance_type'] = instance_type
    return instance


def create_amazon_linux_2023_instance(ec2_client: any, instance_type: str = 't2.large') -> dict:
    """Creates an EC2 instance configuration for an Amazon Linux 2023 instance.

    Args:
        ec2_client: The EC2 client object used to interact with AWS EC2 services.
        instance_type (str): The instance type for the EC2 instance. Defaults to 't2.large'.

    Returns:
        dict: A dictionary containing the AMI ID and instance type.
    """
    instance = {}
    ami = 'ami-0ebfd941bbafe70c6'  # Hardcoded AMI ID for Amazon Linux 2023
    instance['ami'] = ami
    instance['instance_type'] = instance_type
    return instance


def create_amazon_linux_2_instance(ec2_client: any, instance_type: str = 't2.nano') -> dict:
    """Creates an EC2 instance configuration for an Amazon Linux 2 instance.

    Args:
        ec2_client: The EC2 client object used to interact with AWS EC2 services.
        instance_type (str): The instance type for the EC2 instance. Defaults to 't2.nano'.

    Returns:
        dict: A dictionary containing the AMI ID and instance type.
    """
    instance = {}
    ami = 'ami-0a5c3558529277641'  # Hardcoded AMI ID for Amazon Linux 2
    instance['ami'] = ami
    instance['instance_type'] = instance_type
    return instance


def get_ec2_client() -> None:
    """Placeholder function to get the EC2 client object.

    Returns:
        None: This function currently returns None.
    """
    return None
