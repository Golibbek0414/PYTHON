

'''
f = open("zopark.txt","r")
new = f.readlines()
lst1 = []; lst2 = []; k = 0; dict1 = {}
for i in new:
    a = i.split(",")
    s = a[2]    
    d = a[1]
    lst1.append(s)
    lst2.append(d)
lst3=[]    
for i in (lst1,lst2):
    lst3.append(i)
print(lst3) 
k=lst3.sort()
print(k)
'''
# Infoc = open("zopark.txt","r")
# ls1 = []
# s1 = str()
# for i in Infoc.readlines():
#     x = i.split(',')
#     a = x[-3]
#     if a[0] == 'A' or a[0] == 'B' or a[0] == 'C' or a[0] == 'D' or a[0] == 'E' or a[0] == 'F' or a[0] == 'G' or a[0] == 'H':
#         if len(x)== 5:
#              s1 = s1 + x[0] +' '+ x[1]
#         elif len(x) == 6:
#              s1 = s1 + x[0]+x[1]+' '+ x[2]
#     if len(s1)>0:
#         ls1.append(s1)
#     s1 = str()
# ls1.sort()
# print(*ls1,sep="\n")
with open("zopark.txt","r") as f:
    zoo=f.readlines()
temp=list()
for i in zoo:
    if i[0]=="\"":
        x=i.split(",")
        temp.append(x[2])
    else:
        x=i.split(",")
        temp.append(x[1])
temp=list(set(temp))
temp.sort()
for i in temp:
    for j in zoo:
        if j[0] == "\"":
            x = j.split(",")
            if i == x[2]:
                print(x[0],x[1])  
        else:
            x=j.split(",")
            if i==x[1]:
                print(x[0])