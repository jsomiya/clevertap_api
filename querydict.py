
query_dict = [
    {
    "template_id" : "s01",
    "query_text" : "select * from querylist where template_id = :val"
    },
    {
    "template_id" : "s02",
    "query_text" : "select * from tbl_user where user_phone = :val"
    },
    {
    "template_id" : "s03",
    "query_text" : "select user_name from tbl_user where user_phone = :val"
    },
    {
    "template_id" : "s04",
    "query_text" : "select * from products where user_phone = :val"
    },
    {
    "template_id" : "s05",
    "query_text" : "select * from categories where user_phone = :val"
    }
]