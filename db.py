import mysql.connector


cnx = mysql.connector.connect(host='work.cygvgrmbybb5.us-east-2.rds.amazonaws.com',
                        user='user',
                        password='password',
                        database='mydb')

cur = cnx.cursor(dictionary=True)

cur.execute('select * from leaderBoard')

print(cur.fetchall())