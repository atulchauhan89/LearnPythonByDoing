import sqlite3

conn = sqlite3.connect("employee.db")

c = conn.cursor()
# Select disctint rows from the database 
for row in c.execute("SELECT DISTINCT * FROM employees"):
    print(row)
