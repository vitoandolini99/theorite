import os
import mysql.connector
import json
from vendor.rp import resource_path

conf_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'conf', 'db.json')
d = str(conf_path)[-12:]
with open(resource_path(d).replace('''\src\db''', '')) as cf:
    db = json.loads(cf.read())
"""
conf/db.json values
"""
mydb = mysql.connector.connect(
    host=db["host"],
    port=db["port"],
    user=db["user"],
    password=db["password"],
    database=db["database"]
)
mycursor = mydb.cursor()
