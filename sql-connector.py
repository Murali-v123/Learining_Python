import mysql.connector

db = mysql.connector.connect(
    host="localhost", 
    user="root", 
    password="root"
    )
cur = db.cursor()

cur.execute("show database")
rec=cur.fetchone()

cur.execute("databases is",rec)

# for i in cur:
#     print(i)
