import MySQLdb
import db_function
import datetime
currentDT = datetime.datetime.now()
print (str(currentDT))
db = MySQLdb.connect("localhost","root","","sinhviendb")
print 'Connected to Mysql database'
cursor = db.cursor()
#Khoa table
arrayKH = [{'MK':'CNTT','TENK':'TT&MMT'},
           {'MK':'MT','TENK':'MOI TRUONG'},
           {'MK':'SP','TENK':'SU PHAM'},
           {'MK':'KT','TENK':'KINH TE'},
           {'MK':'TN','TENK':'TU NHIEN'},
           ]
for kh in arrayKH:
      sql = """INSERT INTO KHOA
      VALUES('"""+kh['MK']+"""','"""+kh['TENK']+"""')"""

      try:
         cursor.execute(sql)
         db.commit()
         print 'them thanh cong!'
      except TypeError as e:
            print(e)
            db.rollback()
db.close()

khoa = [
           {'MALOP':'DI15Y9A1','MAKHOA':'CNTT','TENLOP':'Truyen Thong & Mang May Tinh','NIENKHOA':'41','THOIHAN':'4.5 nam'},
           {'MALOP':'DT15Y9A2','MAKHOA':'MT','TENLOP':'Ki Thuat Moi Truong','NIENKHOA':'41','THOIHAN':'4 nam'},
           {'MALOP':'DI15Y9A3','MAKHOA':'SP','TENLOP':'Su Pham Toan','NIENKHOA':'41','THOIHAN':'4 nam'},
           {'MALOP':'DY15Y9A4','MAKHOA':'KT','TENLOP':'Tai Chinh Ngan Hang','NIENKHOA':'41','THOIHAN':'4 nam'},
           {'MALOP':'DC15Y9A5','MAKHOA':'TN','TENLOP':'Khoa Hoc May Tinh','NIENKHOA':'41','THOIHAN':'4 nam'},
           ]
for lp in khoa:
      db_function.them_lop(lp['MALOP'],lp['MAKHOA'],lp['TENLOP'],lp['NIENKHOA'],lp['THOIHAN'])


# arraySV = [
#             {'MASV':'C1500398','MALOP':'DI15Y9A1','HOTEN':'le khac phuong nhi','NGAYSINH':'11/07/1994','GIOITINH':'1','ADD':'KDC Hong Phat','SDT':'0923657515','DTB':'2.9'},
#             {'MASV':'C1500399','MALOP':'DT15Y9A2','HOTEN':'le huu phat','NGAYSINH':'08/03/1994','GIOITINH':'0','ADD':'41 Huynh Cuong,p.An Cu','SDT':'0123456647','DTB':'2.7'},
#             {'MASV':'C1500393','MALOP':'D15Y9A3','HOTEN':'le hieu','NGAYSINH':'26/03/1993','GIOITINH':'0','ADD':'42 Tran Phu','SDT':'0256896275','DTB':'1.7'},
#             {'MASV':'C1500395','MALOP':'DY15Y9A4','HOTEN':'si du','NGAYSINH':'26/12/1994','GIOITINH':'1','ADD':'128/51 CMT8','SDT':'0923589456','DTB':'1.7'},
#             {'MASV':'C1500400','MALOP':'DC15Y9A5','HOTEN':'van hau','NGAYSINH':'28/11/1992','GIOITINH':'0','ADD':'125/89/14 Tran Hoang Na','SDT':'0939658479','DTB':'3.7'},
#             {'MASV':'C1500301','MALOP':'DI15Y9A1','HOTEN':'Dinh Thi Phuong','NGAYSINH':'16/06/1992','GIOITINH':'1','ADD':'149/45 Tam Vu','SDT':'093894563','DTB':'4.0'},
#             {'MASV':'C1500302','MALOP':'DI15Y9A1','HOTEN':'Le Thi Kim Oanh','NGAYSINH':'18/04/1994','GIOITINH':'1','ADD':'Ap Long Thanh H.Tra On T.Vinh Long','SDT':'0933698452','DTB':'3.7'},
#             {'MASV':'C1500310','MALOP':'DC15Y9A5','HOTEN':'Phan Van Hai','NGAYSINH':'22/03/1997','GIOITINH':'0','ADD':'H.Cau Ke T.Tra Vinh','SDT':'0989654123','DTB':'2.7'},
#             {'MASV':'B1500399','MALOP':'DY15Y9A4','HOTEN':'Luu Van Ba','NGAYSINH':'28/07/1997','GIOITINH':'0','ADD':'78/2 Khom 3 T.Vinh Long','SDT':'093965249','DTB':'3.79'},
#             ]
# for sv in arraySV:
#       db_function.insert(sv['MASV'],sv['MALOP'],sv['HOTEN'],sv['NGAYSINH'],sv['GIOITINH'],sv['ADD'],sv['SDT'],sv['DTB'])




