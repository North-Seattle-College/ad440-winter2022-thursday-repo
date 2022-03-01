#s3BucketList.py for issue 87 Create a cleanup script for all listing of s3 buckets 1jc

import boto3
client = boto3.client('s3')
response = client.list_buckets()
for name in response ['Buckets']:
    print (name['Name'])
