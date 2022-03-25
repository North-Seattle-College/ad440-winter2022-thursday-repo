#For deleting all s3 buckets Issue#152 Pull #177

#Step 1 :- export your profile using below command Or you can export access_key and secrete_access_key 

#export AWS_PROFILE=<Your-Profile-Name> 
 
#Step 2:- Use below python code, Run it on local and see your all s3 buckets will delete.

#If you see error like boto3 not found please go to link and install it Install boto3 using pip

import boto3

client = boto3.client('s3')
response = client.list_buckets()
for bucket in response['Buckets']:
    s3 = boto3.resource('s3')
    s3_bucket = s3.Bucket(bucket['Name'])
    bucket_versioning = s3.BucketVersioning(bucket['Name'])
    if bucket_versioning.status == 'Enabled':
        s3_bucket.object_versions.delete()
    else:
        s3_bucket.objects.all().delete()
    response = client.delete_bucket(Bucket=bucket['Name'])

