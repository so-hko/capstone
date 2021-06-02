import os, sys
from getquery import getq
sys.path.append('/home/ec2-user/capstone/capstoneProject/blog')
import models# Pill, OTCInfo
import pymysql

#Mysql Connection 연결
conn = pymysql.connect(
	host='localhost',
	user='root',
	password='wlgP123$%^',
	db='capstone_db',
	charset='utf8'
	)

cur = conn.cursor()
pillquery = getq()

pillname = 'SELECT name FROM blog_pill WHERE = %s' % pillquery

#pillname = "SELECT name FROM blog_otcinfo"

cur.execute(pillname)

rows=cur.fetchall()
print(rows)

conn.close()

"""
def A():
    try:
        pillquery = getq()
        global cur
        pillname = "SELECT name FROM Pill" + pillquery
        tmp = cur.execute(pillname)
        print(tmp)
        return cur.fetchall()
    finally:
        cur.close()
        
    def B():
        try:
            name = A()
            cur = conn.cursor()
    
            pillname = "SELECT name FROM OTC_Info WHERE `name`= " + name
            cur.execute(pillname)
            return cur.fetchall()
        finally:
            cur.close()


pil.B()

"""


