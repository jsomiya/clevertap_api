from sqlalchemy import create_engine

# POSTGRES = {
#     'user': 'cm',
#     'pw': 'cm',
#     'host': '13.232.92.91',  # 'cmdb-rr2.cbo3ijdmzhje.ap-south-1.rds.amazonaws.com',
#     'port': '5432',
#     'db' : 'cmdb'
# }


engine = create_engine('postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES)
#engine = create_engine('postgresql://postgres:password@localhost/test')
connection = engine.connect()
