import json


def lambda_handler(event: str, context: str) -> dict:
    if event is None or context is None:
        return {
            "statusCode": 300,
            "body": json.dumps({"message": "No World!"})
        }

    if len(event) < len(context):
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Hello World!"})
        }

    return {
        "statusCode": 400,
        "body": json.dumps({"message": "Bad World!"})
    }