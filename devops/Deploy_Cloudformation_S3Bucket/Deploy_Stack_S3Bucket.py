#Deploys a Stack and S3 Bucket To Cloudformation.
import boto3
import re
import os
import sys

from os.path import dirname
script_dir = dirname(__file__)

#Read In Json Template File
stack_template = ''
with open(f"{script_dir}/StackTemplate.json", 'r') as fd:
	stack_template = fd.read()

print("Deploys a Stack and S3 Bucket To Cloudformation.\n")

patternAlpha = re.compile("[A-Za-z]+")

#Asks For User Initials
initials = ''
while initials != 'q':
    initials = input('Please Enter Your Initials, Or Press "Q" To Quit: ')
    if initials == 'q':
        print("Exiting Program, Goodbye.\n")
        exit()
    elif initials == '':
        print("Error: Initials Must Not Be Empty.\n")
    elif patternAlpha.fullmatch(initials)==None:
         print("Error: Initials Must Contain Alphabetic Characters Only.\n") 
    elif len(initials) < 2:
        print("Error: Initials Must Be At Least 2 characters.\n")
    elif len(initials) > 3:
        print("Error: Initials Must Not Be Longer Than 3 characters.\n")
    else:
        print("\nYour Initials Entered: " + initials + "\n")
        print("Your Stack Will Be Named: " + "'" + initials + "-stack'\n")
        print("Please Wait While Your Stack and S3Bucket Are Being Deployed To Cloudformation.")
        print("Waiting...\n")
        break
       
#Uses User Initials For Stack Name
stack_name = (initials + '-stack')

#Creates Cloudformation Client
cf_client = boto3.client('cloudformation')

#Checks If Stack Already Exists
paginator = cf_client.get_paginator('list_stacks')
for page in paginator.paginate():
    for stack in page['StackSummaries']:
        if stack['StackStatus'] == 'DELETE_COMPLETE':
            continue
        if stack['StackName'] == stack_name:
            print("Error: This Stack Already Exists, Please Try Again.\n")
            exit()

#Deploys New Stack And S3Bucket       
stack_result = cf_client.create_stack(StackName=stack_name, TemplateBody=stack_template)
waiter = cf_client.get_waiter('stack_create_complete')
waiter.wait(StackName=stack_name)
print("Congradulations! Your Stack " + stack_name + " And S3Bucket Is Now Completed.\n")
