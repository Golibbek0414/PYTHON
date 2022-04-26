ls=[1,2,3,4,5,6,7]
ls1=[]
ls2=[]
for i in ls:
    if i%2==0:
        ls1.append(i)

    else:
        ls2.append(i)
ls1,ls2=ls2,ls1
print(ls1,ls2)