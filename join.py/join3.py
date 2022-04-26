import sqlite3
class DataBase():
    def __init__(self):
        self.con=sqlite3.connect("Cinemalar.db")
        self.kur=self.con.cursor()
        # self.create()
        # self.insert()
        self.inner_join()
        # self.sorov1()
        self.con.close()
        
    
    def create(self):
        self.kur.execute('''CREATE TABLE IF NOT EXISTS Janr (janr_id NUMERIC, janr_nomi TEXT,
                            PRIMARY KEY(janr_id))''')
        self.kur.execute('''CREATE TABLE IF NOT EXISTS
                            Kino(kino_id NUMERIC, kino_ismi TEXT,kino_yili INTEGER,kino_davlat TEXT, janr_id NUMERIC,
                            PRIMARY KEY(kino_id),
                            FOREIGN KEY(janr_id) REFERENCES Janr(janr_id))''')
        self.con.commit()

    def insert(self):
        self.kur.execute('''INSERT INTO Janr VALUES
                            (1,"Dramatik"),
                            (2,"Jangarilar"),
                            (3,"Sarguzasht"),
                            (4,"Triller"),
                            (5,"Komediya"),
                            (6,"Milodrama"),
                            (7,"Jinoyat"),
                            (8,"Horror"),
                            (9,"Fantasy"),
                            (10,"Badiiy")''')
    
        self.kur.execute('''INSERT INTO Kino VALUES
                            (1,"Bahubali1",1997,"India",1),
                            (2,"Bahubali2",1988,"India",2),
                            (3,"Bahubali3",1989,"India",3),
                            (4,"Bahubali4",19990,"India",4),
                            (5,"Chuqur",2018,"Turkey",5),
                            (6,"Qashqirlar Makoni",2003,"Turkey",4),
                            (7,"Jodugarlar",2021,"USA",6),
                            (8,"QR 13",2017,"Russia",4),
                            (9,"a 14",2015,"China",7),
                            (10,"b 14",2016,"Uzbekiston",9)''')
        self.con.commit()

    def inner_join(self):
        print("====================================INNER JOIN========================")
        self.kur.execute('''SELECT kino_id, kino_ismi,kino_yili,kino_davlat, janr_nomi FROM Kino
                            INNER JOIN Janr
                            ON Janr.janr_id=Kino.janr_id''')
        ls=self.kur.fetchall()
        for i in ls:
            print(*i)
       


ob=DataBase()