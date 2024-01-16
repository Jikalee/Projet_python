import boto3

s3 = boto3.resource("s3")

bucket = s3.Bucket("mrspython123")

bucket.upload_file(Filename="./donnees.csv", Key="donnees.csv")

