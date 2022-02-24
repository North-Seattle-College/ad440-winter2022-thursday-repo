import json
import boto3

s3 = boto3.resource('s3')

obj = s3.Object('ad440-mpg-floop-export-storage', 'auto-floop-s3-export3.json')
# after ], add '.read().decode('utf-8)' ?  try json.loads instead?
data = json.load(obj.get()['Body'])
print(data[3][1])

fbList = []
for x in range(10):
    fbList.append(data[x])

print(fbList[3][1])

question = 'Test1'
posNeg = 'Test2'
sent = 'Test3'
for x in fbList:
    for y in range(len(x)):
        x[y].update(
            metadata=['{}'.format(question), '{}'.format(
                posNeg), '{}'.format(sent)]
        )

print(fbList[1])
print(fbList[3])
