'''
a=int(input("a="))
b=int(input("b="))
ls1=[]
s=1
for num in range(a,b):
    if a%2==0:
     
     ls1.append(a)
    a+=1
print(ls1)   
# 2 masala
print("2 masala")
a=int(input("a="))
b=int(input("b="))
ls1=[]
s=1
for num in range(a,b):
    if a%2!=0:
     
     ls1.append(a)
    a+=1
ls1.reverse()
print(ls1)

list1=['salom',123,True,'Hayr','world',3,'7214']
text=[]
for i in list1:

    if type(i)==str:
        text.append(i)
    
print(text)   
text.sort()
print(text)
other=[] 
for i in list1:
    if type(i)!= str:
        other.append(i)

other.sort(reverse=True)
print(other)


list=['salom']
a=len(list) 
if a==0:
    print("bo'sh")
elif a!=0:
    print("bo'sh emas")
'''
'''
ls1=[1,3,5,7,9,10]
ls1.pop()
ls=[2,4,6,8]
ls3=ls1+ls
print(ls3)
'''


'''
ls=[1,2,3,4]
ls1="emp"
ls2=[]
for i in ls:
    ls2+=[ls1+str(i)]
print(ls2) 
'''
'''
ls=[3,4,0,0,5,6,1,2,0,0,3,4] 
a=[]
b=[]
for i in ls:
    if i==0:
        a.append(i) 
    else:
        b.append(i)  
print(b+a)   
'''
from cProfile import label


l1=[1,2,3]
l2=[4,5,6]
l3=[10,11,12]
l4=[13,14,15]
max=(l1,l2,l3,l4)
print(max)


 
        








      

     
    
  

    

    
