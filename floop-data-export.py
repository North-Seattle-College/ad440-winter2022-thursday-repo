import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json
import os

# Get path of firebase cert from user. Prompt user if path doesnt exist
while True:
    certLoc = input('Enter full path of Floop Firebase cert file: ')
    gPath = os.path.isfile(certLoc)

#    n = int(input('Enter the number of conversations required: '))
#   Removing input due to CLI integration as suggested
    n=100

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
#   text, and pulling a limit of 1k.
conversations = db.collection(
    'Databases/Dev_Database/Conversations').where('Comment_Preview', 'not-in', [
        'What is your goal for this year?', 'Audio Comment', 'Freeform', 'Freeform Comment', '', ' ']).limit(n).get()

if __name__ == '__main__':

    # Iniialize empty list, "cList"
    cList = []
    
# For each item in Conversations, each entry has a Messages collection
# all documents will be ordered by 'Date_Submitted' and only the first comment will be pulled.
#    get value of "Text" field and add to cList

    for convo in conversations:

        # Creating dictionary for mapping Sender ID to Teacher or Student
        t_s_mapper = convo.to_dict()['Participant_IDs']

        convo_entries = convo.reference.collection(
            'Messages').order_by(u'Date_Submitted').get()

        for entry in convo_entries:
            # Checking for non-empty strings only
            if entry.get("Text").strip()!='':

                cList.append({
                    'Text': entry.get("Text").strip(),
                    'uid': t_s_mapper[entry.get("Sender_ID").strip()]
                })


# Write contents of document to json file
    with open('floop-conv-data_N.json', 'w') as f:
        json.dump(cList, f)
