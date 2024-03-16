
""" 
dbms - database management system - responsible for:
- creating a database structure;
- inserting, updating, deleting, and searching data;
- ensuring data security;
- transaction management;
- ensuring concurrent access to data for many users;
- enabling data exchange with other database systems.

most popular dbms:
- free
    - mysql
    - postgresql
    - sqlite
- paid
    - oracle
    - microsoft sql server
    - ibm db2

sqlite - focus of this section
- C library which allows the user to read and write data directly to a file. all database is stored to the file
- doesn't require a separate server process to be running in order to communicate with the database
- supports transactions with the ability to roll back any changes if something goes wrong

sqlite3 - python module for working with sqlite databases, compliant with the Python Database API Specification v2.0 (PEP 249)
- https://www.python.org/dev/peps/pep-0249/
- purpose of the DB-API 2.0 specification is to define a common standard for creating modules to work with databases in Python.

there are many versions of SQL (structured query language) implemented over time
- SQL-86, SQL-89, SQL-92, SQL:1999, SQL:2003, SQL:2006, SQL:2008, SQL:2011, SQL:2016, SQL:2019
- sqlite3 implements SQL-92 standard
- https://www.sqlite.org/lang.html


"""

import sqlite3
# help(sqlite3)

conn = sqlite3.connect('hello.db')  
# pass ':memory:' for in-memory (RAM) database that is deleted as soon as the connection is closed
# pass a different path to create a database file in a specific location
# if a db file exists, it will be used, otherwise it will be created
