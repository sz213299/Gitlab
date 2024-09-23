import pymysql

import requests

conn = pymysql.connect(host='localhost', user='root', password='root', db='pc', charset='utf8', port=3306)
cursor = conn.cursor()
sql = "select * from ds"

res=cursor.execute(sql)

for i  in cursor.fetchall():
    print(i)
cursor.close()
conn.commit()
conn.close()
