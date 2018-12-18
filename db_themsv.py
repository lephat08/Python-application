import MySQLdb
import Tkinter as tk
import datetime
import db_function
# currentDT = datetime.datetime.now()
# print (str(currentDT))
db = MySQLdb.connect("localhost","root","","sinhviendb")
# print 'Connected to Mysql database'
cursor = db.cursor()

print "\t                            Them thong tin sinh vien vao CSDL"
id = raw_input("nhap msv: ")
cl = raw_input("Ma lop: ")
name = raw_input("Ho&ten: ")
birth = raw_input("Ngay sinh: ")
sex = raw_input("Gioi tinh: ")
mark = raw_input("Diem tb: ")
add = raw_input("Dia chi: ")
fone = raw_input("sdt: ")
db_function.insert(id,cl,name,birth,sex,add,fone,mark)
# win=tk.Tk()
#
# tk.Label(win,text="ID",anchor="center",fg="blue").grid(row=0)
# tk.Label(win, text="Ma lop",anchor="center",fg="blue").grid(row=0,column=3)
# tk.Label(win, text="Ho ten",anchor="center",fg="blue").grid(row=1)
# tk.Label(win, text="Ngay sinh",fg="blue").grid(row=1,column=3)
# tk.Label(win, text="Gioi tinh",fg="blue").grid(row=2)
# tk.Label(win, text="Dia chi",fg="blue").grid(row=2,column=3)
# tk.Label(win, text="Phone",fg="blue").grid(row=3)
# tk.Label(win, text="Diem",fg="blue").grid(row=3,column=3)
# def userput():
#
#     id = raw_input("nhap msv: ")
#     cl = raw_input("Ma lop: ")
#     name = raw_input("Ho&ten: ")
#     birth = raw_input("Ngay sinh: ")
#     sex = raw_input("Gioi tinh: ")
#     mark = raw_input("Diem tb: ")
#     add = raw_input("Dia chi: ")
#     fone = raw_input("sdt: ")
#     db_function.insert(id, cl, name, birth, sex, add, fone, mark)
# win.mainloop()