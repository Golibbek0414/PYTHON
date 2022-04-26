
cars=["malibu","kia","trekker","audi","mers"]
cars.sort()   # sort metodi ASCII kod  bo'yicha tartiblab beradi
print(cars)
cars.sort(reverse=True)  # teskari tartiblash
print(cars)
print(sorted(cars))  # sorted bu faqat consol oynasida tartiblab beradi asl qiymat o'zgarmaydi 
print(sorted(cars,reverse=True)) # teskari tartibda consolga chiqarib beradi
sonlar=[1,2,3,4,54,65,-7,0,-77,7456]
sonlar.sort() # sortlash
print(sonlar)
sonlar.sort(reverse=True) # teskari tartibda tartiblash
print(sonlar)
print(sorted(sonlar))
print(sorted(sonlar,reverse=True))
len(cars)            # uzunligi hisoblaydi
print(cars)
uzunlik=len(sonlar)
print(uzunlik)
sonlar=list(range(0,10))
print(sonlar)
toq_sonlar=list(range(1,21,2))
print(toq_sonlar)
max_qiymat=max(sonlar)
print(max_qiymat)
min_qiymat=min(toq_sonlar)
print(min_qiymat)
narhlar=[1234,2345,123456,1234567,123456789,12345678,1234567890]
arzon=min(narhlar)
qimmat=max(narhlar)
jami=sum(narhlar)
print("Eng arzon narh",arzon,". Eng qimmat narh",qimmat,". Jami narh",jami)
print(narhlar[0:4])
narhlar.remove(123456)   # remove ga kiritilgan qiymatni o'chirish
print(narhlar)
my_narhlar=narhlar[:]      # nusxalash
my_narhlar=narhlar[1:7:2]
print(my_narhlar)
my_narhlar.remove(1234567890)
print(narhlar)
print(my_narhlar)




