#%% in function
text="Salom"
if 't' in text:
    print("bor")
else:
    print("yo'q")
matn="Salom dasturnchilar ishlar qalay" 
if 'dastur' in matn:
    print("dastur bor")
else:
    print("dastur yo'q")
#%% while
k=0
while 1:
    k+=1
    if k==4 or k==6:
        continue
    print('salom',k)
    if k==10:
        break
#%%  while
son=int (input("son= "))
while son!=0:
    print(son%10,end=" ")
    son//=10
print()
#%% for 
text="Salom FOUndation"
for i in text:
    print(i,end=" ")
print()
#%% renge(begin, end, step)
for i in range (1,10,1):
    print(i) 
for t in range(0,len(text),2):
    print(text[t],end=" ")
print()
for i in range(10,0,-1):
    print(i,end=" ")
print()                                        