"""Lambda function to delete unused (stopped) MySQL RDS instances."""

import boto3

def lambda_handler(event, context):
    rds = boto3.client('rds')

    try:
        # Get all RDS instances
        response = rds.describe_db_instances()
        db_instances = response['DBInstances']

        # Filter MySQL instances that are stopped or not available
        unused_instances = [
            db['DBInstanceIdentifier']
            for db in db_instances
            if db['Engine'] == 'mysql' and db['DBInstanceStatus'] != 'available'
        ]

        # Delete unused RDS instances
        if unused_instances:
            for db_id in unused_instances:
                rds.delete_db_instance(
                    DBInstanceIdentifier=db_id,
                    SkipFinalSnapshot=True  # optional, prevents extra cost
                )
                print(f"Deleted unused MySQL RDS instance: {db_id}")
        else:
            print("No unused MySQL RDS instances found.")
    
    except Exception as e:
        print(f"Error while processing: {str(e)}")