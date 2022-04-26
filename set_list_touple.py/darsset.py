'''
list=[2,1,5,2,8,4,1,8,7,6,6]
a = set(list)
print(a)
a.add("apple")   # o'ziga parametr sifatida bitta qiymat qabul qiladi qabul qilingan ma'lumotni set ichiga qo'shadi
a.remove("a")   # set ichidagi biron bir ma'lumot qabul qiladi va ushbu kiritilgan ma'lumotni o'chirib yuboradi agar kiritilgan ma'lumot set ichida bo'lmasa xatolik beradi
a.descard("as")  # set ichidagi biron bir ma'lumot qabul qiladi va ushbu kiritilgan ma'lumotni o'chirib yuboradi agar kiritlgan ma'lumot set ichida bo'lmasa xatolik bermaydi
a.clear()  # set ichidagi ma'lumotlarni o'chirib yuboradi
a=a.union({1,2,3,4}) # o'ziga parametr sifatida set qabul qiladi va qabula qilingan ma'lumotni oldingi set bilan birlashtiradi
print(a)

a={"apple","IBM","Dell","hp"}
b={"Lenovo","acer","asus",'apple','hp'}
b=a.intersection(b) # set ichidagi bir xil qiymatli elementlarni chiqarib beradi
print(b)
print("apple"in a) # tekshirishini tiger deb nomlanadi
a=[1,2,3,4,5,6,7]
for i, value in enumerate(a):
    print(i,"-",value)
    
cars=["bmw",'tiko',"nexia",'01','01','07']
print(len(list(set(cars)))) 
s1={1,2,True,False,'salom','dunyo',3,4,5,8,9}
#s1.add(int(input("son="))) 
#print(s1)  
s2={1,8,9,10}
s3=s1.difference(s2)
print(s3)
'''
a=(1,2,3,4,5)

a=list(a)
print(type(a))

