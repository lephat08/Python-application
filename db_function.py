import MySQLdb
db = MySQLdb.connect("localhost","root","","sinhviendb")

cursor = db.cursor()
#Them SINH VIEN
# def insert(MASV,MALOP,HOTEN,NGAYSINH,SEX,ADD,SDT,DTB):
#       sql = """INSERT INTO SINHVIEN
#       VALUES('"""+MASV+"""','"""+MALOP+"""','"""+HOTEN+"""','"""+NGAYSINH+"""',"""+SEX+""",'"""+ADD+"""',"""+SDT+""","""+DTB+""")"""
#
#       try:
#          cursor.execute(sql)
#          # commit cac thay doi vao trong Database
#          db.commit()
#          print 'Them thanh cong!'
#       except TypeError as e:
#             print(e)
#             db.rollback()


#Get Thong Tin
def getThongTinSV(msvn) :

     cursor = db.cursor(MySQLdb.cursors.DictCursor)
     sql = "SELECT * FROM SINHVIEN WHERE MASV LIKE'%" + msvn + "%';"
     try :
         cursor.execute(sql)
#         return cursor.fetchall()
         results = cursor.fetchall()
         for row in results:
             a = row['MASV']
             b = row['HOTEN']
             c = row['MALOP']
             d = row['DIACHI']
             print " ||ID Student:%s || Ho ten: %1s || Ma lop: %s || Dia chi: %s\n"% (a,b,c,d)

     except TypeError as e:
         print (e)
         print "Khong tim thay msv can tim"
#         return e


#UPDATE THONG TIN SV
def update(MASV,HOTEN,BIRTH,DTB,ADD):
      sql = "UPDATE SINHVIEN SET HOTEN = '"+HOTEN+"',NGAYSINH = '"+BIRTH+"',DIEMTB = '"+DTB+"',DIACHI = '"+ADD+"' WHERE MASV='"+MASV+"';"
      try:
         cursor.execute(sql)
         # commit cac thay doi vao trong Database
         db.commit()
         print 'Cap nhat thanh cong'
      except TypeError as e:
            print(e)
            db.rollback()
#INSERT LOP
def them_lop(MALOP,MAKHOA,TENLOP,NIENKHOA,THOIHAN):
      sql ="""INSERT INTO LOP
      VALUES('"""+MALOP+"""','"""+MAKHOA+"""','"""+TENLOP+"""',
              '"""+NIENKHOA+"""','"""+THOIHAN+"""')"""
      try:
         cursor.execute(sql)
         #commit cac thay doi vao trong Database
         db.commit()
      except TypeError as e:
            print(e)
            db.rollback()



#DELETE

      def xoa(a):
          sql = """DELETE FROM SINHVIEN WHERE MASV ='""" + a + """'"""
          try:
              cursor.execute(sql)
              db.commit()
              print 'xoa thanh cong!'
          except TypeError as e:
              print(e)
              db.rollback()

#SHOW
def insv():
    cursor = db.cursor(MySQLdb.cursors.DictCursor)

    sql = "SELECT * FROM SINHVIEN sv,LOP lp,KHOA kh WHERE sv.MALOP = lp.MALOP AND lp.MAKHOA = kh.Makhoa"

    try:
        cursor.execute(sql)
        # lay tat ca cac hang trong list
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
            print " MASV:%s  ||  MA LOP:%s ||  TEN:%s  ||  Ngay sinh:%s  || Gioi tinh:%d || Khoa:%s  || Diem:%0.2f ||  Ten khoa:%s  || SDT:%d" % \
                  (a, b, c, d, e, f, g, h, i)
            print "---------------------------------------------------------------------------------------------------------------------------------------------------------"

    except TypeError, e:
        print(e)
        print "ERROR:khong the lay thong tin"

    # db.close()
