import sqlite3
class Database():
    def __init__(self):
        self.con=sqlite3.connect("G'olibbek1.db")
        self.kurs=self.con.cursor()
        self.create()
        #self.insert()
        self.sorov1()
        self.con.close()

    def create(self):
        self.kurs.execute('''CREATE TABLE IF NOT EXISTS talabalar(id NUMERIC, ismi TEXT, kurs INTEGER, stipendiya REAL)''')
        self.con.commit()

    def insert (self):
        self.kurs.execute('''INSERT INTO talabalar VALUES
                            (1,'Sanjar',2,2345),
                            (2,"G'ani",1,654),
                            (3,"Sadulla",3,86594),
                            (4,"Abror",4,0987673)''')
        self.con.commit()
    def sorov1(self):
        self.kurs.execute("UPDATE talabalar SET kurs=kurs+1")
        self.con.commit()
        self.kurs.execute("DELETE FROM talabalar WHERE kurs=5")
        self.con.commit()
ob=Database()
