davlatlar=["Uzbekiston","Qatar","Tojikiston","Turkmaniston","Turkiya","Amerika"]
print(davlatlar)
uzunlik=len(davlatlar)  # len metodi uzunligini aniqlaydi
print(uzunlik)
davlatlar.sort()   # sort metodi ASCII kod bo'yicha tartiblaydi
print(davlatlar)
davlatlar.sort(reverse=True)  # reverse metodi oxiridan boshlab chiqaradi
print(davlatlar)
print(sorted(davlatlar))      # sorted metodi faqat consolda o'zgartiradi asl qiymat o'zgarmaydi
print(sorted(davlatlar,reverse=True)) # reverse oxirida boshla chiqaradi asl qiymat o'zgarmaydi
juft_sonlar=list(range(120,1200,2))
print(juft_sonlar)
yigindi=sum(juft_sonlar)
print(yigindi)