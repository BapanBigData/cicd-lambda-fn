import json
import requests


def lambda_handler(event, context):

    print("Event Data -> ", event)
    response = requests.get("https://www.google.com/")
    print(response.text)
    
    print("Demo Completed !!!")

    return {"statusCode": 200, "body": json.dumps("Hello from Lambda!")}
