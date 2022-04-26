# Object Oriented Programming(OOP)
# Obyektga yo'naltirilgan dasturlash
# OOP 4 ta qismdand iborat 
# 1 Inhertiance (Vorislik)
# 2 Polimorfizm
# 3 Inkaplsulatsiya
# 4 Abstraksiya



# class Odam():
#     a=(input("ma'lumot kiriting: "))
#     b=input("ma'lumot kiriting: ")
#     c=input("ma'lumot kiriting: ")
#     def korish(self):
#         print(self.c,"bilan dunyoni ko'rish mumkin")
#     def yugurish(self):
#         print(self.b,"bilan yugurish va yurush mumkin")
#     def yozish(self):
#         print(self.a,"bilan kod yozish mumkin")
# Anvar=Odam()
# Anvar.korish()
# Anvar.yugurish()
# Anvar.yozish()  

class Player():
    def __init__(self,name):
        self.nomi=name
        self.joni=100
        self.qurol="pichoq"
    def show(self):
        print(self.nomi,self.joni,self.qurol) 
    def add_armour(self,a):
        self.qurol=a 
    def otish(self,raqib):
        if self.joni!=0:
            raqib.joni-=50
            print(self.nomi,"pix",raqib.joni,"pax")
        else:
            print(self.nomi,"is dead ❌")
Terrorist=Player("Abdulla")
CounterTerrorist=Player("Davron")
Terrorist.add_armour("AK-47")
CounterTerrorist.add_armour("MK4")
Terrorist.show()
CounterTerrorist.show()
Terrorist.otish(CounterTerrorist)
Terrorist.show()
CounterTerrorist.show()
CounterTerrorist.otish(Terrorist)
Terrorist.show()
CounterTerrorist.show()
Terrorist.otish(CounterTerrorist)
Terrorist.show()
CounterTerrorist.show()
CounterTerrorist.otish(Terrorist)
Terrorist.show()
CounterTerrorist.show()