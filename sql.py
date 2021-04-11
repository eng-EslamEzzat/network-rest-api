import sqlite3
con = sqlite3.connect('db.sqlite3')
cur = con.cursor()
for r in cur.execute('SELECT * FROM network_Post'):
    print(r)
