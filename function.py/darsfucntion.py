#%% Function
def summary(a,b):
    print(a+b,type(a+b))
summary(123,456)
summary(123,4.56)
summary(True,2345)
summary("123","12345")
summary([1,2,3],[4,5,6])
summary((1,2,3),(4,5,6))
#summary({1,2,3},{4,5,6})
# summary({1:23},{4:56})
def math(a,b): 
    return [a+b,a-b,a*b,a/b,a//b,a%b,a**b]
matem=math(int(input("a=")),int(input("b=")))
print(matem)       
#%% Bir nechta funksiyalar bilan ishlash
def main():
    salomlashish()
    print(hayrlashish())
def salomlashish():
    print("salom "*3) 
def hayrlashish():
    return "alvido "*2
main()           