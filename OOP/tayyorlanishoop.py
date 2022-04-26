'''
class Hayvon():
    def __init__(self,a):
        self.name=a

class Yirtqich(Hayvon):
    def yugurish(self):
        print(self.name,"o'ljani ovlash uchun yuguradi")
        self.ovlash()
        self.uxlash()
    
    def ovlash(self):
        print(self.name,"yashash uchun ovlaydi")
    
    def uxlash(self):
        print(self.name,"kuch yig'ish uchun uxlaydi")

class Utxur(Hayvon):
    def yugurish(self):
        print(self.name,"yirtqichdan qochish uchun yuguradi")
        self.avlod_qoldirish()
        self.eshitish()
    
    def avlod_qoldirish(self):
        print(self.name,"kamaymaslik uchun avlod qoldiradi")

    def eshitish(self):
        print(self.name,"yirtqichlarni yaqinlashganini eshitadi")

sher=Yirtqich("Alex")
sher.yugurish()
kiyik=Utxur("Bambi")
kiyik.yugurish()
'''






class Shape():
    def __init__(self,name):
        self.nomi=name
class Line(Shape):
    def show(self):
        print(10*"*")

class Triangle(Shape):
    def show(self):
        n=int(input("Nechata: "))
        for i in range(1,n+1):
            for j in range(i,i+1):
                if i==1 or i==n or j==i or j==1:
                    print("* ",end="")
                
                else:
                    print(end=" ")
                
            print()
class Rectangle(Shape):
    def show(self):
        n=int(input("Nechat: "))
        for i in range(1,n+1):
            for j in range(1,i+1):
                if i==1 or i==n or j==1 or j==n:
                    print("* ",end="")
                
                else:
                    print(end=" ")
                
            print()

class NullShape(Shape):
    def show(self):
        print("Bo'sh shakl")
ob1=Line("Line")
ob2=Triangle("Triangle")
ob3=Rectangle("Rectangle")
ob4=NullShape("NullShape")
ls=[ob1,ob2,ob3]
k=1
name=input("Name: ")
for i in ls:
    if name==i.nomi:
        i.show()
        k=0
        break
if k==1:
    ob4.show()