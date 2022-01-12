from flask_sqlalchemy import SQLAlchemy

POSTGRES = {
    'user': 'cm',
    'pw': 'cm',
    'host': '13.232.92.91',  # 'cmdb-rr2.cbo3ijdmzhje.ap-south-1.rds.amazonaws.com',
    'port': '5432',
    'db' : 'cmdb'
}

db = SQLAlchemy()