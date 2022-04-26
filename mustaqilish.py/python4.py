text='salom qish. Imtihon zo\'r o\'tdi'
print(text)
text="Salom Qish. Imtihon zo'r o'tdi"
print (text)
text="""   Salom Foundation '29'
            Imtihon natijalari "zo'r" o'tdi
            Hamma hursand"""
print(text)
text='Salom'
print(*text)   # probel tashlash
print(text*5)
print(text[0],text[1],text[2],text[3],text[4]) # har bir indeksni o'qish
print(text[-1],text[-2],text[-3],text[-4])     # teskari tartibda o'qish
print(len(text))    # uzunligini aniqlash
# [start : finish : step]
matn="Salom bolalar"
print(matn[0:5:1])  # 0- indeksdan 5- indeksgacha 1 qadam
print (matn[5:])    # 5- inkeksdan oxirigacha
print(matn[1:10:2])  # toq indeks
print(matn[:5])      # boshidan boshlab 5 indeksgacha chiqarib beradi
print(matn[::-1])    # kiritgan ma'lumotni oxiridan boshigacha chiqarib beradi
# matn[0]='K' 
number="12345678910"
print(*number[0:10:2])
