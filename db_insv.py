import MySQLdb
import datetime
currentDT = datetime.datetime.now()
print (str(currentDT))

db = MySQLdb.connect("localhost","root","","sinhviendb")
print 'Connected to Mysql database'
cursor = db.cursor(MySQLdb.cursors.DictCursor)

sql = "SELECT * FROM SINHVIEN sv,LOP lp,KHOA kh WHERE sv.MALOP = lp.MALOP AND lp.MAKHOA = kh.Makhoa"

try:
      cursor.execute(sql)
      #lay tat ca cac hang trong list
      results = cursor.fetchall()
      print "\t\t\t                            ****Danh sach quan ly sinh vien toan truong****"
      print " "

      for row in results:
##            print row
            a = row['MASV']
            b = row['MALOP']
            c = row['HOTEN']
            d = row['NGAYSINH']
            e = row['GIOITINH']
            f = row['NIENKHOA']
            g = row['DIEMTB']
            h = row['TenKhoa']
            i = row['SDT']
            print "---------------------------------------------------------------------------------------------------------------------------------------------------------"
            print " MASV:%s  ||  MA LOP:%s ||  TEN:%s  ||  Ngay sinh:%s  || Gioi tinh:%d || Khoa:%s  || Diem:%0.2f ||  Ten khoa:%s  || SDT:%d"%\
                  ( a , b , c , d , e , f , g , h , i )
            print "---------------------------------------------------------------------------------------------------------------------------------------------------------"

except TypeError, e:
      print(e)
      print "ERROR:khong the lay thong tin"

db.close()
##select * from sinhvien sv, lop lp, khoa kh where sv.MALOP = lp.MALOP and lp.MAKHOA = kh.Makhoa 
