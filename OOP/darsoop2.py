# class Komanda():
#     def __init__(self,a,b,c,d):
#         self.name=a
#         self.participants =b
#         self.coach =c
#         self.leader=d
#     def show(self):
#         print("Name:",self.name,"Participants:",self.participants,"Coach:",self.coach,"Leader:",self.leader)

# k1=Komanda(a=input("Kamanda nomini kiriting: "),b=int(input("Ishtirokchilar sonini kiriting: ")),c=input("Murabbiyni kiriting: "),d=input("Kapitanni kiriting: "))
# k2=Komanda(a=input("Kamanda nomini kiriting: "),b=int(input("Ishtirokchilar sonini kiriting: ")),c=input("Murabbiyni kiriting: "),d=input("Kapitanni kiriting: "))
# k3=Komanda(a=input("Kamanda nomini kiriting: "),b=int(input("Ishtirokchilar sonini kiriting: ")),c=input("Murabbiyni kiriting: "),d=input("Kapitanni kiriting: "))
# teams=[k1,k2,k3]
# new_kamanda=input("Kamanda nomini kiriting: ")
# for i in teams:
#     if i[0]==new_kamanda:
#         i.show()
#     else:
#         print("Bunday kamanda yo'q")    



# class Yirtqichlar():
#     def __init__(self,name,b):
#         self.ism=name
#         self.turarjoy=b
        
#     def tooth (self):
#         print(f"{self.ism} uchun tish go'sht maydalash uchun kerak")
# class Otxorlar():
#     def __init__(self,name,b):
#         self.ism=name
#         self.turarjoy=b
        
#     def tooth (self):
#         print(f"{self.ism} uchun tish o't maydalash uchun kerak")
# yh1=Yirtqichlar(name=input("Hayvon nomini kiriting: "),b=input("Turar joyini kiriting:"))
# yh2=Yirtqichlar(name=input("Hayvon nomini kiriting: "),b=input("Turar joyini kiriting:"))
# yh3=Yirtqichlar(name=input("Hayvon nomini kiriting: "),b=input("Turar joyini kiriting:"))
# yh1.tooth()
# oh1=Otxorlar(name=input("Hayvon nomini kiriting: "),b=input("Turar joyini kiriting:"))
# oh2=Otxorlar(name=input("Hayvon nomini kiriting: "),b=input("Turar joyini kiriting:"))
# oh3=Otxorlar(name=input("Hayvon nomini kiriting: "),b=input("Turar joyini kiriting:"))
# oh3.tooth()

class list1():
    def __init__(self,a,b,c,d):
        self.son1=a
        self.son2=b
        self.son3=c
        self.son4=d
    def show(self):
        print(self.son1,self.son2,self.son3,self.son4)
class list2(list1):
    def __init__(self,a,b,c,d):
        super().__init__(a,b,c,d)  # copy vazifasida kelmoqda
        
    def show(self):
        super().show()
class list3(list1):
    def __init__(self,a,b,c,d):
        super().__init__(a,b,c,d)  # copy vazifasida kelmoqda
        
    def show(self):
        super().show() 
class list4(list1):
    def __init__(self,a,b,c,d):
        super().__init__(a,b,c,d)  # copy vazifasida kelmoqda
        
    def show(self):
        super().show()      

ls1=list1(a=int(input("son kiriting: ")),b=int(input("son kiriting: ")),c=int(input("son kiriting: ")),d=int(input("son kiriting: ")))
ls1.show()
ls2=list2(a=float(input("son kiriting: ")),b=float(input("son kiriting: ")),c=float(input("son kiriting: ")),d=float(input("son kiriting: ")))
ls2.show()
ls3=list3(a=bool(input("son kiriting: ")),b=bool(input("son kiriting: ")),c=bool(input("son kiriting: ")),d=bool(input("son kiriting: ")))
ls3.show()
ls4=list4(a=str(input("son kiriting: ")),b=str(input("son kiriting: ")),c=str(input("son kiriting: ")),d=str(input("son kiriting: ")))
ls4.show()


