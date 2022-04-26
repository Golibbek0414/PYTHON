'''
class kitob():
    def __init__(self,name):
        self.nome=name
        self.muallif=input("Muallifini kiriting: ")
        self.narx=float(input("Narhi: "))
        self.nashr=input("Nashriyotini kiriting: ")
    def show(self):
        if self.nashr[0]in"ABCDEFG":
            print(f"\n Kitob nomi: {self.nome},Kitob aftori:{self.muallif},Kitob narhi: {self.narx},Kitob nashiryoti: {self.nashr}")
            
kitob1=kitob(input("1- Kitob nomi: "))
kitob2=kitob(input("2- Kitob nomi: "))
kitob3=kitob(input("3- Kitob nomi: "))
kitob4=kitob(input("4- Kitob nomi: "))
kitob5=kitob(input("5- Kitob nomi: "))
print("===============================================")
kitob1.show()
kitob2.show()
kitob3.show()
kitob4.show()
kitob5.show()

'''
class kom():
    def __init__(self,name):
        self.nome=name
        self.rami=int(input("Kom ramini kiriting: "))
        self.narx=float(input("Narhi: "))
        self.pro=input("Protesessori: ")
    def show(self):
        if 4>self.rami<16:
            print(f"\n Kompyuter nomi: {self.nome},Kompyuter rami:{self.rami},Kompyuter narhi: {self.narx},Kompyuter protsessori: {self.pro}")
            
kom1=kom(input("1- Kom nomi: "))
kom2=kom(input("2- Kom nomi: "))
kom3=kom(input("3- Kom nomi: "))
kom4=kom(input("4- Kom nomi: "))
kom5=kom(input("5- Kom nomi: "))
print("===============================================")
kom1.show()
kom2.show()
kom3.show()
kom4.show()
kom5.show()

# class Odam():
#     def __init__(self,name):
#         self.ismi=name
#     def salomlashish(self):
#        print(f"Salom {self.ismi}") 
# odam1=Odam(input("ismingizni kiriting: "))
# odam1.salomlashish()

# import time

# class Odam():
#      def __init__(self, ismi):
#           self.name = ismi

#      def kuylash(self, obj):
#           print(f"{self.name} : Bir she'r yozdim satrlari dardan iborat ")
#           obj.eshitish()
#           print(f"{obj.name} {obj.gapirish()}")

#      def eshitish(self):
#           time.sleep(4)

#      def gapirish(self):
#           return "Ofarin"


# Hindolbek = Odam("Hindolbek")
# Komol = Odam("Komol")
# Hindolbek.kuylash(Komol)

# class Time():
#      def __init__(self,soat1,minut1,sekund1):
#         self.hour=soat1
#         self.minut=minut1
#         self.sekund=sekund1
#      def show(self):
#          print(self.hour,self.minut,self.sekund)
        
        
# class Hour(Time):
    
#     def __init__(self,soat,minut,sekund):
#         super().__init__(soat,minut,sekund)
#         self.hour += 20

#     def show(self):
#         super().show()
#         print(self.ozgargansoat)
# class Minut():
#     def __init__(self,soat,minut,sekund):
#         super().__init__(soat,minut,sekund)
#         self.ozgarganminut=minut+10
# # class Sekund():
# #     pass

# h = Hour(3, 3, 4)
# print(dir(h))  # hamma metodlarni ko'rsatadi
# new_time=Time(int(input("Soat kiriting: ")),int(input("Minut kiriting: ")), int(input("Sekund kiriting: ")))
