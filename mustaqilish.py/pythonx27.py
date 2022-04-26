'''
# a ga belgi kiritadi b ga belgi kiritdadi shular orasidagi so'zni chiqarish
text=input("Text kiriting: ")
A=input("A=")
B=input("B=")
i1=text.index(A)
i2=text.index(B)
print(text[i1+1:i2])

'''

'''
 # eng ko'p harfni va eng uzun so'zni chiqarib beradi
matn=input("Matn kiriting: ")
lst=list()
lst2=list()
s=''
for i in matn:
    if i==' ' or i=='.':
        lst.append(s)
        s=''
    elif i==matn[-1]:
        s+=i
        lst.append(s)
        s=' '
    if i!=' ' or i!='.':
        s+=i
for i in lst:
    lst2.append(lst.count(i))
print("Eng ko'p takrorlangan so'z: "+lst[lst2.index(max(lst2))])
imax=''
for i in lst:
    if len(i)>len(imax):
        imax=i
print("Eng uzun so'z: ",imax)



'''

#  File A bilan boshlangan komlarni metod2 ga metod1 ga videokarta bilan borlari chiqadi
def Method1(lst):
    for i in lst:
        if "videokarta" in i:
            print (i)
def Method2(lst):
    for i in lst:
        if i[0]=='A' or i[0]=='a':
            print (i)

with open("Kompyuter","w") as f:
    f.write("Acer, videokarta, protsessor, operativka, monitor, 10\n")
    f.write("Mac, videokarta, protsessor, operativka, monitor, 20\n")
    f.write("Lenovo,protsessor, operativka, monitor, 30\n")
    f.write("asus, protsessor, operativka, monitor, 40\n")
    f.write("Hp, protsessor, operativka, monitor, 50\n")
    f.write("Samsung, videokarta, protsessor, operativka, monitor,60\n")
    f.write("LG, protsessor, operativka, 70\n")
    f.write("IBM, videokarta, protsessor, operativka, monitor,80\n")
    f.write("Dell, protsessor, operativka, monitor, 90\n")
    f.write("Acer, protsessor, operativka, monitor, 100\n")
lst=list()
with open("Kompyuter","r") as p:
    for i  in range(0,10,1):
        lst.append(p.readline())
# print(lst)
print("----------------------------------")
print("Method1: ")
Method1(lst)
print("----------------------------------")
print("Method2: ")
Method2(lst)





'''
dict={}
l=''
N=int(input("N="))
for i in range(1,N+1,1):
    l=input()
    dict[i]=l
    l=''
for i in range(1,N+1,1):
    if dict[i].isdigit():
        dict.pop(i)
print(dict)
asd=list()
for i in dict:
    pp=dict[i]
    ll=i
    for j in dict:
        if dict[j]<pp and dict[j] not in asd:
            pp=dict[j]
            ll=j
        else:
            for j in dict:
                if  dict[j] not in asd:
                    pp = dict[j]
                    ll = j

    print(ll,pp)
    asd.append(pp)
    pp=""
    '''
