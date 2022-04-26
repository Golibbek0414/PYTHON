import sqlite3
connection=sqlite3.connect("Talaba2.db")
kursor=connection.cursor()
def creat_table():
  kursor.execute(''' CREATE TABLE IF NOT EXISTS talaba
                      (id NUMERIC,name TEXT, age INTEGER,number INTEGER)''')
  connection.commit()

def insert_table(a,b,c,d):
  kursor.execute(''' INSERT INTO talaba VALUES(?,?,?,?)''',(a,b,c,d))
  connection.commit()

def selection():
  kursor.execute("SELECT *FROM talaba WHERE 90>=number<101,ORDER BY name ASC ")
  connection.commit()
 
creat_table()
for i in range(int(input("Nechta= "))):
  insert_table(i+1,input("Ism= "),int(input("Yosh= ")),int(input("Bahosini kiriting= ")))
 
selection()
connection.close()

