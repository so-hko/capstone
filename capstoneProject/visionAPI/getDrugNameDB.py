import pymysql

conn = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = 'wlgP123$%^',
        db='capstone_db',
        charset = 'utf8'
)

def getDrugNameDB():
    try:
        cur = conn.cursor()
        cur.execute('select name from blog_medicine')
        return cur.fetchall()
    
    finally:
        cur.close()
        conn.close()
