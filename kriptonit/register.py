import pymysql


username="byceran"
password=1998-949
binaceapikey = "6zjM09CCUZkZzMhgNHTMaC7ke9UG3S4X4802rGTrFQr0mRxxBC4I0IV5ImKFjgrd"
apisecretkey = 'QB9dv7Lw3fXCQQVJbgqpHL6Dv8UX9bvG1GXJBApOOkkcJUDEWpCu1zVPvAzuLb4C'

conn = pymysql.connect(host='kriptonitbot.mysql.pythonanywhere-services.com',
                            user='kriptonitbot',
                            password='1998-949',
                            db='users',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()
sql = """insert into `users` (username,passwords,binaceapikey,apisecretkey)
         values (%s, %s, %s, %s) 
    """
cur.execute(sql,(username,password,binaceapikey,apisecretkey))
conn.commit()