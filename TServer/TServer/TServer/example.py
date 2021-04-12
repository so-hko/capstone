import pymysql

conn=pymysql.connect(host='localhost',user='root',password='1234',db='blog',charset='utf8')

curs=conn.cursor()

sql="select * from A"
curs.execute(sql)

data=curs.fetchall()
print(data[0])