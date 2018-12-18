import Tkinter as tk
from Tkinter import *
import tkMessageBox
import MySQLdb

db = MySQLdb.connect("localhost","root","","sinhviendb")
cursor = db.cursor()

global sbd
global ten
global ns
global dm
global dc
global update

win=tk.Tk()
win.geometry("550x250")
win.title("Cap nhat thong tin sinh vien")
# win.configure(bg="")

id=StringVar()
id.set('')
name=StringVar()
name.set('')
birth=StringVar()
birth.set('')
mark=StringVar()
mark.set('')
add=IntVar()
add.set('')

tk.Label(win,text="ID",anchor="center",fg="blue",font=("family",11)).grid(row=0)
tk.Label(win, text="Ho ten",anchor="center",fg="blue",font=("family",11)).grid(row=0,column=3)
tk.Label(win, text="Ngay sinh",anchor="center",fg="blue",font=("family",11)).grid(row=1)
tk.Label(win, text="Diem",fg="blue",font=("family",11)).grid(row=1,column=3)
tk.Label(win, text="Dia chi",fg="blue",font=("family",11)).grid(row=2)


sbd = tk.Entry(win,textvariable=id,width=30)
ten = tk.Entry(win,textvariable=name,width=30)
ns = tk.Entry(win,textvariable=birth,width=30)
dm = tk.Entry(win,textvariable=mark,width=30)
dc = tk.Entry(win,textvariable=add,width=30)


sbd.grid(row=0, column=1)
ten.grid(row=0, column=4)
ns.grid(row=1, column=1)
dm.grid(row=1, column=4)
dc.grid(row=2, column=1)

tk.Button(win,text="Excute",bg="red",fg="white",width=13,command=lambda:update(sbd.get(),ten.get(),ns.get(),dm.get(),dc.get())).grid(row=9,column=0,sticky=tk.W,pady=4)

def update(MASV, HOTEN, BIRTH, DTB, ADD):
    sql = "UPDATE SINHVIEN SET HOTEN = '" + HOTEN + "',NGAYSINH = '" + BIRTH + "',DIEMTB = '" + DTB + "',DIACHI = '" + ADD + "' WHERE MASV='" + MASV + "';"
    try:
        tkMessageBox.showinfo("Warning", " Da cap nhat !")
        cursor.execute(sql)
        # commit cac thay doi vao trong Database
        db.commit()
        print 'Cap nhat thanh cong'
    except TypeError as e:
        print(cursor._last_executed)
        # print(e)
        db.rollback()

win.mainloop()