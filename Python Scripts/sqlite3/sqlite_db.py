import sqlite3
#Create a database connection or connect to existing one
conn = sqlite3.connect('employee.db')

#create a cursor object to perform sql ops
c = conn.cursor()

# c.execute('''CREATE TABLE employees (
#           first TEXT,
#           last TEXT,
#           pay INTEGER
#           )''')

# c.execute("insert into employees values ('mary','karmakar',50000)")

c.execute("select * from employees")
print(c.fetchall())

# commit the transaction
conn.commit()

#close the connection
conn.close()