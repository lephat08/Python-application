import Tkinter as tk
from Tkinter import *
import tkMessageBox
import MySQLdb

db = MySQLdb.connect("localhost","root","","sinhviendb")
cursor = db.cursor()

global masv
global xoa

win=tk.Tk()
win.geometry("320x200")
win.title("Delete ID Student")
win.configure(bg="green")
id=StringVar()
id.set('')

tk.Label(win,text="ID can xoa",anchor="center",fg="black",bg="green",font=("family",13)).grid(row=0)
masv = tk.Entry(win,textvariable=id,width=50)
masv.grid(row=1)
tk.Button(win,text="Excute",bg="red",fg="white",width=13,command=lambda:xoa(masv.get())).grid(row=2,column=0,sticky=tk.W,pady=4)


def xoa(a):
    tkMessageBox.showinfo("Warning", " Du lieu se bi xoa!")
    sql = """DELETE FROM SINHVIEN WHERE MASV ='""" + a + """'"""
    try:
        cursor.execute(sql)
        db.commit()
        print 'xoa thanh cong!'
    except TypeError as e:
        print(e)
        db.rollback()
win.mainloop()