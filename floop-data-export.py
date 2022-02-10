import sys
import boto3
import argparse
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

# Initiate Argparse for command line arguments and instructions for '--help'.
parser = argparse.ArgumentParser(description='Using the data-export script.')
parser.add_argument("fp", type=str,
                    help="1st arg: This is the credentials filepath variable")
parser.add_argument("db", choices=["Dev", "Prod"],
                    type=str, help="2nd arg: Floop db to export from ('Dev'|'Prod')")

args = parser.parse_args()
fp = args.fp
dbase = args.db
print('filepath: ' + fp + '\ndatabase: ' + dbase)

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
        'Comment_Preview', 'not-in', conditionals).limit(10).get()

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

# Initiate s3 connection to desired bucket and default object filename.
    s3 = boto3.resource('s3')
    s3object = s3.Object('ad440-mpg-floop-export-storage', 'auto-export-test.json')

# Put json of list into object and put into s3 bucket.
    s3object.put(
        Body=(bytes(json.dumps(new_arr).encode('UTF-8'))), ContentType='application/json'
    )