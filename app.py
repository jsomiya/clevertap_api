from http.client import REQUESTED_RANGE_NOT_SATISFIABLE
import json, requests, sys
from sre_constants import SUCCESS
from sqlalchemy import text
from flask import Flask, request

from querydict import query_dict
from slackalert import sendSlackMessage
from db import connection
from config import url


app = Flask(__name__)

@app.route('/ct/event/message', methods=['POST'])
def sendparams():
    try:
        request_data = request.get_json()
        numbers = request_data['numbers']
        no_of_users = len(numbers)
        template_id = request_data['template_id']
        params=[]
        for key,value in request_data.items():
            if key!="numbers" and key!="template_id":
                params.append(value)
        for i in range(0,no_of_users):
            data = {
            "numbers": [numbers[i]],
            "template_id": template_id,
            "parameters":params
            }
            headers = {
                'x-ct-key': 'AkbMw8wTBL/tq/KYPuvOPsyIpz3xP+h2lZRsSECvc24=',
                'Content-Type': 'application/json',
            }
            response  = requests.post(url+'/api/ct/webhook', headers=headers, data=json.dumps(data))
    except:
        return 'success' , 200


@app.route('/ct/qeury/message', methods=['POST'])
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
                params= []
                params.append(list(res))
                data = {
                    "numbers": [numbers[i]],
                    "template_id": template_id,
                    "parameters":params[0]
                }
                headers = {
                'x-ct-key': 'AkbMw8wTBL/tq/KYPuvOPsyIpz3xP+h2lZRsSECvc24=',
                'Content-Type': 'application/json',
                }
                response  = requests.post(url+'/api/ct/webhook', headers=headers, data=json.dumps(data))
                return 'OK'
            except:
                sendSlackMessage("The query returned none or too many data at once")
    except Exception:
        return sendSlackMessage(sys.argv()[0])
