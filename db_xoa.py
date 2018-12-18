import MySQLdb
import datetime
import db_function
currentDT = datetime.datetime.now()
print (str(currentDT))
db = MySQLdb.connect("localhost","root","","sinhviendb")
print 'Connected to Mysql database'
cursor = db.cursor()
print "-------------------------------------------------"
er = raw_input("Nhap ma sinh vien muon xoa: ")
db_function.xoa(er)