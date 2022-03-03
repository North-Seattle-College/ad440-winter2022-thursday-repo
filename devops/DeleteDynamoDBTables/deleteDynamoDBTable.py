import boto3
import argparse
import sys


def main():
    """Main funnction that lists all tables in the specified aws region and propmpts the user to delete a table.

    Keyword arguments:
    --region :The AWS region where the DyanmoDB table is located
    --tableName :The name of the table to be deleted
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--region', type=str, required=True,
                        help='AWS region where the table is located')
    parser.add_argument('--tableName', type=str,
                        help='The name of the table to be deleted')
    args = parser.parse_args()
    # connect to aws and list all the tables in the selected region
    client = boto3.client('dynamodb', region_name=args.region)
    response = client.list_tables()

    # print the table names in the selected region
    for table in response['TableNames']:
        print(table)
    # ask the the user if he wants to delete all the tables in the selected region
    if args.tableName is None:
        if input("Do you want to delete all the tables in the selected region?(y/n)") == "y":
            # call the delete all tables function
            delete_all_tables(client, response)
        else:
            # ask the user to re-run the script with the table name to be deleted
            print("Please re-run the script with the table name to be deleted")
            sys.exit(1)
    else:
        # call the delete table function
        delete_table(client, args.tableName, response)

# A function that'll delete all the tables in the selected region


def delete_all_tables(client, response):
    """Delete all the tables in the selected region.

    Keyword arguments:
    client :The boto3 client object
    response :The response object from the list_tables function
    """
    for table in response['TableNames']:
        response = client.delete_table(TableName=table)
        print("All the tables in the selected region have been deleted")

# A function that'll only delete the table specified in the command line argument


def delete_table(client, tableName, response):
    """Delete the table specified in the command line.

    Keyword arguments:
    client :The boto3 client object
    tableName :The name of the table to be deleted
    response :The response from the list_tables function
    """
    for table in response['TableNames']:
        if table == tableName:
            response = client.delete_table(TableName=tableName)
            print("The table has been deleted successfully")
        else:
            print("The table does not exist")


# run the main function
if __name__ == '__main__':
    main()
