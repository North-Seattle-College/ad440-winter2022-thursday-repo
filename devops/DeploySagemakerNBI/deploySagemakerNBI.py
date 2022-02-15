
import boto3
from os.path import dirname
import argparse


# function to deploy SageMaker basic notebook instance
# parameters: CloudFormation template file in json format, initials to use in stack name
def create_sagemaker_nbi(cf_template, initials, region):
    # print starting message
    print('Stack and notebook instance creation starting using initials:' + \
        initials + ' and region:' + region)
    
    # create stack and notebook names
    stack_name = initials + '-sagemaker-notebook-stack'
    notebook_name = initials + '-sagemaker-notebook-instance'

    # create CloudFormation client
    cf_client = boto3.client('cloudformation', region)

    # check if stack exists
    paginator = cf_client.get_paginator('list_stacks')
    for page in paginator.paginate():
        for stack in page['StackSummaries']:
            if stack['StackStatus'] == 'DELETE_COMPLETE':
                continue
            if stack['StackName'] == stack_name:
                print('Error: stack already exists.')
                exit()

# deploy new stack and SageMaker notebook instance       
    cf_client.create_stack(StackName = stack_name, TemplateBody = cf_template, \
        Parameters = [{'ParameterKey': 'NotebookNameParameter', \
        'ParameterValue': str(notebook_name)}], Capabilities = ['CAPABILITY_IAM'])
    waiter = cf_client.get_waiter('stack_create_complete')
    waiter.wait(StackName = stack_name)
    print(stack_name + 'created successfully.')


# main function
if __name__ == "__main__":
    # create argument parser and params for initials and AWS region
    parser = argparse.ArgumentParser()
    parser.add_argument('--initials', type = str, required = True)
    parser.add_argument('--region', type = str, required = True)
    
    # get args as variables
    args = parser.parse_args()
    initials = args.initials
    region = args.region

    # open CloudFormation template
    script_dir = dirname(__file__)
    cf_template = ''
    with open(f"{script_dir}/sagemakerStackTemplate.json", 'r') as fd:
        cf_template = fd.read()
    
    # call function to create notebook instance
    create_sagemaker_nbi(cf_template, initials, region)