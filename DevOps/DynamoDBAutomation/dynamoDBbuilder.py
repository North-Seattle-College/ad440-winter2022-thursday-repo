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
    table_status = stack['Stacks'][0]['StackStatus']

# return the table status
    return table_status


# accept the table name and key name from the user
tableName = input("Enter the table name: ")
keyName = input("Enter the key name: ")


# deploy the template and print the table status
if __name__ == '__main__':
    table_status = create_dynamodb_table(
        tableName, keyName, 'createDynamoDB.json')
    print(table_status)
