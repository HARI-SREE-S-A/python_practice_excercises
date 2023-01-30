import sqlite3

id_n = input("enter thew id number")
name = input("enter your name")
desig = input("enter the designation")




initializing = sqlite3.connect("sample_database.db")

cur = initializing.cursor()


#creating the table in database


tab = """CREATE TABLE IF NOT EXISTS notes(id INTEGER PRIMARYKEY,name TEXT,designation TEXT);'''
cur.execute(tab)



