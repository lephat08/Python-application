import MySQLdb
#Tao DATABASE PYTHON CODE                  
data = MySQLdb.connect("localhost","root","")

cursor = data.cursor()
sql ='CREATE DATABASE demodb'
try:
      cursor.execute(sql)
      print 'tao thanh cong!'
except TypeError as e:
      print (e)
      data.rollback()
data.close()
