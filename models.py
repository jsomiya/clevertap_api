from app import db

class Querylist(db.Model):
    __tablename__ = 'querylist'
    template_id = db.Column(db.VARCHAR(50),primary_key = True)
    query_text = db.Column(db.VARCHAR(2048), nullable = False)
    is_active = db.Column(db.BOOLEAN, default = True)


def __init__(self,template_id,query_text,is_active):
    self.template_id = template_id
    self.query_text = query_text
    self.is_active = is_active

