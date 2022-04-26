'''
#%% String
text="Salom bolalar ishlar qalay"
print(*text) # textni ajratib chiqarib beradi masalan Salom so'zini S a l o m qilib textda kiritgan barchasi
print(text*2) # textdagi ma'lumotlarni ikkita dan chiqaradi
print(len(text))   # uzunligini chiqarib beradi
print(text[0:5:1])  # 0 indeksdan 5 indeksgacha 1 qadam
print(text[14:20:1]) # natijasi ishlar chiqadi
print(text[0:])  # 0 indeksdan oxirigacha chiqadi
print(text[0:26:2])   # juft indeksdagi ma'lumotlarni chiqarib beradi
print(text[1:26:2])   # toq indeksdagi ma'lumotlarni chiqarib beradi
print(text[:26])  # 0 indeksdan 26 indeksgacha ma'lumotlarni chiqarib beradi
print(text[::1])  # bunda 0 indeksdan oxirigacha 1 qadmda ma'lumotlarni chiqarib beradi
print(text[::-1]) #  textga kiritgan ma'lumotni teskari tartibda chiqarib beradi
#%% Iput orqali ma'lumot kiritish
a=int(input("a=")) #int tipiga oid butun son kiritamiz
print(a,type(a))   
b=float(input("b=")) # float tipiga oid haqiqiy son kiritamiz
print(b,type(b))
c=bool(input("c="))
print(c,type(c))

#%%
from this import d


matn="Salom dasturlchilar ishlar qalay"
if "dastur" in matn:
    print("bor")
else:
    print("yo'q")    
#%% while
k=0
while 1:
    k+=1
    if k==4 or k==6:
        continue
    print(k,end=" ")
    if k==10:
        break
print()      
#%% kiritilgan sonni teskari tartibda chiqarish
son=int(input("son="))
while son!=0:
    print(son%10,end=" ")
    son//=10
#%% kirtilgan sonni xonalarini kamaytirish
son=int(input("son="))
while son!=0:
    son%10
    son//=10
    print(son)  
    '''
    '''
#%%  For loop
matn="Salom Foundation a'zolari ishlar qalay" 
for i in matn:
    print(i,end=" ")  
print()
#%%  range ishlatish
text="salom dunyo"
for i in range(0,len(text),2):
    print(text[i])    
print()
for i in range(12,0,-1):
    print(i,end=" ")    
'''

