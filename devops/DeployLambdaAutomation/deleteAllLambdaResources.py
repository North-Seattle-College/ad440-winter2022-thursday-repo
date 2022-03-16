
from tabnanny import check
import boto3
import argparse


def main():
    #Main funnction that lists all tables in the specified aws region and propmpts the user to delete a table.
    parser = argparse.ArgumentParser()
    parser.add_argument('--region', type=str, required=True,
                        help='AWS region where the table is located')
    parser.add_argument('--functionName', type=str,
                        help='The name of the table to be deleted')
    parser.add_argument('--cleanAllLambda', action='store_true',
                        help='warning: This will force delete all the tables in the selected region')
    args = parser.parse_args()
    # connect to aws and list all the tables in the selected region
    client = boto3.client('lambda', region_name=args.region)
    response = client.list_functions()

  # print the table names in the selected region
    for function in response['Functions']:
        print(function['FunctionName'])

  # if --cleanAllLambda is specified, call the delete all tables function
    if args.cleanAllLambda:
        delete_all_functions(client, response)
    # if --functionName is specified call the delete table function
    elif args.functionName is not None:
        delete_function(client, args.functionName, response)


# This function delete all the lamda resources in the selected region

def delete_all_functions(client, response):
    #Delete all the lambda in the selected region.
    for function in response['Functions']:
        response = client.delete_function(FunctionName=function)
        print("All the tables in the selected region have been deleted")

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
