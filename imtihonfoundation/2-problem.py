son= int(input("Son kiriting: "))
temp= str(son)
list1=[]
show=[]
for i in range(0, len(temp)):
    h=int(temp[i])
    list1.append(h)
for i in range(0, len(list1)):
    foo=0
    for j in range(0, len(list1)):
        if i!=j:
            if list1[i]>list1[j]:
                foo=foo+list1[i]-list1[j]
            else:
                foo=foo+list1[j]-list1[i]
    show.append(foo)
print(show)
print(min(show))