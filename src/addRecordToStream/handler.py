import boto3
import os

# Create an Kinesis client
kinesis = boto3.client('kinesis')
stream_name = os.environ['STREAM_NAME'] # Supplied by Function service-discovery wire

def handler(message, context):
  # Publish a sample record to the specified Kinesis stream
  response = kinesis.put_record(
      StreamName=stream_name,
      Data='Sample Record',
      PartitionKey='123'
  )
  return response