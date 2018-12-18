import MySQLdb

db = MySQLdb.connect("localhost","root","","sinhviendb")

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print "DATABASE version : %s" % data

db.close()
