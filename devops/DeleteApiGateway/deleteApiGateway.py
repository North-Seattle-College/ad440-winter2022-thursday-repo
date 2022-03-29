#!/usr/bin/env python3
# Path: devops\DeleteApiGateway\deleteApiGateway.py

from tabnanny import check
import boto3
import argparse


def main():
    """Main funnction that lists all api gateways and deletes them.

    Keyword arguments:
    --region :The AWS region where the api gateway is located
    --forceDelete :Force delete the api gateway in the selected region
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--region', type=str, required=True,
                        help='AWS region where the api gateway is located')
    parser.add_argument('--forceDelete', action='store_true',
                        help='warning: This will force delete all the api gateways in the selected region')
    args = parser.parse_args()
    # connect to aws and list all the api gateways in the selected region
    client = boto3.client('apigateway', region_name=args.region)
    response = client.get_rest_apis()

    # print the api gateway names in the selected region
    for api in response['items']:
        print(api['name'])
    # delete all the api gateways in the selected region
    if args.forceDelete:
        delete_all_apis(client, response)
    # else tell the re-run the script with --forceDelete and exit
    else:
        print("Please re-run the script with --forceDelete and try again")
        exit()


def delete_all_apis(client, response):
    """Delete all the api gateways in the selected region.

    Keyword arguments:
    client :The boto3 client object
    response :The response object from the list_apis function
    """
    for api in response['items']:
        response = client.delete_rest_api(restApiId=api['id'])
        print("All the api gateways in the selected region have been deleted")


# # run the main function
if __name__ == '__main__':
    main()
