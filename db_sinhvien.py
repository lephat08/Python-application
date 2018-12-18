import MySQLdb

db = MySQLdb.connect("localhost","root","","sinhviendb")

cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS SINHVIEN")

sql = """CREATE TABLE SINHVIEN(
         MASV VARCHAR(255) PRIMARY KEY,
         MALOP VARCHAR(255) NOT NULL,
         HOTEN VARCHAR(255) NOT NULL,
         NGAYSINH VARCHAR(255) NOT NULL,
         GIOITINH BOOLEAN NOT NULL,
         DIACHI VARCHAR(255) NOT NULL,
         SDT INT NOT NULL,
         DIEMTB FLOAT NOT NULL);"""

cursor.execute(sql)

cursor.execute("DROP TABLE IF EXISTS KHOA")

sql = """CREATE TABLE KHOA(
         Makhoa VARCHAR(255) PRIMARY KEY,
         TenKhoa VARCHAR(255) NOT NULL);"""


cursor.execute(sql)

cursor.execute("DROP TABLE IF EXISTS LOP")

sql = """CREATE TABLE LOP(
   MALOP                varchar(255)                   not null,
   MAKHOA               varchar(255)                   not null,
   TENLOP               varchar(255)                   null,
   NIENKHOA             VARCHAR(255)                         null,
   THOIHAN              VARCHAR(255)                      null,
   constraint PK_LOP primary key (MALOP));"""


cursor.execute(sql)

cursor.execute("DROP TABLE IF EXISTS CHITIET")
sql = """create table CHITIET 
(
   MASV                 varchar(255)                   not null,
   MALOP                varchar(255)                   not null,
   NGAYBATDAU           varchar(255)                         null
);"""

cursor.execute(sql)
sql = """create unique index SINHVIEN_PK on SINHVIEN (
MASV ASC
);
create index RELATIONSHIP_3_FK on CHITIET (
MALOP ASC
);
create index RELATIONSHIP_4_FK on CHITIET (
MASV ASC
);
create unique index KHOA_PK on KHOA (
MAKHOA ASC
);
create unique index LOP_PK on LOP (
MALOP ASC
);
create index RELATIONSHIP_1_FK on LOP (
MAKHOA ASC
);
"""
cursor.execute(sql)

sql = """ alter table CHITIET
   add constraint FK_CHITIET_RELATIONS_SINHVIEN foreign key (MASV)
      references SINHVIEN (MASV)
      on update restrict
      on delete restrict;"""
cursor.execute(sql)

sql = """alter table CHITIET
   add constraint FK_CHITIET_RELATIONS_LOP foreign key (MALOP)
      references LOP (MALOP)
      on update restrict
      on delete restrict;"""
cursor.execute(sql)

sql = """alter table LOP
   add constraint FK_LOP_RELATIONS_KHOA foreign key (MAKHOA)
      references KHOA (MAKHOA)
      on update restrict
      on delete restrict;"""
cursor.execute(sql)
db.close()
