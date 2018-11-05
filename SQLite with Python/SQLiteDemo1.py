import sqlite3
# no need to pip SQLite as it is included with standered library
# It provides a SQL interface compliant with the DB-API 2.0 specification described by PEP 249.
# Made a connection object conn and Data will store in "employee.db" file.
# If you want to create a database in RAM then use ":memory:"

conn = sqlite3.connect("employee.db")

# Now create cursor object and then you can perform execute() method to perform SQL commands
c = conn.cursor()
 
# Created a table
c.execute('''CREATE TABLE employees(firstName text,lastName text, pay integer ) ''' )

# Insert a row with data
c.execute("INSERT INTO employees VALUES ('Tom','Hardy','30000')")

# Always save the changes with commit command. If you will not commit then after closing the connection data will lost.
conn.commit()

# Close the connection
conn.close()
