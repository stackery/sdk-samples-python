import boto3
import os

# Create an SNS client
sns = boto3.client('sns')
topic_arn = os.environ['TOPIC_ARN'] # Supplied by Function service-discovery wire

def handler(message, context):
  notification = "Hello All! \n We've made quite a few changes to our product...";

  # Publish a simple message to the specified SNS topic
  response = sns.publish(
      TopicArn=topic_arn,
      Message=notification,
  )
  return response