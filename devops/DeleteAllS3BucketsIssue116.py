#s3BucketDelete.py for issue 87 Create a cleanup script for all s3 buckets 1jc
#revision for issue 116 Sprint 4 Fix issue #87 Fix script to delete all s3 buckets even with data 1jc

import boto3
client = boto3.client('s3')
response = client.list_buckets()
for name in response ['Buckets']:
    print (name['Name'])

response = client.delete_buckets()
print(response)
