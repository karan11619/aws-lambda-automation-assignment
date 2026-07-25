import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):

    print("Received Event:", event)

    instance_id = event['detail']['responseElements']['instancesSet']['items'][0]['instanceId']

    ec2.create_tags(
        Resources=[instance_id],
        Tags=[
            {
                'Key': 'Environment',
                'Value': 'Development'
            },
            {
                'Key': 'Owner',
                'Value': 'Prabakaran'
            },
            {
                'Key': 'Project',
                'Value': 'AWS Automation'
            }
        ]
    )

    return {
        'statusCode': 200,
        'body': f'Tagging completed for {instance_id}'
    }