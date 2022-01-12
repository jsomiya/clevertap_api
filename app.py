import json
import requests
from flask import Flask, request

from db import POSTGRES, db
from models import Querylist

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/test'
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://cm:cm@13.232.92.91:5432/cmdb"

db.init_app(app)

@app.route("/test")
def test():
    return "done"

@app.route('/postqueryresponse', methods=['POST'])
def getquery():
    url = "citymall.dev"
    request_data = request.get_json()
    numbers = request_data['numbers']
    no_of_users = len(numbers)
    template_id = request_data['template_id']
    query_data = Querylist.query.get_or_404(template_id)
    sql = query_data.query_text
    for i in range(0,no_of_users):
        result = db.session.execute(sql, {'val':numbers[i]})
        res = result.one_or_none()
        parameters = list(res)
        data = {
            "numbers": numbers,
            "template_id": template_id,
            "parameters":parameters
        }
        response  = requests.post('http://'+url+'//api/ct/webhook',data)
    return response.status_code


if __name__ == '__main__':
    app.run(debug=True)
    


