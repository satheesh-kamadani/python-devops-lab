import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    # Get all EBS snapshots
    response = ec2.discribe_snapshots(OwnerIds='self')

    # Get all active ec2 instance IDs
    instances_response = ec2.discribe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    active_instance_ids = set()

    for reservation in instances_response['Reservations']:
        for instance in reservation['instances']:
            active_instance_ids.add(instance['InstanceId'])

    # Iterate through each snapshot and delete if it's not attached to any volume or the volume is not attached to a running instance
    for snapshot in response['snapshots']:
        snapshot_id = snapshot['SnapshotId']
        volume_id = snapshot.get['VolumeId']

        if not volume_id:
            # Delete the snapshot if it is not attached to any volume
            ec2.delete_snapshot(SnapshotId=snapshot_id)
            print(f'Deleted EBS snapshot {snapshot_id} as it was not attached to any volume')
        else:
            # Check if the volume still exists
            try:
                volume_response = ec2.describe_volume(VolumeIds=[volume_id])
                if not volume_response['Volume'][0]['Attachments']:
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f'Deleted EBS snapshot {snapshot_id} as it was taken from a volume not attached to any running instance.')
            except ec2.exceptions.ClientError as e:
                if e.response['Error']['code'] == 'InvalidVolume.NotFound':
                    # The volume associated with the snapshot is not found (it might have been deleted)
                    ec2.delete_snapshot(SnapshotId=snapshot_id)
                    print(f'Deleted EBS snapshot {snapshot_id} as its associated volume was not found')







