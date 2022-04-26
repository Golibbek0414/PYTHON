#%% LIST
l1=[]  # bo'sh list e'lon qilish
l3=[1,2,3,4,5,6,7,8,9,10]
print(l3,type(l3))
l4=[123,3/1234,True,'salom',19,False,'hayr']
print(l4)
l5=list([1,2,3,4,5,6,7,8,9])
print(15)
for i in l5:
    print(i)
for i in range(len(l4)):
    print(i,l4[i])
#%% List function append and insert
ls1=[1,20,'salom',3.124,True]
ls1.append(123456789) # listning oxiriga qiymat qo'shish
print(ls1)
ls1.insert(0,"hello")  # 0- indexga qo'shish
print(ls1)
ls1.insert(2,-122) # 2- indexga qo'shish
print(ls1)
#%% List funtion pop and remove
ls1=[1,20,'salom',3.1234,True]
ls1.pop() # oxirgi elementni o'chirish
print(ls1)
ls1.pop(0)   # 0 - indexdagi elemetni o'chirish
print(ls1)
ls1.remove('salom')  #  qiymati bo'yicha o'chirish
print(ls1)
#%% List function count, index,sort, reverse
ls10=[1,2,3,4,5,6,7,8,9]
print(f"{1} qiymati {ls10.count(1)}ta") 
print(f"{5} qiymati {ls10.count(5)}ta")
# count qiymat nechi marta takrorlangaligini aniqlaydi
ls11=[1,'salom',3.12345]
print(ls11.index(3.12345))  # qiymatining indexini chiqarish
ls10.sort() # list elementlarini o'sish tartibida sortlash
print(ls10)
  # kamayish tartibida
print(ls10)
ls10.reverse()  # listni teskarisiga saqlash
print(ls10)
#%%  sort
ls12=['salom','aziza','Sardor','malika']
ls12.sort()
print(ls12)
print(ls12[0][::-1])
text='Sardor'
ls=[*text]
ls.sort()
print(ls)
ls13=[3.123,1000,-234,True,1,False, 0, 75]
ls13.sort()
print(ls13)
#%% clear, copy
ls12=['salom','aziza',"Sardor",'malika','azi','david']
new=['salom','aziza',"Sardor",'malika','azi','david']
new.clear()   # tozalash
print(new)
l3=[3.1123,100,-234,False,True,1,0]
new=ls13.copy()
print(new)
new=list(ls12)
print(new)