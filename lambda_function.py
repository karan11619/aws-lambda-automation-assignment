import boto3
from datetime import datetime, timezone, timedelta

s3 = boto3.client("s3")

BUCKET_NAME = "praba-s3-cleanup-demo"


AGE_LIMIT = timedelta(days=30)

def lambda_handler(event, context):
    paginator = s3.get_paginator("list_objects_v2")
    now = datetime.now(timezone.utc)
    deleted = []

    for page in paginator.paginate(Bucket=BUCKET_NAME):
        if "Contents" not in page:
            continue

        for obj in page["Contents"]:
            age = now - obj["LastModified"]

            if age > AGE_LIMIT:
                s3.delete_object(
                    Bucket=BUCKET_NAME,
                    Key=obj["Key"]
                )

                print(f"Deleted: {obj['Key']}")
                deleted.append(obj["Key"])

    return {
        "deleted": deleted
    }