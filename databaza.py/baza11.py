import sqlite3
class Database():
    def __init__(self):
        self.con=sqlite3.connect("MASALALAR.db")  
        self.kurs=self.con.cursor()
        self.create()
        #self.insert()
        self.sorov1()
        self.con.close()

    def create(self):
        self.kurs.execute('''CREATE TABLE IF NOT EXISTS people_data(  id INT,
                             full_name VARCHAR(50),
                             company VARCHAR(50),
                             gender VARCHAR(50),
                                born_year INT,
                                 born_month INT,
                                 born_country VARCHAR(50),
                                 car_model VARCHAR(50),
                                 job_position VARCHAR(50),
                                 salary INT,
                                 family VARCHAR(50))''')
        
        self.con.commit()
    def sorov1(self):
        print("=========")
        self.kurs.execute("SELECT *FROM people_data WHERE company BETWEEN Germany AND ")
            

ob=Database()
     

