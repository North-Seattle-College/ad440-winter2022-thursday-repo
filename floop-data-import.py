from decimal import Decimal
import json
from xml.etree.ElementTree import Comment
import boto3


def load_conversation(conversation, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Conversation')
    for conversation in conversation:
        id = int(conversation['id'])
        print("Adding conversation:", id)
        table.put_item(Item=Comment)


if __name__ == '__main__':
    with open("floop-conv-data.json") as json_file:
        conversation_list = json.load(json_file, parse_float=Decimal)
    load_conversation(list)
