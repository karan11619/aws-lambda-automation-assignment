import boto3
from datetime import date, timedelta

ce = boto3.client('ce')
sns = boto3.client('sns')

SNS_TOPIC_ARN = "YOUR_SNS_TOPIC_ARN"

THRESHOLD = 1.0  # USD


def lambda_handler(event, context):

    today = date.today()
    yesterday = today - timedelta(days=1)

    response = ce.get_cost_and_usage(
        TimePeriod={
            'Start': yesterday.strftime('%Y-%m-%d'),
            'End': today.strftime('%Y-%m-%d')
        },
        Granularity='DAILY',
        Metrics=['UnblendedCost']
    )

    amount = float(
        response['ResultsByTime'][0]['Total']['UnblendedCost']['Amount']
    )

    print("Current Cost:", amount)

    if amount > THRESHOLD:

        message = f"""
AWS Daily Cost Alert

Current Cost: ${amount}

Threshold: ${THRESHOLD}
"""

        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="AWS Daily Cost Alert",
            Message=message
        )

    return {
        "statusCode": 200,
        "Cost": amount
    }