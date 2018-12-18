import MySQLdb
import datetime
import db_function
currentDT = datetime.datetime.now()
print (str(currentDT))
db = MySQLdb.connect("localhost","root","","sinhviendb")
print 'Connected to Mysql database'
cursor = db.cursor()
print "------------------------------------------------"
id = raw_input("Nhap ID student: ")
print "----Chinh sua thong tin sinh vien----"
name = raw_input("Ho & ten: ")
birth = raw_input("Ngay sinh: ")
mark = raw_input("Diem: ")
add = raw_input("Dia chi: ")
db_function.update(id,name,birth,mark,add)