import sqlite3
class Database():
    def __init__(self):
        self.con=sqlite3.connect("COUNTRY.db")
        self.kurs=self.con.cursor()
        self.create()
        self.insert()
        self.inner_join()
        
        self.con.close()
    def create(self):
        self.kurs.execute('''CREATE TABLE IF NOT EXISTS  Country(country_id NUMERIC, country_name TEXT)''')
    
        self.kurs.execute('''CREATE TABLE IF NOT EXISTS
                            Location(location_id NUMERIC, location_city TEXT, country_id NUMERIC)''')
        self.con.commit()
    
    def insert(self):
        self.kurs.execute('''INSERT INTO Country VALUES
                            (1,"UZBEKISTON"),
                            (2,"UKRAINA"),
                            (3,"YAPONIYA"),
                            (4,"AMERIKA"),
                            (5,"FRANSIYA") ''')

    
        self.kurs.execute('''INSERT INTO Location VALUES
                            (1,"TASHKENT",1),
                            (2,"KYIV",2),
                            (3,"TOKIO",3),
                            (4,"VASHINGTON",4),
                            (5,"PARIJ",5),
                            (6,"LIVERPOL",6),
                            (7,"DUBAI",7)''')
        self.con.commit()
    def inner_join(self):
        self.kurs.execute('''SELECT location_id,location_city,country_name FROM Location
                            JOIN Country
                            ON location_id=country_id''')

        ls=self.kurs.fetchall()
        for i in ls:
            print(*i)

ob=Database()
