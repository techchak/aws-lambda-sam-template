import boto3
import os
ec2 = boto3.resource('ec2')
client = boto3.client('sns')

SNS_ARN = os.environ['SNS_ARN']
INSTANCE_TYPE = os.environ['INSTANCE_TYPE']
KEY_NAME = os.environ['KEY_NAME']
AMI=os.environ['AMI']
SUBNET_ID=os.environ['SUBNET_ID']
SNS_MESSAGE = os.environ['SNS_MESSAGE']


def lambda_handler(event, context):
    instance = ec2.create_instances(
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME,
        ImageId=AMI,
        SubnetId=SUBNET_ID,
        MaxCount=3,
        MinCount=1,
        TagSpecifications=[{
            'ResourceType': 'instance',
            'Tags': [{'Key': 'Name','Value': 'Dry-run'}]
        }]   
    )
    print("New instance created:", instance[0].id)
   
    response = client.publish(
        TopicArn = SNS_ARN,
        Message = SNS_MESSAGE
        )
    return {'statusCode': 200,}