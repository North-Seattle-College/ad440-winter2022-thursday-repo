#Deploys a Stack and S3 Bucket To Cloudformation.
import boto3
import re
import os
import sys
import argparse

from os.path import dirname
script_dir = dirname(__file__)

#Creates Cloudformation Client
cf_client = boto3.client('cloudformation')

def main(input_initials):

    #Read In Stack Template File
    stack_template = _stack_template_file()

    #Parses Input Initials
    parser = argparse.ArgumentParser(description='Input Initials Required.')
    parser.add_argument('input_initials', metavar='input_initials', help='Input User Initials For Stack Name.', nargs='?', type=str)
    args = parser.parse_args()

    #Gets Initials
    initials = args.input_initials
    print("\nYour Initials Entered: " + initials + "\n")

    #Uses Initials For Stack Name
    stack_name = (initials + '-stack')
    
    #Verifies Initials
    patternAlpha = re.compile("[A-Za-z]+")
    if patternAlpha.fullmatch(initials)==None:
        print("Error: Initials Must Contain Alphabetic Characters Only.\n") 
    elif len(initials) == '':
        print("Error: Initials Must Not Be Empty.\n")
    elif len(initials) < 2:
        print("Error: Initials Must Be At Least 2 characters Long.\n")
    elif len(initials) > 5:
        print("Error: Initials Must Not Be More Than 5 characters Long.\n")  
    else:
        print("Your Stack Will Be Named: " + "'" + stack_name + "'\n")
        print("Please Wait While Your Stack and S3Bucket Are Being Deployed To Cloudformation.")
        print("Waiting...\n")
        if _stack_exists(stack_name):
            print("Error: A Stack Named " + "'" + stack_name + "' Already Exists, Please Try Again.\n")
        else:
            stack_result = cf_client.create_stack(StackName=stack_name, TemplateBody=stack_template)
            waiter = cf_client.get_waiter('stack_create_complete')
            waiter.wait(StackName=stack_name)
            print("Congradulations! Your Stack " + stack_name + " And S3Bucket Are Now Completed.\n")
            
#Reads in Stack Template File
def _stack_template_file():
    stack_template = ''
    with open(f"{script_dir}/stack_template.json", 'r') as fd:
        stack_template = fd.read()
    return stack_template

#Checks if Stack Already Exists
def _stack_exists(stack_name):
    paginator = cf_client.get_paginator('list_stacks')
    for page in paginator.paginate():
        for stack in page['StackSummaries']:
            if stack['StackStatus'] == 'DELETE_COMPLETE':
                continue
            if stack['StackName'] == stack_name:
                return True

if __name__ == '__main__':
    main(*sys.argv[1:])