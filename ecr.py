# boto3 - to create any resource in aws you need boto3
import boto3


ecr_client = boto3.client('ecr', region_name='ap-south-1')

repository_name = 'cloud-native-monitoring-app'
response = ecr_client.create_repository(repositoryName=repository_name)

repository_uri = response['repository']['repositoryUri']
print(repository_uri)