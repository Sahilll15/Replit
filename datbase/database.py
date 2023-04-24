import mysql.connector

db = mysql.connector.connect(host="localhost",
                             username="root",
                             passwd="",
                             database='employe')

print(db)

cursor = db.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS employe")

cursor.execute("USE  employe")

employee_create = """CREATE TABLE IF NOT EXISTS emp_details(
NAME VARCHAR(100) NOT NULL,
AGE VARCHAR(100) NOT NULL
                 )"""
cursor.execute(employee_create)

employee_INSERT = "INSERT INTO  emp_details(NAME,AGE) VALUES (%s,%s) "
val = ('chikitsa', 19)
try:
  cursor.execute(employee_INSERT, val)
  db.commit()
  print("SUCCESS")
except Exception as e:
  print("Error occurred: ", e)
  db.rollback()

employee_DELETE = "DELETE FROM emp_details WHERE NAME='%s'"
employee_name = "sahil"

try:
  cursor.execute(employee_DELETE % employee_name)
  db.commit()
  print("SUCCESS")
except Exception as e:
  print("ERROR OCCURED: ", e)
  db.rollback()

employee_UPDATE = "UPDATE emp_details SET AGE=%s WHERE NAME=%s"
emp_update = (20, 'chikitsa')

try:
  cursor.execute(employee_UPDATE, emp_update)
  db.commit()
  print("SUCCESS")
except Exception as e:
  print("ERROR OCCURED ", e)
  db.rollback()

db.close()
