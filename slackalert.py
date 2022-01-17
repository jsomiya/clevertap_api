import requests

def sendSlackMessage(message):
    payload = '{"text":"%s"}' % message
    response = requests.post('https://hooks.slack.com/services/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', data=payload)
    print(response.status_code)