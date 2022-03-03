#s3BucketDelete.py for issue 87 Create a cleanup script for all s3 buckets 1jc

import boto3
client = boto3.client('s3')

#need name of bucket for delete

bucket_name = str (input ('Please provide bucket name to be deleted: '))
print ('Before deleting the bucket we need to check if its empty.  Checking...')
       
#need to check if bucket is empty
       
objs = client.list_objects_v2 (Bucket = bucket_name)
filecount = objs ['KeyCount']
print (filecount)
filecount = objs ['KeyCount']
       
#need to make sure filecount is zero
       
if filecount == 0:
       response = client.delete_bucket(
       Bucket = bucket_name)
       print ('{} has been deleted successfully!!!'.format (bucket_name))
       
#will not delete s3 bucket if filecount > zero must be empty
       
else:
       print ('{} is not empty!!!'.format (bucket_name))
       print ('Please make sure s3 bucket is empty before deleting!!!')
