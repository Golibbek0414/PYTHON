# # a dan b sonigacha juft sonlarni to'g'ri tartibda listga joylashtirish
# # 1-masala
# print("1 masala")
# a=int(input("a="))
# b=int(input("b="))
# ls=[]
# for i in range(a,b):
#     if i%2==0:
#         ls.append(i) 
# print(ls)
# # a dan b sonigacha toq sonlarni teskari tartibda listga joylashtirish
# # 2 masala
# print("2 masala")
# a=int(input("a="))
# b=int(input("b="))
# ls=[]
# for i in range(a,b):
#     if i%2!=0:
#         ls.append(i)
# ls.sort(reverse=True) 
# print(ls)       
# # 3 masala
# ls=["salom",123,"True","Hayr",'world',3.232,'76543']
# text=[]
# other=[]
# for i in ls:
#     if type(i)==str:
#         text.append(i)
#     else:
#         other.append(i)
# text.sort()
# other.sort(reverse=True)            
# print(text)
# print(other)

# agar ikkita elementning yig'indisi kiritilga son teng bo'lsa shu elementlarning ideksini ekranga chiqaring
# ls1=[1,2,33,4,5,6,7,8,9]
# n=int(input("sonni kiriting: "))
# for i in range(len(ls1)):
#       for j in range(i+1,len(ls1)):  
#          if ls1[i]+ls1[j]==n:
#              print(i,j)  

# input orqali gap kiritiladi shu gapda so'zlarni bosh harfini orqali alfabit tartibida chiqarish kerak
# text=input("Textni kiriting: ")
# sozlar=[]
# for i in text.split():
#     sozlar.append(i)
# sozlar.sort()
# print(*sozlar)    

#  kiritilgan gapdagi toq uzunlikdagi so'zlarni teskarisiga yozilsin juft uzunlikdagilari esa shundoq qolsin
# text=input("Textni kiriting: ")
# text1=str()
# for i in text.split():
#     if len(i)%2!=0:
#         text1+=i[::-1]
#     else:
#         text1+=i+" "
# text=str(text1)
# print(text1)     
  
  # kiritilgan sondan kiyingi 5 ta tub son topish
# n=int(input("sonni kiriting: "))
# print("Kattaroq tub sonlar:",end='') 
# num=n+1
# s=0
# while True:
#     for i in range(2,num-1):
#         if num%i==0:
#             break
#     else:
#             print(num,end=' ')
#             s+=1
#             if s==5:
#                 break
#     num+=1
# print(num)            


# Foydalanuvchi so'z va harf kiritadi agar kiritilgan harf so'zda bo'lsa usha o'sha harfni kattaga almashtirish
# text=input("textni kiriting: ")
# harf=str(input("harf kiriting: "))
# text1=str()
# for i in text:
#     if i==harf:
#         text1+=i.upper()
#     else:
#         text1+=i 
# print(text1)          

 # n gacha bo'lgan sonlar yig'indisini toping

n=int(input("n="))
s=0
for i in range(1,n):
    print("2"*i,end="+")
    s+=int("2"*i)
s+=int("2"*n) 
print("2"*n,"=",s)   