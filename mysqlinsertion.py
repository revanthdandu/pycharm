import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root123",
  database="students"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE sample (Name VARCHAR(255), Id int)")
