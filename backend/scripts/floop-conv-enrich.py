import json
import boto3

# Initiate s3 connection to desired bucket and desired object filename.
s3 = boto3.resource('s3')

obj = s3.Object('ad440-mpg-floop-export-storage', 'auto-floop-s3-export3.json')

# Loads body of json from the s3 object
data = json.load(obj.get()['Body'])
# after ], add '.read().decode('utf-8)' ?  try json.loads instead?

print(data[3][1])

# Create temp list of 10 items from the s3 file for modifying data elements
fbList = []
for x in range(10):
    fbList.append(data[x])

print(fbList[3][1])

# Plaeholder variables for string formatting - to be replaced with question/statement,
#   positive/negative/neutral, and emotion matching later...?
question = 'Test1'
posNeg = 'Test2'
emotion = 'Test4'

# For each item in fbList, check # of dictionaries in item. For each dictionary, update
#   with new key:value of <'metadata':array of length 3> -- formatted for ea placeholder
for x in fbList:
    for y in range(len(x)):
        # - x[y].get('Text') - retrieve the value for key 'Text' (the fedback/replies to analyze)
        # run Text value through analyzers?
        # save results into appropriate variables above?

        # This updates each comment dictionary in fbList with metadata K:V.
        x[y].update(
            metadata=['{}'.format(question), '{}'.format(
                posNeg), '{}'.format(emotion)]
        )

print(fbList[1])
print(fbList[3])


# Define new object to be put in s3
enrichObj = s3.Object('ad440-mpg-floop-export-storage',
                      'enriched-conv-sample.json')

# Put json of fbList into object and put into s3 bucket.
enrichObj.put(
    Body=(bytes(json.dumps(fbList).encode('UTF-8'))), ContentType='application/json'
)
