
q_template = ["s01","s02","s03","s04","s05"]
q_query = ["select * from querylist where template_id = :val","select * from tbl_user where user_phone = :val","select * from orders where user_phone = :val","select * from products where user_phone = :val","select * from querylist where template_id = :val",]

query_dict=dict(zip(q_template,q_query))