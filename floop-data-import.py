
import json 
from xml.etree.ElementTree import Comment
import boto3 


def load_conversation(conversations, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Conversation')
    i=1000
    # Loop through all the items and load each
    for conversation in conversations:
       
        table.put_item(Item={"comment": conversation, "id": i})
        i+=1

if __name__ == '__main__':
    # open file and read the data in it
    with open("floop-conv-data.json",encoding="utf-8") as json_file:
        conversation_list = json.load(json_file)
    load_conversation(conversation_list)
