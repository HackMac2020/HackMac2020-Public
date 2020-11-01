import MySQLdb
import os

db = MySQLdb.connect(
    host=os.environ.get("MYSQL_HOST"),
    user=os.environ.get("MYSQL_USER"),
    passwd=os.environ.get("MYSQL_PASSWORD"),
    db=os.environ.get("MYSQL_DB")
)

cursor = db.cursor()

cursor.execute(
    ''' CREATE TABLE IF NOT EXISTS users (username VARCHAR(100) NOT NULL, password VARCHAR(100) NOT NULL) ''')
print("Created users table")
cursor.execute(''' INSERT INTO users VALUES('45678909', 'Sup3rh4cker') ''')
cursor.execute(''' INSERT INTO users VALUES('98765432', 'Hacky101') ''')

db.commit()

cursor.close()
