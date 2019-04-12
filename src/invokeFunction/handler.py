import boto3
import os
import json

# Create an Lambda client
lambda_client = boto3.client('lambda')
function_name = os.environ['FUNCTION_NAME'] # Supplied by Function service-discovery wire

def handler(message, context):
  params = {
    "source": "invokeFunction",
    "content": "SampleData"
  }

  # Invoke another Function
  response = lambda_client.invoke(
      FunctionName=function_name,
      Payload=json.dumps(params)
  )
  return