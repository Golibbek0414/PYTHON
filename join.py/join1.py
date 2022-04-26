# Joinlar   1 Inner join  ikkita jadvanning kesishmasini oladi 2 Left join 1 jadval va kesishmasini oladi 3 Right join 2 jadval va kesishmasini oladi 4 Full join to'liq jadvalni oladi 5 Cross join bitta jadvalga oladi
import sqlite3
class DataBase():
    def __init__(self):
        self.con=sqlite3.connect("MARKAZ.db")
        self.kur=self.con.cursor()
        self.create()
        #self.insert()
        #self.inner_join()
        #self.left_join()
        #self.right_join()
        #self.full_outer_join()
        self.cross_join()
        self.con.close()
        
    
    def create(self):
        self.kur.execute('''CREATE TABLE IF NOT EXISTS Kurs(kurs_id NUMERIC, kurs_nomi TEXT,
                            PRIMARY KEY(kurs_id))''')
        self.kur.execute('''CREATE TABLE IF NOT EXISTS
                            Talaba(talaba_id NUMERIC, talaba_ismi TEXT, kurs_id NUMERIC,
                            PRIMARY KEY(talaba_id),
                            FOREIGN KEY(kurs_id) REFERENCES Kurs(kurs_id))''')
        self.con.commit()

    def insert(self):
        self.kur.execute('''INSERT INTO Kurs VALUES
                            (1,"Frontend"),
                            (2,"Go"),
                            (3,"Java"),
                            (4,"NodeJS"),
                            (5,"Flutter"),
                            (6,".Net")''')
    
        self.kur.execute('''INSERT INTO Talaba VALUES
                            (1,"Saidkamol",1),
                            (2,"G'olibbek",6),
                            (3,"Otabek",4),
                            (4,"Javohir",3),
                            (5,"Furqat",2),
                            (6,"Y.Abdulloh",3),
                            (7,"Ibratebek",7),
                            (8,"Bobur",1),
                            (9,"Q.Abdulloh",2),
                            (10,"Ziyodullo",4),
                            (11,"Oybek",6),
                            (12,"Muhammad",1),
                            (13,"Temur",7)''')
        self.con.commit()

    def inner_join(self):
        print("====================================INNER JOIN========================")
        self.kur.execute('''SELECT talaba_id, talaba_ismi, kurs_nomi FROM Talaba
                            INNER JOIN Kurs
                            ON Kurs.kurs_id=Talaba.kurs_id''')
        ls=self.kur.fetchall()
        for i in ls:
            print(*i)
    
    def left_join(self):
        print("====================================LEFT JOIN========================")
        self.kur.execute('''SELECT talaba_id, talaba_ismi, kurs_nomi FROM Talaba
                            INNER JOIN Kurs
                            USING(kurs_id)''')
        ls=self.kur.fetchall()
        for i in ls:
            print(*i)

    def right_join(self):
        print("====================================RIGHT JOIN========================")
        self.kur.execute('''SELECT talaba_id, talaba_ismi, kurs_nomi FROM Kurs
                            LEFT JOIN Talaba
                            USING(kurs_id)''')
        ls=self.kur.fetchall()
        for i in ls:
            print(*i)
        
    def full_outer_join(self):
        print("====================================FULL OUTER JOIN========================")
        self.kur.execute('''SELECT talaba_id, talaba_ismi, kurs_nomi FROM Talaba
                            LEFT JOIN Kurs
                            USING(kurs_id)
                            UNION ALL
                            SELECT talaba_id, talaba_ismi, kurs_nomi FROM Talaba
                            INNER JOIN Kurs
                            USING(kurs_id)''')
        ls=self.kur.fetchall()
        for i in ls:
            print(*i)

    def cross_join(self):
        print("====================================CROSS JOIN========================")
        self.kur.execute('''SELECT talaba_id, talaba_ismi, kurs_nomi FROM Kurs
                            CROSS JOIN Talaba''')
        ls=self.kur.fetchall()
        for i in ls:
            print(*i)
ob=DataBase()
