import boto3

sns_client = boto3.client('sns')

def send_sns_notification(topic_arn, message, subject):
    response = sns_client.publish(
        TopicArn=topic_arn,
        Message=message,
        Subject=subject
    )
    return response
