import json
import boto3

# Initialize a DynamoDB client
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('visitorsCounterIAC')  # Your DynamoDB table name

def lambda_handler(event, context):
    # Attempt to update the visitor count
    try:
        response = table.update_item(
            Key={'id': 'visitorCount'},
            UpdateExpression='ADD #count :increment',
            ExpressionAttributeNames={'#count': 'count'},
            ExpressionAttributeValues={':increment': 1},
            ReturnValues='UPDATED_NEW'
        )
        # Prepare the response with the updated count
        responseBody = {
            'count': int(response['Attributes']['count'])
        }
        return {
            'statusCode': 200,
            'body': json.dumps(responseBody),
            'headers': {
                'Content-Type': 'application/json'
            },
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Could not update visitor count'}),
            'headers': {
                'Content-Type': 'application/json'
            },
        }

