import mysql.connector

mydb = mysql.connector.connect(
    host="AntonR.mysql.pythonanywhere-services.com",
    user="AntonR",
    password="6896180An!"
)


mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
