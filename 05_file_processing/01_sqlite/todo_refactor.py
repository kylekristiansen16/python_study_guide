
import sqlite3

class Todo:
    def __init__(self):
        self.conn = sqlite3.connect('todo_refactor.db')  # initialize connection in init
        self.c = self.conn.cursor()  # set up the cursor as a class attribute
        self.create_task_table()  # call the db table creation method
        
    def create_task_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                     id INTEGER PRIMARY KEY,
                     name TEXT NOT NULL,
                     priority INTEGER NOT NULL
                     );''')
    
    def add_task(self):
        name = input('Enter task name: ')
        priority = int(input('Enter priority: '))
        
        self.c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', (name, priority))
        self.conn.commit()

app = Todo()
app.add_task()
