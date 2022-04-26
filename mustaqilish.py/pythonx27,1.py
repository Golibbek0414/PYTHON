
'''
# File input orqali son kiritadi shuni kun soat minut sekundda topish
time=(input("vaqtni kiriting: "))
with open("vaqt","w") as f:
    f.write(time)   
with open("vaqt","r") as f:
    time=f.read()  
time1=int(time)          
kun=time1//(24*3600)
time1=time1%(24*3600)
soat=time1//3600
min=time1%3600//60
sekund=time1%3600%60
print(f"kun={kun},soat={soat},minut={min},sekund={sekund}")  
'''

qatorsoni=sum(1 for line in open('Talaba'))
with open("Talaba","r") as d:
 print("Method 1")
 for i in range(0,qatorsoni):
     qator=d.readline()
     p=0
     for i in range(len(qator)):
         if qator[i]=='.':
             p=i
             break
     p=p+1
     if (qator[p]=='0' and (qator[p+1]=='1' or qator[p+1]=='2')) or (qator[p]=='1' and qator[p+1]=='2'):
         print(qator,end="")
qatorsoni = sum(1 for line in open('Talaba'))
with open('Talaba', "r") as d:
    print("Method 2")
    for i in range(0,qatorsoni):
        qator=d.readline()
        p=0
        for i in range(len(qator)):
            if qator[i]==' ':
                p=i
        p = p + 1
        if qator[p]=='2':
            print(qator,end="")
'''
# funksiya parametri sifatida string ushbu stringda nechta raqamdan iborat
def string(temp):
    s=0
    for i in temp:
        if i.isdigit():
            s+=1
    print(f"kiritilgan matnda {s} ta raqam qatnashgan")
string(temp=input("matn kiriting= "))                   

'''

