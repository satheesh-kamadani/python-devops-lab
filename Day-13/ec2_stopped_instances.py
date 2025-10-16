"""Lambda function to terminate stopped EC2 instances."""
import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    try:
        # Get all the stopped ec2 instance ID's
        instances_response = ec2.describe_instances(
        Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}]
    )
        stopped_instance_ids = [
            instance['InstanceId']
            for reservation in instances_response['Reservations']
            for instance in reservation['Instances']
        ]

        # Terminate if any stopped instances
        if stopped_instance_ids:
            ec2.terminate_instances(InstanceIds=stopped_instance_ids)
            print(f'Deleted stopped instances: {stopped_instance_ids}')
        else:
            print(f'No stopped instances found.')
    except Exception as e:
        print(f'Error while processing {str(e)}')
            
    




