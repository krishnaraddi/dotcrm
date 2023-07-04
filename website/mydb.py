import mysql.connector

database=mysql.connector.connect(
    host='localhost',
    user='dbadmin',
    passwd='moser@123'

)

#prepare cursor object 

cursonObject=database.cursor()

cursonObject.execute('CREATE DATABASE kkdbcrm')

print("ALL DONE!!")