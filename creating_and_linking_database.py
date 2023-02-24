import sqlite3



try:
  connect = sqlite3.connect("database.db")
  print("connected")
except sqlite3.Error as error:
  print("not connected",error)
finally:
  if connect:
    connect.close()
    print("connection closed")

