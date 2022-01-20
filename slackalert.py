import requests
from config import slack_token

def sendSlackMessage(message):
    payload = '{"text":"%s"}' % message
    response = requests.post(slack_token, data=payload)
    print(response.status_code)
