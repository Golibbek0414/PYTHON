'''
        # Aylananing uzunligini aniqlash
radus=15
PI=3.14
diametr=2*radus
print("Aylananing uzunligi=",PI*diametr)

        # matn yaratish
ism=(input("Ismingizni kiriting:"))
yosh=int(input("Yoshingizni kiriting:"))
xabar= ism + ' ' +str(yosh) +' ' 'yoshda'
print(xabar)

       # Yoshini topish
t_yil =int(input("Tug'ulgan yilinizni kiriting: "))
yosh = 2022-t_yil 
print("Siz",yosh,"yoshda ekansiz")

       # tug'ulgan yilini topish 
yosh=int(input("Yoshingizni kiriting: "))
t_yil=2022-yosh
print("Siz",t_yil,"yilda tug'ulgansiz") 
 
 
 # stringlar bilan ishlash


mevalar=["olma","anor"]
print(mevalar[0].title())      # ideksdagi elementni bosh harfini katta qilib chiqaradi masalan olma bo'lsa Olma chiqaradi
print(mevalar[1].upper())   # elementlarini katta harfga o'giradi
mevalar.append("tarvuz")       # append metodi qo'shish bu oxirgi elementiga qo'shadi
print(mevalar)
mevalar.insert(0,"banan")     # insert metodi ma'lumot qo'shish 
print(mevalar)
mevalar.insert(3,"ananas") # insert 3 indeksga ma'lumot kiritish
print(mevalar)
 # mashinalar bilan ishlash


cars=[]
cars.append("Kia")  # append bu bo'sh joyga ma'lumot kiritish
cars.append("Nexia")
cars.append("Malibu")
print(cars)
del cars[0]     # ma'lumotni o'chirish
print(cars)
cars.insert(0,"Trikker")  # ma'lumot kiritish
print(cars)
cars.remove("Malibu")   # kiritgan ma'lumotingizni o'chirish
print(cars)


 # boz
   
bozorlik=["un","yog'","go'sh","makaron"]
mahsulot=bozorlik.pop(1) # pop metodi ma'lumot ichidagi ma'lumotlarni boshqa tempga ko'chirish 
print("Men " + mahsulot + "sotib oldim") 
print("Sotib olmagan mahsulotlarim",bozorlik)
mahsulot2 = bozorlik.pop()  # pop metodiga indeks kiritmasak oxirgi elementi olib qo'yadi
print(mahsulot2)
'''
