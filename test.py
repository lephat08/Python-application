#!/usr/bin/python

# -*- coding: utf8 -*-
import Tkinter as tk
from Tkinter import StringVar
from Tkinter import IntVar
from Tkinter import *
import tkMessageBox
import MySQLdb


db = MySQLdb.connect("localhost","root","","sinhviendb")

cursor = db.cursor()





root=tk.Tk()
root.geometry("600x300")
root.title("Le Huu Phat_Nien luan co so TT&MMT")
root.configure(bg="orange")

msv=StringVar()
msv.set('')
malop=StringVar()
malop.set('')
name=StringVar()
name.set('')
birth=StringVar()
birth.set('')
sex=IntVar()
sex.set('')
add=StringVar()
add.set('')
fone=IntVar()
fone.set('')
mark=StringVar()
mark.set('')



tk.Label(root,text="ID",anchor="center",fg="blue",bg="orange",font=("family",11)).grid(row=0)
tk.Label(root, text="Ma lop",anchor="center",fg="blue",bg="orange",font=("family",11)).grid(row=0,column=3)
tk.Label(root, text="Ho ten",anchor="center",fg="blue",bg="orange",font=("family",11)).grid(row=1)
tk.Label(root, text="Ngay sinh",fg="blue",bg="orange",font=("family",11)).grid(row=1,column=3)
tk.Label(root, text="Gioi tinh",fg="blue",bg="orange",font=("family",11)).grid(row=2)
tk.Label(root, text="Dia chi",fg="blue",bg="orange",font=("family",11)).grid(row=2,column=3)
tk.Label(root, text="Phone",fg="blue",bg="orange",font=("family",11)).grid(row=3)
tk.Label(root, text="Diem",fg="blue",bg="orange",font=("family",11)).grid(row=3,column=3)


e1 = tk.Entry(root,textvariable=msv,width=30)
e2 = tk.Entry(root,textvariable=malop,width=30)
e3 = tk.Entry(root,textvariable=name,width=30)
e4 = tk.Entry(root,textvariable=birth,width=30)
e5 = tk.Entry(root,textvariable=sex,width=30)
e6 = tk.Entry(root,textvariable=add,width=30)
e7 = tk.Entry(root,textvariable=fone,width=30)
e8 = tk.Entry(root,textvariable=mark,width=30)

e1.grid(row=0, column=1)
e2.grid(row=0, column=4)
e3.grid(row=1, column=1)
e4.grid(row=1, column=4)
e5.grid(row=2, column=1)
e6.grid(row=2, column=4)
e7.grid(row=3, column=1)
e8.grid(row=3, column=4)

tk.Button(root,text="Them",fg="black",bg="green",width=13,command=lambda:insert_sv(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get())).grid(row=8,column=0,sticky=tk.W,pady=4)
tk.Button(root,text="Xoa",bg="yellow",width=13,command=lambda:execfile('delete_form.py')).grid(row=9,column=1,sticky=tk.W,pady=4)
tk.Button(root,text="Cap Nhat",bg="blue",fg="white",width=13,command=lambda:execfile('win_insert.py')).grid(row=9,column=0,sticky=tk.W,pady=4)
tk.Button(root,text="Xem",width=13,command=lambda:execfile('form_insv.py')).grid(row=10,column=0,sticky=tk.W,pady=4)
tk.Button(root,text="Thoat",fg="white",bg="red",command=root.quit,width=13).grid(row=8,column=1,sticky=tk.W,pady=4)
tk.Button(root,text="Find",width=13,command=lambda:execfile('find_idsv.py')).grid(row=10,column=1,sticky=tk.W,pady=4)
# tk.Button(root,text="Cap Nhat",width=13,command=lambda:update(e1.get(),e3.get(),e4.get(),e8.get(),e6.get())).grid(row=9,column=0,sticky=tk.W,pady=4)


def create_windown():
     windown = tk.Toplevel('form_insv.py')

# def update(MASV, HOTEN, BIRTH, DTB, ADD):
#     sql = "UPDATE SINHVIEN SET HOTEN = '" + HOTEN + "',NGAYSINH = '" + BIRTH + "',DIEMTB = '" + DTB + "',DIACHI = '" + ADD + "' WHERE MASV='" + MASV + "';"
#     try:
#         tkMessageBox.showinfo("Warning", " Da cap nhat !")
#         cursor.execute(sql)
#         # commit cac thay doi vao trong Database
#         db.commit()
#         print 'Cap nhat thanh cong'
#     except TypeError as e:
#         print(cursor._last_executed)
#         # print(e)
#         db.rollback()



def insert_sv(MASV,MALOP,HOTEN,NGAYSINH,SEX,ADD,SDT,DTB):
    tkMessageBox.showinfo("Warning", " Du lieu se duoc save Click Ok !")
    sql = """INSERT INTO SINHVIEN
        VALUES('""" + MASV + """','""" + MALOP + """','""" + HOTEN + """','""" + NGAYSINH + """',""" + SEX + """,'""" + ADD + """',""" + SDT + """,""" + DTB + """)"""
    try:
        cursor.execute(sql)
        # commit cac thay doi vao trong Database
        db.commit()
        print 'Them thanh cong!'
    except TypeError as e:
       # print(e)
       print(cursor._last_executed)
       db.rollback()

# def xoa(a):
#     tkMessageBox.showinfo("Warning", " Du lieu se bi xoa!")
#     sql = """DELETE FROM SINHVIEN WHERE MASV ='""" + a + """'"""
#     try:
#         cursor.execute(sql)
#         db.commit()
#         print 'xoa thanh cong!'
#     except TypeError as e:
#         print(cursor._last_executed)
#         # print(e)
#         db.rollback()


root.mainloop()

# tk.Button(root, text="Show", fg="white", bg="red", width=13, command=show_entries).grid(row=0, column=0,sticky=tk.W, pady=4)




    # def them_sv():
#     tkMessageBox.showinfo("Warning"," Du lieu se duoc save Click Ok !")
#     arraySV = [
#         {'MASV': 'A1500398', 'MALOP': 'DI15Y9A1', 'HOTEN': 'le khac phuong nhi', 'NGAYSINH': '11/07/1994',
#          'GIOITINH': '1', 'ADD': 'KDC Hong Phat', 'SDT': '0923657515', 'DTB': '2.9'},
#         {'MASV': 'O1500399', 'MALOP': 'DT15Y9A2', 'HOTEN': 'le huu phat', 'NGAYSINH': '08/03/1994', 'GIOITINH': '0',
#          'ADD': '41 Huynh Cuong,p.An Cu', 'SDT': '0123456647', 'DTB': '2.7'},
#         {'MASV': 'F1500393', 'MALOP': 'D15Y9A3', 'HOTEN': 'le hieu', 'NGAYSINH': '26/03/1993', 'GIOITINH': '0',
#          'ADD': '42 Tran Phu', 'SDT': '0256896275', 'DTB': '1.7'},
#         {'MASV': 'H1500395', 'MALOP': 'DY15Y9A4', 'HOTEN': 'si du', 'NGAYSINH': '26/12/1994', 'GIOITINH': '1',
#          'ADD': '128/51 CMT8', 'SDT': '0923589456', 'DTB': '1.7'},
#         {'MASV': 'K1500400', 'MALOP': 'DC15Y9A5', 'HOTEN': 'van hau', 'NGAYSINH': '28/11/1992', 'GIOITINH': '0',
#          'ADD': '125/89/14 Tran Hoang Na', 'SDT': '0939658479', 'DTB': '3.7'},
#         {'MASV': 'L1500301', 'MALOP': 'DI15Y9A1', 'HOTEN': 'Dinh Thi Phuong', 'NGAYSINH': '16/06/1992', 'GIOITINH': '1',
#          'ADD': '149/45 Tam Vu', 'SDT': '093894563', 'DTB': '4.0'},
#         {'MASV': 'M1500302', 'MALOP': 'DI15Y9A1', 'HOTEN': 'Le Thi Kim Oanh', 'NGAYSINH': '18/04/1994', 'GIOITINH': '1',
#          'ADD': 'Ap Long Thanh H.Tra On T.Vinh Long', 'SDT': '0933698452', 'DTB': '3.7'},
#         {'MASV': 'N1500310', 'MALOP': 'DC15Y9A5', 'HOTEN': 'Phan Van Hai', 'NGAYSINH': '22/03/1997', 'GIOITINH': '0',
#          'ADD': 'H.Cau Ke T.Tra Vinh', 'SDT': '0989654123', 'DTB': '2.7'},
#         {'MASV': 'D1500399', 'MALOP': 'DY15Y9A4', 'HOTEN': 'Luu Van Ba', 'NGAYSINH': '28/07/1997', 'GIOITINH': '0',
#          'ADD': '78/2 Khom 3 T.Vinh Long', 'SDT': '093965249', 'DTB': '3.79'},
#     ]
#     for sv in arraySV:
#         db_function.insert(sv['MASV'], sv['MALOP'], sv['HOTEN'], sv['NGAYSINH'], sv['GIOITINH'], sv['ADD'], sv['SDT'],
#                            sv['DTB'])




# tk.Button(root,text="Tim",width=13).grid(row=10,column=1,sticky=tk.W,pady=4)


root.mainloop()

