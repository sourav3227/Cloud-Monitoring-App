# boto3 - to create any resource in aws you need boto3
# To create a ecr repo in aws 
import boto3

ecr_client = boto3.client('ecr', region_name='ap-south-1')

repository_name = "my_monitoring_app_image"
response = ecr_client.create_repository(repositoryName=repository_name)

repository_uri = response ['repository']['repositoryUri']
print(repository_uri)