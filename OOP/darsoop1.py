# # Inheritance
# class Direktor():
#     def __init__(self,name,surname,salary):
#         self.ism=name
#         self.fam=surname
#         self.oylik=salary
#     def show(self):
#         print(self.ism,self.fam,self.oylik,end=" ")
# class Xodim(Direktor):
#     def __init__(self,name,surname,salary,rank):
#         super().__init__(name,surname,salary)  # copy vazifasida kelmoqda
#         self.lavozim=rank
#     def show(self):
#         super().show()
#         print(self.lavozim)

# abdulla=Direktor("Abdullo","Elov",1000)
# abdulla.show()
# print()
# anvar=Xodim("Anvar","Toshev",500,"Junior")
# anvar.show()


# Vorislik bu bir klassning barcha element va xususiyatlari ikkinchi klassga o'tish jaroyoni hisoblanadi
# Inkopsulyatsiya bu klass elementlari va metodlarini himoyalash yoki tanitish hisoblanadi
class Card():
    def __init__ (self,nomi,raqami):
        self.name=nomi # public
        self.numbers=raqami # public
        self.__code='1111' # Private
    def show(self):
        print(self.name,self.numbers,self.__code)
    def set_code(self,new_code): # setter public
        self.__code=new_code
    def __get_code(self): # getter private
        return self.__code
karta=Card("Humo","9800112233445566")
karta.show()
karta.name="Uzcard"
karta.numbers="8600102030405060"
karta.__code='7777'
karta.show()
karta.set_code("5555")
karta.show()
print(karta._Card__get_code())
karta._Card__code='9999'
karta.show()




# #Polimorfizm bir xil ko'rinishdagi xususiyatlarning har-hilcha ishlatilishi
# #1- operatorlarni qayta yuklash
# print(20+30)
# print("salom"+"dunyo")
# print(2*5)
# #2- funksiyalarni qayta yuklash
# print(len([1,2,3,4,5]))
# print(max({1,2,3,4,5}))
# #3- class methodlarini qayta e'lon qilish
# class Hayvon():
#     def __init__(self,nomi):
#         self.name=nomi
#     def voice(self):
#         print("Bir narsa bir narsa")
# class Cat(Hayvon):
#     pass
#     def voice(self):
#         print("Miau miau")
# class Dog(Hayvon):
#     def voice(self):
#         print("Vouv vouv")
# Thomas=Cat("Tom")
# Thomas.voice()
# Guffy=Dog("Guffy")
# Guffy.voice()




