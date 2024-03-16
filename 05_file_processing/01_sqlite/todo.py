

import sqlite3

# conn2 = sqlite3.connect() # NOT ALLOWED
conn = sqlite3.connect('todo.db')
c = conn.cursor()  # connection method cursor - object that is allowed to execute SQL queries on a database

c.execute('DROP TABLE IF EXISTS tasks')  # drop a table if it exists

### CREATE TABLE ###

# create a table
c.execute('''CREATE TABLE IF NOT EXISTS tasks (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
priority INTEGER NOT NULL
);''')

# insert a row omitting the id
# c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', ('My first task', 1))
c.execute('INSERT INTO tasks (name, priority) VALUES (?,?), (?, ?)', ['My first task', 1, 'second task', 2])  # ? - placeholder for a value, to protect against SQL injection

# OR

# us the executemany method to insert multiple rows
tasks = [
    ('My fourth task', 4),
    ('5th task', 5),
    ('third tAsK', 3),
]
c.executemany('INSERT INTO tasks (name, priority) VALUES (?,?)', tasks)

# we need to call the commit method to confirm the changes
conn.commit()  # none of the queries will be executed until commit is called, for C U D operations (not read)

### READ DATA ###

print("using read iterator:")
# SWITCH FOCUS TO READING FROM DATABASE
for row in c.execute('SELECT * FROM tasks'):  # cursor object is treated as an iterator
    print(row)  # each row is a tuple, with index access (not able to use column name access)

# OR 

print("using fetchall method:")
c.execute('SELECT * FROM tasks')
rows = c.fetchall()  # fetchall method gets all records and returns a list of tuples
print(rows)

# fetchall is less efficient than iterating over the cursor object bc all rows are stored in memory

# OR

print("using fetchone method:")
c.execute('SELECT * FROM tasks')
row = c.fetchone()  # fetchone method gets the next row and returns a tuple
print(row)

### UPDATE DATA ###
# UPDATE table_name
# SET column1 = value1, column2 = value2, column3 = value3, …, columnN = valueN
# WHERE condition;

c.execute('UPDATE tasks SET priority = ? WHERE id = ?', (20, 1))
c.commit()

### DELETE DATA ###
# DELETE FROM table_name WHERE condition;

c.execute('DELETE FROM tasks WHERE id = ?', (3,))
c.commit()

# close the connection
conn.close()