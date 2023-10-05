#import mysql.connector
from mysql-connector-python

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="jota#1970"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")
