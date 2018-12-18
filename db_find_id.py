import MySQLdb
import datetime
import db_function
currentDT = datetime.datetime.now()
print (str(currentDT))
db = MySQLdb.connect("localhost","root","","sinhviendb")
print 'Connected to Mysql database'
cursor = db.cursor()
print "\t                                   Tim Kiem Thong Tin Sinh Vien  "
mssv = raw_input("Nhap vao ma sinh vien can tim: ")
print "\n"
db_function.getThongTinSV(mssv)