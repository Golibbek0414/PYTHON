# uy ishi 1

son=int (input("son="))
if son>0:
    son+=1
    print(son)
if son<0 :
    print(son)
    
   # uy ishi 2
son=int (input("son="))
if son>0:
    son+=1
    print(son)
if son<0:
    son-=2
    print(son)
    
    # uy ishi 3
son= int (input("son="))
if son>0:
    son+=1
    print(son)
elif son<0:
    son-=2
    print(son)
else:
    son=10
    print(son) 
    
    # uy ishi 4
son1=int(input("son1="))
son2=int(input("son2="))  
son3=int(input("son3="))
s=0
if son1>0:
    s+=1
if son2>0:
    s+=1
if son3>0:
    s+=1
print("musbat sonlar",s) 

    # uy ishi 5
son1=int(input("son1="))
son2=int(input("son2="))  
son3=int(input("son3="))
musbat=0
manfiy=0
nol=0
if son1>0:
    musbat+=1
if son2>0:
    musbat+=1
if son3>0:
    musbat+=1
if son1<0:
    manfiy+=1
if son2<0:
    manfiy+=1
if son3<0:
    manfiy+=1
if son1==0:
    nol+=1
if son2==0:
    nol+=1
if son3==0:
    nol+=1        
print("musbat sonlar=",musbat) 
print("manfiy sonlar=",manfiy) 
print("nolga teng=",nol)  

   # uy ishi 6
son1=int(input("son1="))
son2=int(input("son2="))
if son1>son2:
    print("katta son",son1)
else:
    print("katta son",son2)  

    # uy ishi7
son1=int(input("son1="))
son2=int(input("son2="))
if son1<son2:
    print(1)
elif son1>son2:
    print(2)
else:
    print("teng")
    
    # uy ishi8
son1=int(input("son1="))
son2=int(input("son2="))
if son1>son2:
    print("katta son",son1)
elif son2>son1:
    print("katta son",son2)
if son1<son2:
    print("kichik son",son1)
elif son1>son2:
    print("kichik son",son2)        
else:
    print("teng") 
    
    # uy ishi9
A=float(input("son1="))
B=float(input("son2="))
s=A
d=B
if A<B:
    print(A)
    print(B)
else:
    A=d
    B=s
    print(A)
    print(B)
    
    # uy ishi10
A=int(input("son1="))
B=int(input("son2="))
s=0
d=A+B
if A!=B:
    A=d
    B=d
    print("A=",A)
    print("B=",B)
else:
    A=s
    B=s
    print("A=",A) 
    print("B=",B)
    
    # uy ishi11
A=int(input("son1="))
B=int(input("son2="))
if A!=B and A<B:
    A=B
    print("A=",A)
    print("B=",B)
elif A!=B and A>B:
    B=A 
    print("A=",A)
    print("B=",B)
elif A==B:
    A=0
    B=0
    print("A=",A)
    print("B=",B) 
    
    # uy ishi12
son1=input("son1=")
son2=input("son2=")
son3=input("son3=")   
if son1<son2:
    if son1<son3:
        print("kichik son=",son1)
    else:
        print("kichik son=",son3)    
elif son2<son3:
    print("kichik son=",son2)
else:
    print("kichik son=",son3) 

    # uy ishi 13
a=input("a=")
b=input("b=")
c=input("c=")
if a>b and a>c:
    if b>c:
        print("o'rtanchi son=",b)
    else:
        print("o'rtanchi son=",a)
elif b>a and b>c:
    if a>c:
        print("o'rtanchi son=",a)
    else:
        print("o'rtanchi son=",c)    
elif c>a and c>b:
    if a>b:
        print("o'rtanchi son=",a)
    else:
        print("o'rtanchi son=",b)
        
        # uy ishi 14
son1=input("son1=")
son2=input("son2=")
son3=input("son3=")
if son1<son2:
    if son1<son3:
        print("kichik son=",son1)
    else:
        print("kichik son=",son3)    
elif son2<son3:
    print("kichik son=",son2)
else:
    print("kichik son=",son3)      
33
if son1>son2:
    if son1>son3:
        print("katta son=",son1)
    else:
        print("katta son=",son3)    
elif son2>son3:
    print("katta son=",son2)
else:
    print("katta son=",son3) 

   # uy ishi 15
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
print("Output:",max(a,b,c),end=" ")
if a>min(b,c) and a<max(b,c):
    print(a)
elif b>min(a,c) and b<max(a,c):
    print(b) 
else:
    print(c)
    
    # uy ishi 16
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if (a<b<c):
    a *= 2; b *= 2; c *= 2
else:
    a = -a; b = -b; c = -c
print("a=",a,"b=",b,"c=",c)
 
     # uy ishi 17
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
if a<b<c or c<b<a:
    a*2; b*2; c*2
else:
    a=-a;  b=-b; c=-c
print("a=",a,"b=",b,"c=",c) 

    # uy ishi 18
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
if a==b:
    print("3chi son=",c)  
elif b==c:
    print("1chi son=",a)
else: 
    print("2chi son=",b)                     

    # uy ishi 19
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))   
d=int(input("d="))
if a==b==c:
    print("4chi son=",d)
elif b==c==d:
    print("1chi son=",a)
elif c==d==a:
    print("2chi son=",b)
else:
    print("3chi son=",c)        

       


      
