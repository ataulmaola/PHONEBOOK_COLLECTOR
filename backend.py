import sqlite3

def connectDatabase():
    conn=sqlite3.connect("phoneBook.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS phoneBook (id INTEGER PRIMARY KEY, fullname text  , phonenumber integer)")
    conn.commit()
    conn.close()

def insertNewEntry(fullname,phonenumber):
    conn=sqlite3.connect("phoneBook.db")
    cur=conn.cursor()
    cur.execute("SELECT fullname,phonenumber FROM phoneBook WHERE fullname=? OR phonenumber=?",(fullname, phonenumber))
    result = cur.fetchone()

    if result:
        print("Name or Number already EXISTS")
    else:
        cur.execute("INSERT INTO phoneBook VALUES (NULL,?, ?)", (fullname, phonenumber))
    conn.commit()
    conn.close()
    

def viewAllDatabase():
    conn=sqlite3.connect("phoneBook.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM phoneBook")
    rows=cur.fetchall()
    conn.close()
    ls=list(rows)
    print("\t\tID\t\t\t Name\t\t\tPhoneNumber")
    for x in ls:
            print("\t\t {}\t\t\t {}\t\t\t{}".format(x[0], x[1], x[2]))

def searchTheNumber(fullname=""):
    conn=sqlite3.connect("phoneBook.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM phoneBook WHERE fullname=? ", (fullname,))
    rows=cur.fetchall()
    conn.close()
    ls=list(rows)
    name=[x[1] for x in ls]
    number=[x[2] for x in ls]
    print(" Name is {} \n Phonenumber is {}".format(*name,*number))


def deleteTheNumber(fullname=""):
    conn=sqlite3.connect("phoneBook.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM phoneBook WHERE fullname=? ",(fullname,))
    conn.commit()
    conn.close()

def updateTheNameAndNumber(id,fullname,phonenumber):
    conn=sqlite3.connect("phoneBook.db")
    cur=conn.cursor()
    cur.execute("UPDATE phoneBook SET fullname=?, phonenumber=? WHERE id=?",(fullname,phonenumber,id))
    conn.commit()
    conn.close()
def updateTheNumber(fullname,phonenumber):
    conn=sqlite3.connect("phoneBook.db")
    cur=conn.cursor()
    cur.execute("UPDATE phoneBook SET  phonenumber=? WHERE fullname=?",(phonenumber,fullname))
    conn.commit()
    conn.close()
connectDatabase()

insertNewEntry("abas",913123132)
insertNewEntry("aaas",44344)
insertNewEntry("aeas",44444)
insertNewEntry("abras",22222)

