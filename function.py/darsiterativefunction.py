#%% iterative function
def juft(sonlar):
    for i in sonlar:
        if i%2==0:
            print(i,end=" ")
ls=[1,2,3,4,5,6,7,8,9,10]
juft(ls)
print()    
#%% Recursive
def fact(n):
    if n==0:
        return 1
    elif n>0:
        return n*fact(n-1)
print("5!=",fact(5)) 
print()     
#%% 
def teskari(n):
    if n>0:
        print(n,end=" ")
        teskari(n-1)
teskari(10) 
print()       
def togri(n):
    if n>0:
        togri(n-1)
        print(n,end=" ")
togri(10)        
