import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root123",
  database="students"
)
mycursor = mydb.cursor()
mycursor.execute("insert into sample(Name,Id) values('reshma',99)")
mydb.commit()