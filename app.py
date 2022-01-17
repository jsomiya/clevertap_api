import json, requests
from re import template
from flask import Flask, request

from sqlalchemy import text
from querydict import q_template, query_dict
from config import url
from db import connection

app = Flask(__name__)

#send alerts on slack
def sendSlackMessage(message):
    payload = '{"text":"%s"}' % message
    response = requests.post('https://hooks.slack.com/services/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', data=payload)
    print(response.status_code)


@app.route('/postqueryresponse', methods=['POST'])
def getquery():
    try:
        request_data = request.get_json()
        numbers = request_data['numbers']
        template_id = request_data['template_id']
        no_of_users = len(numbers)
        if template_id in q_template:
            for key,value in query_dict.items():
                if key==template_id:
                    sql = value
        else:
            sendSlackMessage("The webhook sent invalid template_id")
        for i in range(0,no_of_users):
            sql_query = text(sql)
            result = connection.execute(sql_query, val = template_id)
            try:
                res = result.one()
            except:
                sendSlackMessage("The query returned none or too many data at once")
            parameters = list(res)
            data = {
                "numbers": [numbers[i]],
                "template_id": template_id,
                "parameters":parameters
                }
            response  = requests.post(url+'//api/ct/webhook',data=json.dumps(data))
            return response.status_code  
    except Exception as err:
        sendSlackMessage(err)
