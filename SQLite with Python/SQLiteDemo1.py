import sqlite3
# no need to pip SQLite as it is included with standered library of Python3
# It provides a SQL interface compliant with the DB-API 2.0 specification described by PEP 249.
# Made a connection object conn and Data will store in "employee.db" file.
# If you want to create a database in RAM then use ":memory:"
# If "employee.db" database is not available and you are trying to connect hen sqlite will create the database for you.

conn = sqlite3.connect("employee.db")

# Now create cursor object and then you can perform execute() method to perform SQL commands
c = conn.cursor()
 
# Created a table
c.execute('''CREATE TABLE employees(firstName text,lastName text, pay integer ) ''' )

# Insert a row with data
c.execute("INSERT INTO employees VALUES ('Tom','Hardy','30000')")

# Get first row from the employees table
c.execute("SELECT * FROM employees")
print(c.fetchone())

# Always save the changes with commit command. If you will not commit then after closing the connection data will lost.
conn.commit()

# Close the connection
conn.close()


# *Note* usually your SQL operations will need to use values from Python variables. You shouldn’t assemble your query using Python’s string operations because doing so is insecure; it makes your program vulnerable to an SQL injection attack 
