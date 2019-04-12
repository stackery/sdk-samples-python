import boto3
import os

# Create an DynamoDB client
dynamo = boto3.client('dynamodb')
table_name = os.environ['TABLE_NAME'] # Supplied by Function service-discovery wire

def handler(message, context):
  # Add items to your Dynamo Table
  response = dynamo.batch_write_item(
    RequestItems={
      table_name: [
        {
          'PutRequest': {
            'Item': {
              'id': {
                'S': 'aaa'
              },
              'ItemName': {
                'S': 'Item1'
              },
              'User': {
                'S': 'Jon'
              },
              'Account': {
                'N': '1'
              }
            }
          },
          'PutRequest': {
            'Item': {
              'id': {
                'S': 'bbb'
              },
              'ItemName': {
                'S': 'Item2'
              },
              'User': {
                'S': 'Amy'
              },
              'Account': {
                'N': '2'
              }
            }
          }
        },
      ]
    },
  )
  return response