import sqlite3
#connect to sqlite
connection = sqlite3.connect("student.db")
#make a cursor
cursor = connection.cursor()

#create table query
create_table = """ create table Student (Name varchar(25), 
Class varchar(25), Section varchar(25), Marks int)"""

cursor.execute(create_table)

#insert data into table
cursor.execute('''Insert into Student values('Shubham', 'Data Science','A',20)''')
cursor.execute('''Insert into Student values('Sid', 'Data Analytics','B',12)''')
cursor.execute('''Insert into Student values('Ankita', 'ETNT','A',15)''')

#read data
data = cursor.execute('''Select * from Student''')

for i in data:
    print(i)

#close connection
connection.commit()
connection.close