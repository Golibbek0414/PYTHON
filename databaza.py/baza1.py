# import sqlite3
# class Database():
#     def __init__(self):
#         self.con=sqlite3.connect("MILLIY_TAOMLAR.db")
#         self.kursor=self.con.cursor()
#     def create(self):
#         self.kursor.execute("CREATE TABLE IF NOT EXISTS talaba(id NUMERIC, name TEXT, masaliq TEXT)")
#         self.con.commit()
    
#     def insert(self):
#         self.kursor.execute("INSERT INTO talaba VALUES(1,'OSH','sabzi'),(2,'mastava','kartoshka'),(3,'shashlik','gosh'),(4,'tadirgosh','gosht'),(5,'honim',"'manti','gruch'"),(6,'somsa','tovuq'),(7,'beshtikis',"'guruch','gosht'")")
#         self.con.commit()
    
#     def toam(self):
#         self.kursor.execute("SELECT *FROM talaba")
#         ls=self.kursor.fetchall()
       
#         for i in ls:
#             if i[1][-1]=='a':
#                 print(*i)

#         print()
#         for i in ls:
#             if 'gruch' in i[2] :
#                 print(*i)



# ob=Database()
# # ob.create()
# #ob.insert()
# #ob.update()
# # ob.delete()
# ob.toam()

import sqlite3

class Database():
    def __init__(self):
        self.con=sqlite3.connect("BOZOR.db")
        self.kursor=self.con.cursor()
    def create(self):
        self.kursor.execute("CREATE TABLE IF NOT EXISTS talaba(id NUMERIC, name TEXT, narx REAL, turi TEXT)")
        self.con.commit()  
    def insert(self):
        self.kursor.execute("INSERT INTO talaba VALUES(1,'OLMA',1200,'BESHYULDUZ'),(2,'NOK',2500,'QATTIQ,YUMSHOQ'),(3,'GILOS',1456,'SHIRIN,NORDON'),(4,'ORIK',146,'SHIRIN,NORDON'),(5,'UZUM',1452,'RIZAMAT, HUSANYNI'),(6,'XURMO',7895,'PISHMAGAN'),(7,'XURMO',45621,'PISHGAN'),(8,'OLCHA',851,'NORDON'),(9,'NOK',987452,'SHIRIN'),(10,'OLCHA',87412,'NORDON')")

        self.con.commit()
    
    def sorov1(self):
        print("++++++++++++++++++++++++++++++")
        self.kursor.execute("SELECT * FROM talaba")
        for i in self.kursor.fetchall():
            self.kursor.execute("DELETE FROM talaba WHERE id=? AND name=? AND narx=? AND turi=?",(i[0],i[1],i[2],i[3]))
            self.con.commit()
            self.insert(i[0],i[1],i[2],i[3])
    
    def sorov2(self):
        self.kursor.execute("SELECT * FROM talaba ORDER BY narx DESC LIMIT 5")
        for i in self.kursor.fetchall():
            print(*i)

ob=Database()
# ob.create()
#ob.insert()
ob.sorov1()
ob.sorov1()
     