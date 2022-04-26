'''
  # juftlarni kamayish tartibida chiqarish
n=int(input("n="))
print("juftlar: ")
for i in range(n,1,-1):
   if i%2==0:
    print(i)

    # toqlarni kamayish tartibida chiqarish
n=int(input("n="))
print("toqlar: ")
for i in range(n,1,-1):
    if i%2!=0:
        print(i)  
        
        # Barcha xonali sonlarni tub sonlarni topish

n=10
son=100
print("Barcha ikki xonali sonlarni tubuni topish")
for num in range(n,son):
    if num>1:
        for i in range(2,num):
            if(num%i==0):
                break
        else:
            print(num,end=" ")
print()                
'''
  #%% 6-masala
n=int(input("n= "))
for i in range(n+1):
    for t in range(n-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("* ",end="")
    print()      



    