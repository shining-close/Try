import sqlite3 

with sqlite3.connect("company.db") as db:
    cursor=db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS students(
               id integer PRIMARY KEY, 
               name text NOT NULL, 
               class text NOT NULL, 
               grade integer);""")


cursor.execute("""INSERT INTO students(id,name, class,grade) VALUES (1,"Mary","Python","67")""")

db.commit() 

newID = input ("Enter ID number: ")

newName = input("Enter name: ")

newClass = input("Enter class: ")

newGrade = input("Enter grade: ")

cursor.execute("""INSERT INTO students(id, name, class, grade) 

  VALUES(?, ?, ?, ?)""", (newID, newName, newClass, newGrade)) 

db.commit() 

cursor.execute("SELECT * FROM students")

print(cursor.fetchall() )

db.close()