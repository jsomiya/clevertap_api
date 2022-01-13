import json, requests
from flask import Flask, request

from sqlalchemy import text
from querydict import query_dict
from config import url
from db import connection

app = Flask(__name__)


@app.route('/postqueryresponse', methods=['POST'])
def getquery():
    try:
        request_data = request.get_json()
        numbers = request_data['numbers']
        no_of_users = len(numbers)
        template_id = request_data['template_id']
        for q in query_dict:
            if q["template_id"]==template_id:
                sql = q["query_text"]
        for i in range(0,no_of_users):
            sql_query = text(sql)
            result = connection.execute(sql_query, val = numbers[i])
            res = result.one_or_none()
            parameters = list(res)
            data = {
                "numbers": numbers,
                "template_id": template_id,
                "parameters":parameters
            }
            response  = requests.post(url+'//api/ct/webhook',data=json.dumps(data))
        return response.status_code
    except:
        return 'success', 200

        

