
""" 
The application is almost ready. Let's add the missing functionalities to it:

Create a method called change_priority, responsible for updating task priority. 
    The method should get the id of the task from the user and its new priority (greater than or equal to 1).
Create a method called delete_task, responsible for deleting single tasks. The method should get the task id from the user.
Implement a simple menu consisting of the following options:

1. Show Tasks 
2. Add Task 
3. Change Priority 
4. Delete Task
5. Exit
where:

Show Tasks (calls the show_tasks method)
Add Task (calls the add_task method)
Change Priority (calls the change_priority method)
Delete Task (calls the delete_task method)
Exit (interrupts program execution)
The program should obtain one of these options from the user, and then call the appropriate method of the TODO object. 
Choosing option 5 must terminate the program. A menu should be displayed in an infinite loop so that the user can choose an option multiple times.

"""

import sqlite3

class Todo:
    def __init__(self):
        self.conn = sqlite3.connect('lab_02.db')
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
    
    def menu(self):
        print("""Menu:\n\t1. Show Tasks\n\t2. Add Task\n\t3. Change Priority\n\t4. Delete Task\n\t5. Exit""")
        action = -1
        while action not in ['1', '2', '3', '4', '5']:
            action = input('Enter desired db action: ')
            
        if action == '1':
            self.show_tasks()
        elif action == '2':
            self.add_task()
        elif action == '3':
            self.change_priority()
        elif action == '4':
            self.delete_task()
        else:  # action == 5
            print('closing db connection')
            self.conn.close()
            return
        
        self.menu()
    
    def request_name(self, existing=False):
        name = input('Enter task name: ')
        while not name or len(name) == 0 or (self.find_task(name) and not existing):
            name = input('Enter a vald task name, string with len > 0 not existing in db: ')
        return name.strip()
        
    def request_priority(self):
        p = int(input('Enter priority (int >= 1): '))
        while p < 1:
            p = int(input('Enter a valid priority (int >= 1) : '))
        return p
    
    def find_task(self, task_name=None):
        if not task_name:
            task_name = self.request_name()
        self.c.execute(f'SELECT * FROM tasks WHERE name = "{task_name}"')
        row = self.c.fetchone()
        if row:
            return row
        else:
            return None
    
    def show_tasks(self):
        print("Task Names:")
        for row in self.c.execute('SELECT name FROM tasks'):
            print(f"\t{row[0]}")
        
    def add_task(self):
        name = self.request_name()
        priority = self.request_priority()
        
        self.c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', (name, priority))
        self.conn.commit()
    
    def change_priority(self, task_name=None, priority=None):
        if not task_name:
            task_name = self.request_name(existing=True)
        if not priority:
            priority = self.request_priority()
          
        if self.find_task(task_name):
            self.c.execute('''UPDATE tasks SET priority = ? WHERE name = ?''', (priority, task_name))
            self.conn.commit()
        else:
            print(f'No task called {task_name} in db')
        
    def delete_task(self, task_name=None):
        if not task_name:
            task_name = self.request_name(existing=True)
        
        if self.find_task(task_name):
            self.c.execute(f'DELETE FROM tasks WHERE name = "{task_name}"')
            self.conn.commit()
        else:
            print(f'No task called {task_name} in db')


app = Todo()
# app.add_task()
# print(app.find_task("first"))
# app.show_tasks()

app.menu()

