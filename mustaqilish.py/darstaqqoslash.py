#%%  Taqqoslash va Mantiqiy amallar
# >, <, >=, <=, ==, !=,  and, or, not
print("2>5",2>5)
print("2<5",2<5)
print("2>=5",2>=5)
print("2<=5",2<=5)
print("2==5",2==5)
print("2!=5",2!=5)
print("2>5 and 3>1", 2>5 and 3>1)
print("2>5 or 3>1", 2>5 or 3>1)
print("not(2>5 and 3>1)", not(2>5 and 3>1))
#%% if elif else
son=int(input("son="))
if son>0:
    print("Musbat son:")
elif son<0:
    print("Manfiy son:")
else:
    print("Nolga teng:") 
#%% maximum
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
if a>b:
    if a>c:
        print(a)
    else:
        print(c)
elif b>c:
    print(b)
else:
    print(c)
print("max=",max(a,b,c))
print("min=",min(a,b,c))                                   