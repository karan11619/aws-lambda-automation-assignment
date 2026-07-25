import boto3
from datetime import datetime, timezone, timedelta

ec2 = boto3.client("ec2")

VOLUME_ID = "vol-0db00758abdee8714"


RETENTION = timedelta(days=30)


def lambda_handler(event, context):
    # Create Snapshot
    snapshot = ec2.create_snapshot(
        VolumeId=VOLUME_ID,
        Description="Automated Snapshot by Lambda"
    )

    snapshot_id = snapshot["SnapshotId"]

    ec2.create_tags(
        Resources=[snapshot_id],
        Tags=[
            {"Key": "CreatedBy", "Value": "Lambda-Backup"}
        ]
    )

    print(f"Created Snapshot: {snapshot_id}")

    response = ec2.describe_snapshots(
        OwnerIds=["self"],
        Filters=[
            {
                "Name": "tag:CreatedBy",
                "Values": ["Lambda-Backup"]
            }
        ]
    )

    now = datetime.now(timezone.utc)

    deleted = []

    for snap in response["Snapshots"]:
        age = now - snap["StartTime"]

        if age > RETENTION:
            ec2.delete_snapshot(
                SnapshotId=snap["SnapshotId"]
            )

            print(f"Deleted Snapshot: {snap['SnapshotId']}")
            deleted.append(snap["SnapshotId"])

    return {
        "CreatedSnapshot": snapshot_id,
        "DeletedSnapshots": deleted
    }