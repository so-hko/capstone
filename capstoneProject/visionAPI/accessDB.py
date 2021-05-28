import pymysql

conn = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = 'wlgP123$%^',
        db='capstone_db',
        charset = 'utf8'
)

# To get Drug Name from Database
def getDrugNameDB():
    try:
        cur = conn.cursor()
        cur.execute('select name from blog_otcinfo')
        return cur.fetchall()
    
    finally:
        cur.close()
        #conn.close()

# To get Drug Information from Database
def getDrugInformation(drugname):
    try:
        cur = conn.cursor()
        cur.execute('select * from blog_otcinfo where `name` = %s',[drugname])
        return cur.fetchall()

    finally:
        cur.close()
        #conn.close()
