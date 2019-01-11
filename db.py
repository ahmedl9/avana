import mysql.connector


cnx = mysql.connector.connect(host='work.cygvgrmbybb5.us-east-2.rds.amazonaws.com',
                        user='user',
                        password='password',
                        database='mydb')

cur = cnx.cursor(dictionary=True)

def printEntries():
    cur.execute('select * from leaderBoard')

    print(cur.fetchall())

def addEntry(name, credit_score, balance, happiness):
    cur.execute('INSERT INTO leaderBoard VALUES(null, %s, %s, %s, %s)', (name, credit_score, balance, happiness))

    cnx.commit()


def getEntries():
    cur.execute('SELECT * FROM leaderBoard ORDER BY idLeaderboard DESC LIMIT 0,3 ')
    return cur.fetchall()

