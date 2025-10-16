"""Lambda function to delete unused (inactive) EKS clusters."""
import boto3

def lambda_handler(event, context):
    eks = boto3.client(eks)

    try:
        # List all eks clusters
        clusters = eks.list_clusters()['clusters']

        if not clusters:
            print("No clusters found")
            return
        
        for cluster_name in clusters:
            # Get cluster details
            cluster_info = eks.describe_cluster(name=cluster_name)['clusters']
            status = cluster_info['status']

            # Delete the cluster if it's inactive or failed
            if status.lower() in ['inactive', 'failed', 'deleting']:
                eks.delete_cluster(name=cluster_name)
                print(f"Deleted ununsed EKS cluster: {cluster_name}")
            else:
                print("EKS cluster {cluster_name} is active. Skipping deletion")
    except Exception as e:
        print(f"Error while processing {str(e)}")
        
            