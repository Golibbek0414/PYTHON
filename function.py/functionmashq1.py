#%% 1-masala
def tub(son):
    k=0
    for i in range(2,son//2+1):
        if son%i==0:
            k+=1
    if k==0 and son>1:
        print(son,"tub son")
    else:q
        print(son,"tub son emas")
tub(int(input("son= ")))
#%% 2-masala
def togri(son):
    if son!=0:
        togri(son//10)
        print(son%10,end=" ")
togri(int(input("son= ")))
#%% 3-masala
def teskari(son):
    if son!=0:
        print(son%10,end=" ")
        teskari(son//10)
teskari(int(input("son= ")))