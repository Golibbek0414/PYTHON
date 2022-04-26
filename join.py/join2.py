import sqlite3
class Database():
    def __init__(self):
        self.con=sqlite3.connect("Foundation29.db")
        self.kurs=self.con.cursor()
        self.create()
        self.insert()
        self.con.close()

    def create(self):
        self.kurs.execute('''CREATE TABLE IF NOT EXISTS 
                            plastik(plastik_id NUMERIC, plastik_nomi TEXT,plastik_kodi INTEGER
                            PRIMARY KEY(plastik_id))''')
        
        self.kurs.execute('''CREATE TABLE IF NOT EXISTS 
                                inson(inson_id NUMERIC, inson_ismi TEXT, plastik_id NUMERIC)
                                PRIMARY KEY(inson_id)
                                FOREIGN KEY(plastik_id)
                                REFERENCES plastik(plastik_id)''')
        self.con.commit()
    
    def insert(self):
        self.kurs.execute('''INSERT INTO plastik VALUES
                            (1,'Humo',1234),
                            (2,"Uzcard",7777),
                            (3,"Kapital bank",6666)''')
        
        self.kurs.execute('''INSERT INTO inson VALUES
                            (1,'ABBOS',3),
                            (2, "ASROR",2),
                            (3,"ALISHER",1)''')
        self.con.commit()

ob=Database()