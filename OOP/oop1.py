# class talaba():
#     name=input("Ismingizni kiriting: ")
#     surname=input("Familyangizni kiriting: ")
#     age=int(input("Yoshingizni kiriting: "))
#     region=input("Tug'ulgan viloyatingizni kiriting: ")  # viloyat=region
#     mist=input("Tug'ulgan tumaningizni kiriting: ")    # mist=tuman
#     village=input("Tug'ulgan qishlog'ingizni kiriting: ")
#     school=int(input("O'qigan maktabingizni kiriting: "))
#     university=input("O'qigan universitettingizni kiriting: ")
#     print()
#     print("Ma'lumotlaringiz=========================================Ma'lumotlaringiz")
#     def ism(self):
#         print(self.name,"go'zal ismga ega inson ekansiz")
#     def fam(self):
#         print(self.surname,"go'zal familyaga ega inson ekansiz")
#     def yosh(self):
#         print(self.age,"yoshda ekansiz")
#     def viloyat(self):
#         print(self.region,"viloyatidan ekansiz")
#     def tuman(self):
#         print(self.mist,"tumanidan ekansiz")
#     def qishloq(self):
#         print(self.village,"qishlog'idan ekansiz")
#     def maktab(self):
#         print(self.school,"maktabda o'qigan ekansiz")
#     def university(self):
#         print(self.university,"universtitda o'qigan ekansiz")
# inson=talaba()
# inson.ism()
# inson.fam()
# inson.yosh()
# inson.viloyat()
# inson.tuman()
# inson.qishloq()
# inson.maktab()
# inson.university()



# class Player():
#     def __init__(self,name):
#         self.nomi=name
#         self.joni=100
#         self.qurol="pichoq"
#     def show(self):
#         print(self.nomi,self.joni,self.qurol) 
#     def add_armour(self,a):
#         self.qurol=a 
#     def otish(self,raqib):
#         if self.joni!=0:
#             raqib.joni-=50
#             print(self.nomi,"pix",raqib.joni,"pax")
#         else:
#             print(self.nomi,"is dead ❌")
# Terrorist=Player("Abdulla")
# CounterTerrorist=Player("Davron")
# Terrorist.add_armour("AK-47")
# CounterTerrorist.add_armour("MK4")
# Terrorist.show()
# CounterTerrorist.show()
# Terrorist.otish(CounterTerrorist)
# Terrorist.show()
# CounterTerrorist.show()
# CounterTerrorist.otish(Terrorist)
# Terrorist.show()
# CounterTerrorist.show()
# Terrorist.otish(CounterTerrorist)
# Terrorist.show()
# CounterTerrorist.show()
# CounterTerrorist.otish(Terrorist)
# Terrorist.show()
# CounterTerrorist.show()
# Terrorist.otish(CounterTerrorist)




#%%  Object Oriented Programming

class Talaba:   # Talaba nomli klass yaratildi
    def __init__(self,ism,familiya,tyil): # Talabaning xususiyatlari ismi familiyasi tyili
        self.ism=ism
        self.familiya=familiya
        self.tyil=tyil
        self.bosqich=int(input("Nechanchi bosqichda o'qiydi: "))
    def get_info(self):  # Talaba haqida ma'lumot 
        return f"{self.ism} {self.familiya}, {self.tyil} -yil, {self.bosqich}-bosqich talabasi "
    
    
    def get_name(self): # Talabaning ismini qaytaradi
        return self.ism

    def get_surname(self):  # Talabaning familiyasini qaytaradi
        return self.familiya
    
    def set_bosqich(self,yangi_bosqich):  # Talabaning kursini yangilovchi metod
        self.bosqich=yangi_bosqich

    def update_bosqich(self):  # Talabaning 1taga ko'tarishd
        self.bosqich +=1

    
talaba1=Talaba("Alijon","Valiyev",1995)
# print(talaba1.ism) 
# print(talaba1.bosqich)
# print(talaba1.get_info())
# print(talaba1.update_bosqich())
# print(talaba1.get_info())


class Fan():   # Fan nomli klass yaratildi
    def __init__(self,nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []    # Talabalar ro'yxatini saqlab boradigan bo'sh list
     
    def add_student(self,talaba):  # Fanga talabalar qo'shish  bu yerda talaba abyekt bo'lib kelmoqda
         self.talabalar.append(talaba)  # Talabalr ro'yxatiga talaba qo'shilmoqda
         self.talabalar_soni += 1


  


matematika=Fan("Oliy matematika")
print(matematika.talabalar_soni)
print(talaba1.ism)
print(matematika.add_student(talaba1))