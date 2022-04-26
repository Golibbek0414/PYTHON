# n=int(input("n="))
# z=0;y=0
# while z!=1:    
#     k=0; a=0; c=0
#     ls = []
#     q = n
#     while n>1:
#         ls.append(int(n%10))
#         k+=1
#         n /=10
#     b = int(k/2)
#     for i in ls:
#         a+=i*(10**(k-1))
#         k-=1
#     for i in range(b):
#         if ls[i]==ls[k-i-1]:
#             c+=1
#     if c==b:
#         print(q,"=>",y,q)
#         z+=1
#     else:  
#         n=a+q
#         y+=1

# 5 - masala qisqasi
n = input(); start = int(n)
s = ''; k = 0
s += n[::-1]
while(1):
    if int(n) == int(s):
        print(start,'==>',k,n)
        break
    else:
        n = str(int(n) + int(s))
        s = ''; s += n[::-1]
        k += 1