'''
练习6–创建一个名为PhoneBook1的SQL数据库，该数据库包含一个称为Names的表，其中包含以下数据：
'''

import sqlite3

# Connect to the database called PhoneBook or create one if there is none
with sqlite3.connect("PhoneBook1.db") as db:
    cursor = db.cursor()

# Create a table called Names with four fields
cursor.execute(""" CREATE TABLE IF NOT EXISTS Names(
    id integer PRIMARY KEY,
    firstname text,
    surname text,
    phonenumber text); """)

    # Insert data into the table
cursor.execute(""" INSERT INTO Names(id,firstname,surname,phonenumber)
    VALUES ("60", "Simon","Pierre","0142678 9056")""")
db.commit()  # Saves the changes

    # Insert data into the table Names
cursor.execute(""" INSERT INTO Names(id, firstname,surname,phonenumber)
    VALUES ("70", "Katarina","Iglesias","0203456 7078")""")
db.commit()  # saves the changes

    # Insert data into a table called Names
cursor.execute(""" INSERT INTO Names(id,firstname,surname,phonenumber)
    VALUES ("30", "Derrick", "Brown", "0122345 8765")""")
db.commit()  # saves the changes

    # Insert data into a table called Names
cursor.execute(""" INSERT INTO Names(id,firstname,surname,phonenumber)
    VALUES ("40", "John", "Smith", "0112653 2312")""")
db.commit()  # saves the changes

    # Insert data into a table called Names
cursor.execute(""" INSERT INTO Names(id,firstname,surname,phonenumber)
    VALUES ("50", "Mark", "Isaac", "0141657 1383")""")
db.commit()  # saves the changes

db.close()  # close the database