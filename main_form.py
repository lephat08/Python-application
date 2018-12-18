import MySQLdb
db = MySQLdb.connect("localhost","root","","sinhviendb")

cursor = db.cursor()
import Tkinter as tk
from Tkinter import StringVar
import os,sys
import db_function
import string
# import backend

#Ham insert

def insert(MASV, MALOP, HOTEN, NGAYSINH, SEX, ADD, SDT, DTB):
    sql = """INSERT INTO SINHVIEN
    VALUES('""" + MASV + """','""" + MALOP + """','""" + HOTEN + """','""" + NGAYSINH + """',""" + SEX + """,'""" + ADD + """',""" + SDT + """,""" + DTB + """)"""

    try:
        cursor.execute(sql)
        # commit cac thay doi vao trong Database
        db.commit()
        print 'Them thanh cong!'
    except TypeError as e:
        print(e)
        db.rollback()

#Ham update


def update(MASV, HOTEN, BIRTH, DTB, ADD):
    sql = "UPDATE SINHVIEN SET HOTEN = '" + HOTEN + "',NGAYSINH = '" + BIRTH + "',DIEMTB = '" + DTB + "',DIACHI = '" + ADD + "' WHERE MASV='" + MASV + "';"
    try:
        cursor.execute(sql)
        # commit cac thay doi vao trong Database
        db.commit()
        print 'Cap nhat thanh cong'
    except TypeError as e:
        print(e)
        db.rollback()


#Ham in sv

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

#Ham tim kiem
def getThongTinSV():
    msvn=StringVar()
    cursor = db.cursor(MySQLdb.cursors.DictCursor)

    sql = "SELECT * FROM SINHVIEN WHERE MASV LIKE'%" + msvn.get() + "%';"

    try:
        cursor.execute(sql)
        #         return cursor.fetchall()
        results = cursor.fetchone()
        for row in results:
            a = row['MASV']
            b = row['HOTEN']
            c = row['MALOP']
            d = row['DIACHI']
            print " ||ID Student:%s || Ho ten: %1s || Ma lop: %s || Dia chi: %s\n" % (a, b, c, d)

    except TypeError as e:
        print (e)
        print "Khong tim thay msv can tim"


#Ham xoa

def xoa(a):
    sql = """DELETE FROM SINHVIEN WHERE MASV ='""" + a + """'"""
    try:
        cursor.execute(sql)
        db.commit()
        print 'xoa thanh cong!'
    except TypeError as e:
        print(e)
        db.rollback()




window = tk.Tk()
window.geometry("750x500")
# window.configure(background="")
window.title("Quan ly thong tin sinh vien")
l1=tk.Label(window,text="ID")
l1.grid(row=0,column=0)

m1=tk.Label(window,text="Ma lop")
m1.grid(row=0,column=2)

l2=tk.Label(window,text="Ho ten")
l2.grid(row=1,column=0)

l3=tk.Label(window,text="Ngay sinh")
l3.grid(row=3,column=0)

l4=tk.Label(window,text="Gioi tinh")
l4.grid(row=2,column=0)

l5=tk.Label(window,text="Que quan")
l5.grid(row=1,column=2)

l6=tk.Label(window,text="So dien thoai")
l6.grid(row=2,column=2)

l7=tk.Label(window,text="Diem")
l7.grid(row=4,column=0)

#define entries
id_text=StringVar()
e1=tk.Entry(window,textvariable=id_text)
e1.grid(row=0,column=1,sticky=tk.W,pady=4)

ml_text=StringVar()
n1=tk.Entry(window,textvariable=ml_text)
n1.grid(row=0,column=3,sticky=tk.W,pady=4)

name_text=StringVar()
e2= tk.Entry(window,textvariable=name_text)
e2.grid(row=1,column=1,sticky=tk.W,pady=4)

birth_text=StringVar()
e3= tk.Entry(window,textvariable=birth_text)
e3.grid(row=3,column=1,sticky=tk.W,pady=4)

sex_text=StringVar()
e4= tk.Entry(window,textvariable=sex_text)
e4.grid(row=2,column=1,sticky=tk.W,pady=4)

que_text=StringVar()
e5= tk.Entry(window,textvariable=que_text)
e5.grid(row=1,column=3,sticky=tk.W,pady=4)

fone_text=StringVar()
e6= tk.Entry(window,textvariable=fone_text)
e6.grid(row=2,column=3,sticky=tk.W,pady=4)

diem_num=StringVar()
e7=tk.Entry(window,textvariable=diem_num)
e7.grid(row=4,column=1,sticky=tk.W,pady=4)
# #define Listbox
list1=tk.Listbox(window,height=14,width=55)
n=['0','1','2','3']
list1.grid(row=5,column=0,rowspan=6,columnspan=2,sticky=tk.W)
for i in n:
    list1.insert(list1.size(),i)

#Atach srollbar to be list
sb1=tk.Scrollbar(window)
sb1.grid(row=5,column=2,rowspan=7)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

#Define button
b1=tk.Button(window,text="Xem het",command=insv,background="green",width=12)
b1.grid(row=5,column=3,sticky=tk.W,pady=4)

b2=tk.Button(window,text="Tim kiem",fg="green",bg="black",command=getThongTinSV,width=12)
b2.grid(row=5,column=4,sticky=tk.W,pady=4)

b3=tk.Button(window,text="Them",command=insert,background="yellow",width=12)
b3.grid(row=6,column=3,sticky=tk.W,pady=4)

b4=tk.Button(window,text="Cap nhat",fg="white",background="blue",width=12)
b4.grid(row=6,column=4,sticky=tk.W,pady=4)

b5=tk.Button(window,text="Xoa",background="red",width=12)
b5.grid(row=7,column=3,sticky=tk.W,pady=4)

b6=tk.Button(window,text="Exit",command=window.quit,width=12)
b6.grid(row=7,column=4,sticky=tk.W,pady=4)

window.mainloop()