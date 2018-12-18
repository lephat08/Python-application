import Tkinter as tk
from Tkinter import *
import tkMessageBox
import MySQLdb

db = MySQLdb.connect("localhost","root","","sinhviendb")
cursor = db.cursor()

global masv
global getThongTinSV
global tt

win=tk.Tk()
win.geometry("530x300")
win.title("Tim kiem thong tin")
win.configure(bg="green")
id=StringVar()
id.set('')

tk.Label(win,text="Nhap ID Student",anchor="center",bg="blue",fg="white",font=("family",13)).grid(row=0,column=0)
masv = tk.Entry(win,textvariable=id,width=50)
masv.grid(row=1)

tk.Button(win,text="Hien Thi",bg="red",fg="white",width=13,command=lambda:getThongTinSV(masv.get())).grid(row=4,column=0,sticky=tk.W,pady=4)

tt = tk.Text(win,height=30,width=80,fg="black",bg="white",font=("Helvetica",10))
tt.grid(row=5)




def getThongTinSV(msvn):
    cursor = db.cursor(MySQLdb.cursors.DictCursor)
    sql = "SELECT * FROM SINHVIEN WHERE MASV LIKE'%" + msvn + "%';"
    try:
        str = ''
        cursor.execute(sql)
        # return cursor.fetchall()
        results = cursor.fetchall()
        for row in results:
            a = row['MASV']
            b = row['HOTEN']
            c = row['MALOP']
            d = row['DIACHI']
            str += "ID Student:%s Ho ten:%1s Ma lop:%s Dia chi: %s\n" % (a, b, c, d)
            str += "\n"
        tt.insert(tk.END, str)
    except TypeError as e:
        # print (e)
        print(cursor._last_executed)
        print "Khong tim thay msv can tim"

win.mainloop()