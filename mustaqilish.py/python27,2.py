

d1=dict()
key=int()
values=()
for i in range(int(input("n= "))):
    print("1-int.2-float, 3-string, 4-bool")
    x=int(input("Keysni tipini kiriting: "))
    if x==1:
        a=int(input("keys: "))
    elif x==2:
        a=float(input("Keys: "))
    elif x==3:
        a=input("Keys: ")
    elif x==4: 
        a=bool(input("Keys: "))
    print("1-int, 2-float, 3-string, 4-bool")
    x=int(input("Valuesni tipini kiriting: "))
    if x==1:
        b=int(input("Values: "))
    elif x==2:
        b=float(input("Values: "))
    elif x==3:
        b=input("Values: ")
    elif x==4:
        b=bool(input("Values: "))
    d1[a]=b
d2=list()
# d2.append([d1[i] for i in d1.keys() if d1[i]==str(d1[i])])
d2=([i for i in d1.values() if i==str(i)])
d2.sort()
print(d2)
''''
l=open("Tavarlar","r")
text=list()

text=l.readlines()
l.close()
text=text[0]
p=""
A=list()
K=list()
a=0
k=0
print(text)

for i in range(len(text)):
    if text[i]!=",":
        p=p+text[i]
    else:
        if a!=0:
            A.append(p)
            a=0
        if k!=0:
            K.append(p)
            k=0
        p=""
    if text[i]=="A" or text[i]=="a":
        a=a+1
    if text[i]=="K" or text[i]=="K":
        k=k+1
print(A)
print(K)
z=open("Aharfli","w")
for i in A:
   z.write(i)
   z.write(",")
z.close()   
z1=open("Kharfli","w")
for i in K:
   z1.write(i)
   z1.write(",")
z1.close()   

'''


  


# MORSE={"-----":"0",
#          ".----":"1",
#          "..---":"2", 
#          "...--":"3",
#          "....-":"4",
#           ".....":"5", 
#           "-....":"6", 
#           "--...":"7", 
#           "---..":"8", 
#           "----.":"9"}

# n=str(input("Belgilar kiriting: "))
# n=n.split(" ")
# for j in n:
#     for i in MORSE:
#         if j==i:
#             print(MORSE[i],end="")
# print()
