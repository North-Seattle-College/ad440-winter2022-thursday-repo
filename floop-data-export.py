import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json
import os

# Get path of firebase cert from user. Prompt user if path doesnt exist
while True:
    certLoc = input('Enter full path of Floop Firebase cert file: ')
    gPath = os.path.exists(certLoc)

    if(gPath):
        break
    else:
        print('File not found, please re-enter file path')

# Use cert file to initialize app access and
#   connect to Dev_Database Conversations collection
cred = credentials.Certificate(certLoc)
firebase_admin.initialize_app(cred)

db = firestore.client()

# pull conversation documents where 'Comment_Preview' field isn't certain
#   text, and pulling a limit of 10k.
conversations = db.collection(
    'Databases/Dev_Database/Conversations').where('Comment_Preview', 'not-in', [
        'What is your goal for this year?', 'Audio Comment', 'Freeform', 'Freeform Comment', '', ' ']).limit(10000).get()

if __name__ == '__main__':

    # Iniialize empty list, "cList"
    cList = []
# For each item in Conversations, ea entry has a Messages collection
# all documents will be ordered by 'Date_Submitted' and only the first comment will be pulled.
# For each document in the pulled list(currently limited to 1 per collection),
#    get value of "Text" field and add to cList

    for convo in conversations:
        convo_entries = convo.reference.collection(
            'Messages').order_by(u'Date_Submitted').limit(1).get()

        for entry in convo_entries:
            cList.append(entry.get("Text").strip())

# Convert cList to a Set to remove duplicate values
#   -- faster than populating set initially
# Convert back to list so json.dump can process it
    arr = set(cList)
    new_arr = list(arr)

# Write contents of list to json file
    with open('floop-conv-data.json', 'w') as f:
        json.dump(new_arr, f)
