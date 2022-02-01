import boto3
import os

# function to deploy SageMaker basic notebook instance
# parameters: CloudFormation template file in json format, initials to use in stack name
def create_sagemaker_nbi(cf_template, initials):

    # create stack name
    stack_name = initials + '-sagemaker-notebook-stack'

    # create CloudFormation client
    cf_client = boto3.client('cloudformation')

    # check if stack exists
    paginator = cf_client.get_paginator('list_stacks')
    for page in paginator.paginate():
        for stack in page['StackSummaries']:
            if stack['StackStatus'] == 'DELETE_COMPLETE':
                continue
            if stack['StackName'] == stack_name:
                print('Error: stack already exists.\n')
                exit()

# deploy new stack and SageMaker notebook instance       
    cf_client.create_stack(StackName = stack_name, TemplateBody = cf_template, Capabilities = ['CAPABILITY_IAM'])
    waiter = cf_client.get_waiter('stack_create_complete')
    waiter.wait(StackName = stack_name)
    print(stack_name + 'created successfully.\n')


# test script with CloudFormation template
from os.path import dirname
script_dir = dirname(__file__)
cf_template = ''
with open(f"{script_dir}/sagemaker_nbi.json", 'r') as fd:
	cf_template = fd.read()
create_sagemaker_nbi(cf_template, input('Enter initials: '))