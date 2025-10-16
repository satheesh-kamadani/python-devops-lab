"""Lambda function to delete unused S3 buckets not linked to any EC2 instances."""
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')

    try:
        # List all S3 buckets in the account
        buckets_response = s3.list_buckets()
        all_buckets = [bucket['Name'] for bucket in buckets_response['Buckets']]

        ec2 = boto3.client('ec2')
        
        # Get all running and stopped instances
        instances_response = ec2.describe_instances(
            Filters=[{'Name': 'instance-state-name', 'Values': ['running', 'stopped']}]
        )
        
        # Collect all bucket names that might be referenced by instances (if tagging or naming pattern applies)
        # NOTE: EC2 instances do not "attach" to S3 buckets directly, but you might check tags or configurations
        associated_buckets = set()
        for reservation in instances_response['Reservations']:
            for instance in reservation['Instances']:
                for tag in instance.get('Tags', []):
                    if 's3' in tag['Key'].lower() or 'bucket' in tag['Key'].lower():
                        associated_buckets.add(tag['Value'])

        # Identify buckets that are not associated with any instance
        unused_buckets = [b for b in all_buckets if b not in associated_buckets]

        # Delete unused buckets
        for bucket_name in unused_buckets:
            # First delete all objects inside the bucket before deleting it
            try:
                s3_resource = boto3.resource('s3')
                bucket = s3_resource.Bucket(bucket_name)
                bucket.objects.all().delete()
                s3.delete_bucket(Bucket=bucket_name)
                print(f"Deleted unused bucket: {bucket_name}")
            except Exception as e:
                print(f"Failed to delete bucket {bucket_name}: {str(e)}")

        if not unused_buckets:
            print("No unused S3 buckets found.")

    except Exception as e:
        print(f"Error while processing: {str(e)}")