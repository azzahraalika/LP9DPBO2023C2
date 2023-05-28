import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_lagu"   
)

dbcursor = mydb.cursor()

sql = "INSERT INTO idol(nama_idol) VALUES ('Blackpink')"
dbcursor.execute(sql)

mydb.commit()

print(dbcursor.rowcount, "record inserted.")

dbcursor = mydb.cursor()
dbcursor.execute("SELECT * FROM idol")

myresult = dbcursor.fetchall()
print("Daftar Idol")
for x in myresult:
    print(x)
    
dbcursor = mydb.cursor()
sql = "DELETE FROM idol WHERE nama_idol = 'Blackpink'"
dbcursor.execute(sql)

mydb.commit()

print(dbcursor.rowcount, "record(s) deleted")

print("Daftar idol setelah dihapus")

dbcursor = mydb.cursor()
dbcursor.execute("SELECT * FROM idol")

myresult = dbcursor.fetchall()

for x in myresult:
    print(x)
    