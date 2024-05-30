import json
import boto3

client = boto3.client('sns')

def lambda_handler(event, context):
    response = client.publish(TopicArn='arn:aws:sns:<REGION>:<AWS_ACCOUNT_ID>:<SNS TOPIC NAME>',Message="Test message")
   
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
