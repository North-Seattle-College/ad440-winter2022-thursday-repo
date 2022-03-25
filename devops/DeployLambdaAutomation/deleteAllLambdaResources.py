
from tabnanny import check
import boto3
import argparse


def main():
    #Main funnction that lists all functions in the specified aws region and propmpts the user to delete a function.
    parser = argparse.ArgumentParser()
    parser.add_argument('--region', type=str, required=True,
                        help='AWS region where the functions are located')
    parser.add_argument('--functionName', type=str,
                        help='The name of the lambda function to be deleted')
    parser.add_argument('--cleanAllLambda', action='store_true',
                        help='warning: This will force delete all the lambda functions in the selected region')
    args = parser.parse_args()
    # connect to aws and list all the functions in the selected region
    client = boto3.client('lambda', region_name=args.region)
    response = client.list_functions()

  # print the functions names in the selected region
    for function in response['Functions']:
        print(function['FunctionName'])

  # if --cleanAllLambda is specified, call the delete all lambda function
    if args.cleanAllLambda:
        delete_all_functions(client, response)
    # if --functionName is specified call the delete lambda function
    elif args.functionName is not None:
        delete_function(client, args.functionName, response)


# This function delete all the lamda resources in the selected region

def delete_all_functions(client, response):
    #Delete all the lambda in the selected region.
    for function in response['Functions']:
        response = client.delete_function(FunctionName=function['FunctionName'])
    print("All the lambda resources have been deleted")

# This function deletes only the lambda function that was entered  command line argument
def delete_function(client, functionName, response):
    ##Delete the lambda specified in the command line.
    for function in response['Functions']:
        if function['FunctionName'] == functionName:
            response = client.delete_function(FunctionName=functionName)
            print("The function that was entered is deleted")
            break
    else:
        print("The function entered doesn't exist")


# run the main function
if __name__ == '__main__':
    main()
