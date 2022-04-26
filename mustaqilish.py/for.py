mehmonlar=["Ali","Vali","Hasan","Husan","Eshmat"]
for mehmon in mehmonlar:
    print("Salom",mehmon)
insonlar=["Davlat","Humoyin","Dilshod","Anvar"]
for taklif in insonlar:
    print(f"Hurmatli {taklif},sizni 9-fevral kuni kutub qolamiz\n")
    print("Hurmat bilan, Foundation29 a'zolari\n")    
sonlar=list(range(1,11))
for son in sonlar:
    print(f"{son} ning kvadrati {son**2} ga teng\n") 
    print(f"{son} ning ko'pi {son**3} ga teng\n")   
sonlar=list(range(11)) # sonlar degan faylga 0 dan 11 gacha sonlar bilan to'ldiradi
son_kvadrat=[] # bo'sh fayl ochib oldik
for son in sonlar:
    son_kvadrat.append(son**2)
print(sonlar)
print(son_kvadrat)
dostlar=[] # bo'sh ro'yxat yaratib oldik
print("5 ta eng yaqin do'stingizni kiriting:\n")
for n in range(5):    #  n bu yerda 0 dan 5 gacha qiymat oladi
    dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting:\n"))
print(dostlar)    
