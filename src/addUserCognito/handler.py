import boto3
import os

# Create an Cognito Identity Provider client
cognito = boto3.client('cognito-idp')
user_pool_client_id = os.environ['USER_POOL_CLIENT_ID'] # Supplied by Function service-discovery wire

def handler(message, context):
  # Add a new user to your User Pool
  response = cognito.sign_up(
      ClientId=user_pool_client_id,
      Username='NewUser_99',
      Password='Password$123',
      UserAttributes=[
        {
          'Name':'email',
          'Value':'test@email.com'
        }
      ]
  )
  return response
Copy to clipboard
