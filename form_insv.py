import Tkinter as tk
from Tkinter import StringVar
from Tkinter import IntVar
from Tkinter import *
import tkMessageBox
import MySQLdb
import db_function

db = MySQLdb.connect("localhost","root","","sinhviendb")

cursor = db.cursor()

root=tk.Tk()
root.geometry("800x400")
root.title("Thong tin sinh vien")
root.configure(bg="gray")

global tt
tk.Label(root,text='Danh sach sinh vien').grid(row=0,column=2)
# w = Label(root,text="Danh sach")
# w.pack()
# textfr=Frame(root)
tt = tk.Text(root,height=80,width=800,fg="green",bg="black",font=("Helvetica",10))
# vscroll = Scrollbar(root, orient=VERTICAL, command=tt.yview)
# Yscroll=Scrollbar(textfr,orient=VERTICAL)
# Xscroll=Scrollbar(textfr,orient=HORIZONTAL)
# tt.configure(yscrollcommand=Yscroll.set)
# tt.configure(xscrollcommand=Xscroll.set)
#
# Yscroll.config(command=tt.yview)
# Xscroll.config(command=tt.xview)
# Yscroll.pack(side=RIGHT,fill=Y)
# Xscroll.pack(side=BOTTOM,fill=X)
# tt.pack(side=LEFT,fill=BOTH,expand=TRUE)
# textfr.pack(side=TOP,fill=BOTH,expand=TRUE)
tt.grid(row=1, column=0)

def show_entries():

    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    sql = "SELECT * FROM SINHVIEN sv,LOP lp,KHOA kh WHERE sv.MALOP = lp.MALOP AND lp.MAKHOA = kh.Makhoa"
    try:
        str = ''
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            a = row['MASV']
            b = row['MALOP']
            c = row['HOTEN']
            d = row['NGAYSINH']
            e = row['GIOITINH']
            f = row['NIENKHOA']
            g = row['DIEMTB']
            h = row['TenKhoa']
            i = row['SDT']
            str += "MaLop: %s \n ID:%s Ten:%s Birth:%s Gender:%d Khoa:%s Diem:%0.2f Ten Khoa:%s Sdt:%d" % \
                  (b , a , c , d , e , f , g , h , i)
            str += "\n"
        tt.insert(tk.END,str)
    except TypeError, e:
        print(cursor._last_executed)
        print "ERROR:khong the lay thong tin"

tk.Button(root,text="Show",fg="white",bg="red",width=13,command=show_entries).grid(row=0,column=0,sticky=tk.W,pady=4)
# tk.Button(root,text="Thoat",fg="white",bg="red",command=root.quit,width=13).grid(row=1,column=0,sticky=tk.W,pady=4)
root.mainloop()








