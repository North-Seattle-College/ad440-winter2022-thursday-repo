#Deploys a stack and S3bucket to cloudformation.

#Imports Python libraries
import boto3
import re
import sys
import argparse
import random
import string
import subprocess
import logging
from datetime import date
from os.path import dirname
script_dir = dirname(__file__)

#Sets logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
file_handler = logging.FileHandler('deployStackS3Bucket.log')
file_handler.setFormatter(formatter)
streamHandler = logging.StreamHandler(sys.stdout)
streamHandler.setLevel(logging.INFO)
logger.addHandler(file_handler)
logger.addHandler(streamHandler)

#Creates cloudformation client
cf_client = boto3.client('cloudformation', region_name='us-west-2')

#Requires user initials input parameter.
def main(input_initials):

    #Read in stack template file
    stack_template = _stack_template_file()

    #Parses input initials
    parser = argparse.ArgumentParser(description='Input Initials Required.')
    parser.add_argument('input_initials', 
                        metavar='input_initials', 
                        help='Input User Initials To Use In Stack Name.', 
                        nargs='?', 
                        type=str)

    args = parser.parse_args()

    #Gets initials
    initials = args.input_initials
    logger.info("Your Initials Entered: " + initials + "\n")

    #Gererates unique id
    unique_id = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(5))

    #Gets the date
    date_created = date.today().strftime("%m%d%y")

    #Uses initials, date, and unique id for stack name
    delimiter = "-"
    stack_vars = (initials, date_created, unique_id, 'stack')
    stack_name = delimiter.join(stack_vars)
    
    #Uses stack with bucket name
    bucket_vars = (stack_name, 'reactapp', 'bucket')
    bucket_name = delimiter.join(bucket_vars)

    #Sets bucket name parameter
    parameters=_set_parameters(bucket_name)
    
    #Creates stack and S3bucket
    _create_stack_s3bucket(initials, stack_name, bucket_name, stack_template, parameters)

#Verifies initials and creates new stack
def _create_stack_s3bucket(initials, stack_name, bucket_name, stack_template, parameters):
    patternAlpha = re.compile("[A-Za-z]+")
    if patternAlpha.fullmatch(initials)==None:
        logger.error("Initials Must Contain Alphabetic Characters Only.\n")
    elif len(initials) == '':
        logger.error("Initials Must Not Be Empty.\n")
    elif len(initials) < 2:
        logger.error("Initials Must Be At Least 2 characters Long.\n")
    elif len(initials) > 5:
        logger.error("Initials Must Not Be More Than 5 characters Long.\n")
    else:
        logger.info("Your Stack Will Be Named: " + "'" + stack_name + "'\n")
        logger.info("Your S3Bucket Will Be Named: " + "'" + bucket_name + "'\n")
        logger.info("Please Wait While Your Stack and S3Bucket Are Being Deployed To Cloudformation.\n")
        logger.info("Waiting...\n")
        #Checks if stack already exists
        if _stack_exists(stack_name):
            logger.error("A Stack Named " + "'" + stack_name + "' Already Exists, Please Try Again.\n")
        else:
            #Creates stack and S3bucket
            stack_result = cf_client.create_stack(StackName=stack_name, TemplateBody=stack_template, Parameters=parameters)
            waiter = cf_client.get_waiter('stack_create_complete')
            waiter.wait(StackName=stack_name)
            logger.info("Congradulations! Your Stack " + stack_name + " And S3Bucket " + bucket_name + " Are Now Completed.\n")
            #Echos bucket name as Github environment variable
            echo_arg = ("echo BUCKET_NAME=" + bucket_name + " >> $GITHUB_ENV")
            subprocess.Popen(echo_arg, shell=True)
            logger.debug(echo_arg)

#Reads in stack template file
def _stack_template_file():
    stack_template = ''
    with open(f"{script_dir}/StackTemplate.json", 'r') as fd:
        stack_template = fd.read()
    return stack_template

# Verifies if stack already exists
def _stack_exists(stack_name):
    paginator = cf_client.get_paginator('list_stacks')
    for page in paginator.paginate():
        for stack in page['StackSummaries']:
            if stack['StackStatus'] == 'DELETE_COMPLETE':
                continue
            if stack['StackName'] == stack_name:
                return True

#Sets parameters
def _set_parameters(bucket_name):
    return [ { 'ParameterKey': 'BucketName',
               'ParameterValue': bucket_name } ]

#Runs main program
if __name__ == '__main__':
    main(*sys.argv[1:])