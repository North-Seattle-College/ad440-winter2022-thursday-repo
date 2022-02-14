# reads the createDynamoDB.json file and creates a stack
import json
import boto3


# wrap the operation in a function
def create_dynamodb_table(tableName, keyName, cfTemplate):
    """Given a table name, key name and CFT template, it'll create a DynamoDB table.

    Keyword arguments:
    tableName -- the DyanmoDB table name
    keyName -- the partion key name
    cfTemplate -- the file path to the cloud formation template json
    """
    cfnclient = boto3.client('cloudformation')

    # open the template file
    with open(cfTemplate) as fd:
        template = json.load(fd)

    # update the template with the table name and hash key name
    template["Resources"]["DynamoDBTable"]["Properties"]["TableName"] = tableName
    template["Resources"]["DynamoDBTable"]["Properties"]["AttributeDefinitions"][0]["AttributeName"] = keyName
    template["Resources"]["DynamoDBTable"]["Properties"]["KeySchema"][0]["AttributeName"] = keyName


# create the stack
    cfnclient.create_stack(StackName=tableName,
                           TemplateBody=json.dumps(template)
                           )

# wait for the stack to complete
    waiter = cfnclient.get_waiter('stack_create_complete')
    waiter.wait(StackName=tableName)

# get the stack output
    stack = cfnclient.describe_stacks(StackName=tableName)


# update to script to run python dynamoDBbuilder.py --tableName sometableName --keyName keySchemaName
if __name__ == "__main__":
    import argparse
    import sys
    parser = argparse.ArgumentParser()
    parser.add_argument("--tableName")
    parser.add_argument("--keyName")
    args = parser.parse_args()

    # check if the tableName already exists and print it already exists, if not create it and print the status
    try:
        table_status = create_dynamodb_table(
            args.tableName, args.keyName, 'dynamoDBStackTemplate.json')
        print("Table {} Table created successfully".format(args.tableName))
    except Exception as e:
        print("Table {} Table name already exists, please choose a different name".format(
            args.tableName))
        sys.exit(1)
