import os
from sqlalchemy import create_engine

POSTGRES = {
    'user': os.environ.get('DBUSER', 'cm'),
    'pw': os.environ.get('DBPASS', 'cm'),
    'host': os.environ.get('DBURL', '13.232.92.91'), 
    'port': os.environ.get('PORT', '5432'), 
    'db' : os.environ.get('DB', 'cmdb'),
}


engine = create_engine('postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES)
# engine = create_engine('postgresql://postgres:password@localhost/test')
connection = engine.connect()
