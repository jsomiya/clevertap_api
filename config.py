import os

url = "http://citymall.live"

slack_token = os.environ.get('SLACK_TOKEN')
x_ct_key = os.environ.get('HEADER_TOKEN')

headers = {
        'x-ct-key': x_ct_key,
        'Content-Type': 'application/json',
        }

