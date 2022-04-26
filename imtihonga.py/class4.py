# class Kitob():
#     def __init__(self,name):
#         self.nomi=name
#         self.muallif=input("Kitob muallifini kiriting: ")
#         self.narx=float(input("Kitob narxini kiriting: "))
#         self.nashriyoti=input("Kitob nashriyotini kiriting: ")
    
#     def show(self):
#         if self.nashriyoti[0] in "ABCDEFG":
#             print(f"\n Kitob nomi: {self.nomi},Kitob muallifi:{self.muallif},Kitob narxi:{self.narx},Kitob nashriyoti:{self.nashriyoti}")

# kitob1=Kitob(input("1 - Kitob nomi: "))
# kitob2=Kitob(input("2 - Kitob nomi: "))
# kitob3=Kitob(input("3 - Kitob nomi: "))
# print("=============Natija=======================")
# kitob1.show()
# kitob2.show()
# kitob3.show()



# class Kompyuter():
#     def __init__(self,nomi):
#         self.name=nomi
#         self.rami=int(input("Kompyuter ramini kiriting: "))
#         self.narxi=float(input("Kompyuter narxini kiriting: "))
#         self.protsessor=int(input("Kompyuter protsessorini kiriting: "))

#     def show(self):
#         if 4>=self.rami<=16 :
#             print(f"\n Kompyuter nomi: {self.name},Kompyuter rami: {self.rami},Kompyuter narxi: {self.narxi},Kompyuter protsessori: {self.protsessor}")


# kompyuter1=Kompyuter(input("Kompyuter nomini kiriting: "))
# kompyuter2=Kompyuter(input("Kompyuter nomini kiriting: "))
# print("===========Natija==========")
# kompyuter1.show()
# kompyuter2.show()

# class Odam():
#     def __init__(self,nomi):
#         self.name=nomi
#         # self.solomlashish()
#     def solomlashish(self):
#         print(f"salom {self.name}")
# inson1=Odam(input("Ismingizni kiriting: "))
# inson1.solomlashish()

# import time
# class Odam():
#     def __init__(self,ismi):
#         self.name=ismi
        
#     def kuylash(self,obj):
#         print(f"{self.name}: Assalomu alaykum")
#         obj.eshitish()
#         print(f"{obj.name}: {obj.gapirish()}")
#     def eshitish(self):
#         time.sleep(5)

#     def gapirish(self):
#         return "Vaalykum assalom"

# Kamol=Odam("Kamol")
# Davron=Odam("Davron")
# Kamol.kuylash(Davron)

# import time
# class Odam():
#     def __init__(self,name):
#         self.ismi=name
        
#     def yugurish(self):
#         print(f"{self.ismi}: yugurmoqda")
#         self.kutush()
#         print(f"{self.ismi} {self.yiqilish()}")

#     def kutush(self):
#         time .sleep(5)
    
#     def yiqilish(self):
#         return "Siz yiqildingiz turub yugurishni davom ettiring!!!"

# Samandar=Odam("Samandar")
# Samandar.yugurish()




