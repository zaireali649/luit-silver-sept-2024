"""Script for list buckets."""
import boto3  # Import the Boto3 library to interact with AWS services

s3 = boto3.client('s3')  # Create an S3 client to interact with the S3 service

response = s3.list_buckets()  # Call the list_buckets method to retrieve a list of all S3 buckets

buckets = response["Buckets"]  # Extract the list of buckets from the response

# Iterate over each bucket in the list and print its name
for bucket in buckets:
    print(bucket["Name"])
