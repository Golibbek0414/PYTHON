# import sqlite3
# connection=sqlite3.connect("Talabalar.db")
# kursor=connection.cursor()
# def create_table():
#     kursor.execute(''' CREATE TABLE IF NOT EXISTS talaba
#                      (id NUMERIC,ism TEXT,kurs INTEGER, stipendiya REAL)''')

#     connection.commit 

# def insert_table(a,b,c,d):
#     kursor.execute('''INSERT INTO talaba VALUES(?,?,?,?,?)''',(a,b,c,d))
#     connection.commit()

# # def selection():
# #     # kursor.execute("SELECT stipendiya, ism, kurs,FROM talaba WHERE ism='Otabek'")
# #     kursor.execute("SELECT *FROM talaba ORDER BY stipendiya DESC,ism ASC") # ASC- o'sish tartibida, DESC -kamayish

# #     #st=kursor.fetchall() # so'rovdagi barcha ma'lumotlarni o'qiydi
# #     #st=kursor.fetchone() so'rovdagi birinchi ma'lumotni o'qiydi
# #     #print(*st)
# #     st=kursor.fetchmany(20) # so'rovdagi boshidagi 20 ta ma'lumotlarni o'qiydi
# #     for i in st:
# #         print(*i)

# # def delete_info():
# #     kursor.execute("DELETE FROM talaba WHERE ism='Oybek")
# #     connection.commit()

# # def update_info():
# #     kursor.execute("""UPDATE talaba SET ism='Oybek',id=20,stipendiya=1,kurs=1 WHERE ism='Ibratbek'""")
# #     connection.commit()
# create_table()
# for i in range(int(input("Nechta? "))):
#   insert_table(i+1,input("Name: "),int(input("Kurs: ")),float(input("Scholarship: ")))
# # selection()
# # delete_info()
# # update_info()z
# connection.close()

