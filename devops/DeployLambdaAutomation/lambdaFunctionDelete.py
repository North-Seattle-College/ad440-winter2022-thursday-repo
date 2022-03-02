import boto3
import argparse

lambda_client = boto3.client('lambda')

#access the delete  function argumnet from the command line
parser = argparse.ArgumentParser()
parser.add_argument("--functionName")
args = parser.parse_args()

#delete  the specific lamda function pass in the argument
response = lambda_client.delete_function(FunctionName=args.functionName)

print('Lambda function deleted')