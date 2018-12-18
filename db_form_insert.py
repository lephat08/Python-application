import MySQLdb
import Tkinter as tk
db = MySQLdb.connect("localhost","root","","sinhviendb")

cursor = db.cursor()
def insert(MASV, MALOP, HOTEN, NGAYSINH, SEX, ADD, SDT, DTB):
    sql = """INSERT INTO SINHVIEN
    VALUES('""" + MASV + """','""" + MALOP + """','""" + HOTEN + """','""" + NGAYSINH + """',""" + SEX + """,'""" + ADD + """',""" + SDT + """,""" + DTB + """)"""

    try:
        cursor.execute(sql)
        # commit cac thay doi vao trong Database
        db.commit()
        # print 'Them thanh cong!'
    except TypeError as e:
        print(e)
        db.rollback()

def show_entries():


# tk.Button(root,text='Save',command=root.insert).grid(row=8,column=1,pady=4)
root.mainloop()

