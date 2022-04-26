#%% Touple 
t1=(10,20)
t2=tuple((1,2))
t3=1,2,3,4,5,6
print(t1, type(t1))
print(t2,type(t2))
print(t3, type(t3))
print(t1.count(1))
print(t2.index(2))
print(len(t3))
#%%    SET 
s1={1,2,2,3,4,5,6,7}
print(s1)
#s1.add(0)
ls=[10,20,'salom',True,2]
s2=set(ls)
print(s2)
print(s2.difference(s1))       # farqini
print(s2.intersection(s1))    # bir xillarini oladi
print(s2.union(s1))            # birlashtirib beradi 2ta setni 
#%%    DICTIONARY
d1=dict()
d2={1:'salom',2:'alvido',False:True,'Hayr':25}
print(d2[1],d2[False])
print(d2)
d3={100:[1,2,4,5,6]}
print(d3)
print(d3[100][3])
d3['hello']=123
print(d3)
for i in d3.keys():
    print(i)
print(d3.keys())   # kalitlarini tekshirish
print(d3.values()) # qiymatlarini tekshirish
print(d3.items())   # ham kalit ham qiymatini tekshiradi
#%%   dictionary functions
d1={1:123,2.23:123,2:'salom'}
print(d1)   
d2={True:False,False:True,'45':45}
# d2=d1.copy()
#print(d2)
print("d2=",d2["45"])
a=d1.pop(1)  # kalit bo'yicha murojat qilinadi
print(d1)
print(a)
a=d2.popitem()   # oxirgi kalitga murojat qiladi
print(a)
d2.update(d1)   # birlashtirish
print(d2)
d2.update(d1)
print(d2)
#%% 
d1={1:10,2:20,3:30,4:30}
for i in d1.keys():
    if d1[i]==30:
        print(i,end=" ")
print("\n",len(d1),"ta element bor")        
#%%   Dictioryda input orqali ma'lumot kiritish
d1=dict()
x=int()
for i in range(int(input("n= "))):
    print("1-int,2-float,3-string,4-bool")
    x=int(input())
    if x==1:
        a=int(input("Keys: "))
    elif x==2:
        a=float(input("Keys: "))
    elif x==3:
        a=input("Keys: ")
    elif x==4:
        a=bool(input("Keys: "))
    print("1-int,2-float,3-string,4-bool")
    x=int(input())
    if x==1:  
           b=int(input ("Values: "))
    elif x==2:
        b=float(input("Values: "))
    elif x==3:
        b=input("Values: ")
    elif x==4:
        b=bool(input("Values: "))         
    d1[a]=b
print(d1)             