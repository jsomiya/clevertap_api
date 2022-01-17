import json, requests, sys
from sqlalchemy import text
from flask import Flask, request

from querydict import q_template, query_dict
from slackalert import sendSlackMessage
from db import connection
from config import url


app = Flask(__name__)


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
        sendSlackMessage(sys.exc_info()[0], err)
