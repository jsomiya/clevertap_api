
query_dict = [
    {
    "template_id" : "s01",
    "query_text" : "select * from querylist where order_id = :val"
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
    "template_id" : "cl_delivery_marking",
    "query_text" : "select user_name from tbl_user where user_phone = :val"
    },
    {
    "template_id" : "cx_first_time_order",
    "query_text" : "select * from \
    (select address_name as var1,\
    'pul' as var2,\
    order_id as var3, \
    address_address1 as var5, \
    'gurgaon' as var6, \
        'var7' as var7,\
    'www.google.com' as var8, \
    address_phone_number as phone_number \
    from orders where order_id='362843' \
    )y where phone_number = :val" }
]