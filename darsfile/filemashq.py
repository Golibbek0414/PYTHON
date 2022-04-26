


#%% 1 2 masala
'''with open('ikki.txt') as file:
    pi=file.read()
print(pi)  
s=0
k=0
for i in range(len(pi)):
    if pi[i].isalpha():
        s+=1
    elif pi[i].isdigit():
        k+=1
print(s,k)  
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
#%%
'''with open('to.txt') as file:
    pi=file.read()
#print(pi)     
for i in pi:
     a=i.split(",")
print(a)'''

     

