
""" 

Our TODO application requires you to add a little security and display the data saved in the database. Your task is to implement the following functionalities:

Create a find_task method, which takes the task name as its argument. The method should return the record found or None otherwise.
Block the ability to enter an empty task (the name cannot be an empty string).
Block the ability to enter a task priority less than 1.
Use the find_task method to block the ability to enter a task with the same name.
Create a method called show_tasks, responsible for displaying all tasks saved in the database.

Example input:
Enter task name: My first task
Enter priority: 1

Example output:
(1, 'My first task', 1)

Example input:
Enter task name: My second task
Enter priority: 2

Example output:
(1, 'My first task', 1)
(2, 'My second task', 2)

Example input:
Enter task name: My first task
Enter priority: 1

Example output:
(1, 'My first task', 1)
(2, 'My second task', 2)
"""

import sqlite3

class Todo:
    def __init__(self):
        self.conn = sqlite3.connect('lab_01.db')
        self.c = self.conn.cursor()
        self.create_task_table()
        self.initialize_task_table()
        
    def create_task_table(self):
        self.c.execute('DROP TABLE IF EXISTS tasks')
        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                     id INTEGER PRIMARY KEY,
                     name TEXT NOT NULL,
                     priority INTEGER NOT NULL
                     );''')
        self.conn.commit()
        
    def initialize_task_table(self):
        raw_data = [
            (1, "first", 1),
            (2, "2nd", 2),
            (3, "my third task", 3),
        ]
        self.c.executemany('INSERT INTO tasks (id, name, priority) VALUES (?, ?, ?)', raw_data)
        self.conn.commit()
    
    def add_task(self):
        name = input('Enter task name: ')
        while (not name or len(name) == 0) or self.find_task(name):
            name = input('Enter a vald task name, string with len > 0 not existing in db: ')
        priority = int(input('Enter priority (int): '))
        while priority < 1:
            priority = int(input('Enter a valid priority, int > 1: '))
        
        self.c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', (name, priority))
        self.conn.commit()
    
    def find_task(self, task_name):
        self.c.execute(f'SELECT * FROM tasks WHERE name = "{task_name}"')
        row = self.c.fetchone()
        if row:
            return row
        else:
            return None
        
    def show_tasks(self):
        for row in self.c.execute('SELECT name FROM tasks'):
            print(row[0])


app = Todo()
# app.add_task()
print(app.find_task("first"))
    
app.show_tasks()

app.add_task()

