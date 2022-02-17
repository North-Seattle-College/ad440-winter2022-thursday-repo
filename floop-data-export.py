import sys
import boto3
import argparse
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json
import pandas as pd


# Initiate Argparse for command line arguments and instructions for '--help'.
parser = argparse.ArgumentParser(description='Using the data-export script.')
parser.add_argument("fp", type=str,
                    help="1st arg: This is the credentials filepath variable")
parser.add_argument("db", choices=["Dev", "Prod"],
                    type=str, help="2nd arg: Floop db to export from ('Dev'|'Prod')")
parser.add_argument(
    "n", type=int, help="3rd arg: number of oversations to query")

args = parser.parse_args()
fp = args.fp
dbase = args.db
quantity = args.n
print('filepath: ' + fp + '\ndatabase: ' +
      dbase + '\nqueries: ' + str(quantity))

# Try clause to handle exceptions should firebase credentials path not be valid.
#    On Exception, will display clear instructions and exit gracefully.
#    On success, will initialize floop db connection, and pull feedback comments.
try:
    cred = credentials.Certificate(fp)
    pass
except Exception as e:
    print("Oops!", e.__class__, "occurred.")
    sys.exit('File not found, check Floop credentials file path and try again.')
else:
    firebase_admin.initialize_app(cred)

    db = firestore.client()

    collection = 'Databases/{}_Database/Conversations'.format(dbase)
    conditionals = ['What is your goal for this year?',
                    'Audio Comment', 'Freeform', 'Freeform Comment', '', ' ']

# Pull conversation documents where 'Comment_Preview' field isn't certain
#   text, and pulling a limit of 10k.
    conversations = db.collection(collection).where(
        'Comment_Preview', 'not-in', conditionals).limit(quantity).get()


if __name__ == '__main__':

# Iniialize empty list, "cList"
    cList = []


# For each item in Conversations, each entry has a Messages collection

# all documents will be ordered by 'Date_Submitted' and only the first comment will be pulled.
#    get value of "Text" field and add to cList
    for convo in conversations:
        tempArr = []
        # print(convo.id)
        # Creating dictionary for mapping Sender ID to Teacher or Student
        t_s_mapper = convo.to_dict()['Participant_IDs']

        convo_entries = convo.reference.collection(
            'Messages').order_by(u'Date_Submitted').get()

        for entry in convo_entries:
            # Checking for non-empty strings only
            if entry.get("Text").strip() != '':

                tempArr.append({
                    'Text': entry.get("Text").strip(),
                    'uid': t_s_mapper[entry.get("Sender_ID").strip()]
                })
        if tempArr not in cList:
            cList.append(tempArr)

    # df = pd.DataFrame(cList)
    #df.drop_duplicates(subset='Text', inplace=True)



# Initiate s3 connection to desired bucket and default object filename.
    s3 = boto3.resource('s3')
    s3object = s3.Object('ad440-mpg-floop-export-storage',
                         'auto-floop-s3-export3.json')


# Put json of list into object and put into s3 bucket.
    s3object.put(
        Body=(bytes(json.dumps(cList).encode('UTF-8'))), ContentType='application/json'
    )

