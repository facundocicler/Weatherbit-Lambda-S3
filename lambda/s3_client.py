import boto3

s3 = boto3.client('s3')

def download_csv_from_s3(bucket, key):
    obj = s3.get_object(Bucket=bucket, Key=key)
    return obj['Body'].read().decode('utf-8-sig')

def upload_csv_to_s3(bucket, key, csv_data):
    s3.put_object(Bucket=bucket, Key=key, Body=csv_data.encode('utf-8-sig'))
