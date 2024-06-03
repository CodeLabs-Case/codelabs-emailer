import sys
import os

# Add the package directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '../package'))

import boto3
import json
import traceback

def lambda_handler(event, context):
    # Initialize a session using AWS Systems Manager
    session = boto3.session.Session()
    client = session.client(
        service_name='ssm',
        region_name='us-east-1'
    )

    # Retrieve the parameter
    parameter_name = "/davisarchitect99/email_password"
    try:
        response = client.get_parameter(
            Name=parameter_name,
            WithDecryption=True
        )
        parameter_value = response['Parameter']['Value']
        return {
            'statusCode': 200,
            'body': parameter_value
        }
    except client.exceptions.ParameterNotFound:
        print(f"Parameter {parameter_name} not found")
        return {
            'statusCode': 404,
            'body': f"Parameter {parameter_name} not found"
        }
    except client.exceptions.InvalidRequest:
        print(f"Invalid request")
        return {
            'statusCode': 400,
            'body': f"Invalid request"
        }
    except client.exceptions.InternalServerError:
        print(f"Internal server error")
        return {
            'statusCode': 500,
            'body': f"Internal server error"
        }
    except Exception as e:
        print(f"Error retrieving parameter: {e}")
        print(traceback.format_exc())
        return {
            'statusCode': 500,
            'body': f"Error: {e}"
        }