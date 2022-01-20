import json, requests, sys
from sqlalchemy import text
from flask import Flask, request

from querydict import query_dict
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
        list_of_template_id = []
        for q in query_dict:
            list_of_template_id.append(q["template_id"])
        if template_id not in list_of_template_id:
            sendSlackMessage("The webhook sent invalid template_id")
        else:
            for q in query_dict:
                if q["template_id"]==template_id:
                    sql = q["query_text"]
        for i in range(0,no_of_users):
            sql_query = text(sql)
            result = connection.execute(sql_query, val = numbers[i])
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
    except Exception:
        sendSlackMessage(sys.exc_info()[0])
