import sqlite3
con=sqlite3.connect("imtixon.db")
kursor=con.cursor()
con.execute('''CREATE TABLE IF NOT EXISTS people_data(  id INT,
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
con.commit()

