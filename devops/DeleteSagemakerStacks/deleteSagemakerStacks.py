import boto3
import argparse

# main driver function that identifies and deletes SageMaker stacks
# argument --region: the AWS region for the CloudFormation client
# argument --prefix: add a prefix to narrow results to specific stacks for testing
# argument --live_run: add this flag to confirm deleted of identified stacks on program execution
# argument --confirm_delete: add this flag to wait for confirmation of each completed stack (slow)
def main():
    
    # create arguments for AWS region, flag for live run, and flag for confirm stack deletion
    parser = argparse.ArgumentParser()
    parser.add_argument('--region', type = str, required=True, help='AWS region for CloudFormation client')
    parser.add_argument('--prefix', type=str, help='enter a prefix to be added to the sagemaker search string for testing purposes')
    parser.add_argument('--live_run', action='store_true', help='warning: identified stacks will be deleted on execution')
    parser.add_argument('--confirm_delete', action='store_true', help='wait for confirmation of deletion for each stack - this will take awhile')
    args = parser.parse_args()
    
    # create CloudFormation client in specified region
    cf_client = boto3.client('cloudformation', args.region)

    # only check for stacks with these statuses
    status_filter = ['CREATE_COMPLETE', 'UPDATE_COMPLETE', 'ROLLBACK_COMPLETE']

    # create paginator and iterate through stacks
    paginator = cf_client.get_paginator('list_stacks')
    response_iterator = paginator.paginate(StackStatusFilter=status_filter)
    # store stacks in list
    stacks = []
    for response in response_iterator:
        stacks += [stack['StackName'] for stack in response['StackSummaries']]
    
    # find sagemaker stacks
    query = 'sagemaker'
    # add prefix to query if provided
    if args.prefix is not None:
        query = args.prefix + 'sagemaker'
    # check stacks with query and add to list
    sagemaker_stacks = []
    for stack_name in stacks:
        if query in stack_name:
            sagemaker_stacks.append(stack_name)
    
    # live_run is off: print identified stacks
    if args.live_run == False:
        print('The following SageMaker stacks were identified:')
        print(sagemaker_stacks)
        print('To proceed with deletion, run script with --live_run argument')
    
    # live_run is on: delete identified stacks
    if args.live_run == True:
        for target_stack in sagemaker_stacks:
            cf_client.delete_stack(StackName=target_stack)
            print(target_stack + ' deletion started')
            # wait for confirmation of deletion for each stack (slow)
            if args.confirm_delete == True:
                waiter = cf_client.get_waiter('stack_delete_complete')
                waiter.wait(StackName=target_stack)
                print(target_stack + ' deleted successfully')
            
# run main function
if __name__ == "__main__":
    main()