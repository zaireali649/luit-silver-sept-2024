import unittest

# Assuming the functions are imported from the module where they are defined
from helpers import (
    create_ubuntu_instance, 
    create_amazon_linux_2023_instance, 
    create_amazon_linux_2_instance
)

class TestEC2InstanceCreation(unittest.TestCase):
    
    def test_create_ubuntu_instance_default(self):
        """Test create_ubuntu_instance with default values."""
        expected_ami = 'ami-0e86e20dae9224db8'
        expected_instance_type = 't2.micro'
        
        result = create_ubuntu_instance(None)
        
        self.assertEqual(result['ami'], expected_ami)
        self.assertEqual(result['instance_type'], expected_instance_type)

    def test_create_amazon_linux_2023_instance_default(self):
        """Test create_amazon_linux_2023_instance with default values."""
        expected_ami = 'ami-0ebfd941bbafe70c6'
        expected_instance_type = 't2.large'
        
        result = create_amazon_linux_2023_instance(None)
        
        self.assertEqual(result['ami'], expected_ami)
        self.assertEqual(result['instance_type'], expected_instance_type)

    def test_create_amazon_linux_2_instance_default(self):
        """Test create_amazon_linux_2_instance with default values."""
        expected_ami = 'ami-0a5c3558529277641'
        expected_instance_type = 't2.nano'
        
        result = create_amazon_linux_2_instance(None)
        
        self.assertEqual(result['ami'], expected_ami)
        self.assertEqual(result['instance_type'], expected_instance_type)

    def test_create_ubuntu_instance_custom(self):
        """Test create_ubuntu_instance with a custom instance type."""
        expected_ami = 'ami-0e86e20dae9224db8'
        custom_instance_type = 't2.medium'
        
        result = create_ubuntu_instance(None, instance_type=custom_instance_type)
        
        self.assertEqual(result['ami'], expected_ami)
        self.assertEqual(result['instance_type'], custom_instance_type)

    def test_create_amazon_linux_2023_instance_custom(self):
        """Test create_amazon_linux_2023_instance with a custom instance type."""
        expected_ami = 'ami-0ebfd941bbafe70c6'
        custom_instance_type = 't3.micro'
        
        result = create_amazon_linux_2023_instance(None, instance_type=custom_instance_type)
        
        self.assertEqual(result['ami'], expected_ami)
        self.assertEqual(result['instance_type'], custom_instance_type)

    def test_create_amazon_linux_2_instance_custom(self):
        """Test create_amazon_linux_2_instance with a custom instance type."""
        expected_ami = 'ami-0a5c3558529277641'
        custom_instance_type = 't3.large'
        
        result = create_amazon_linux_2_instance(None, instance_type=custom_instance_type)
        
        self.assertEqual(result['ami'], expected_ami)
        self.assertEqual(result['instance_type'], custom_instance_type)

# Run the tests
if __name__ == '__main__':
    unittest.main()
