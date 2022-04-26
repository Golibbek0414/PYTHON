
'''#%% File o'qish
with open('pi.text') as file:
    pi=file.read()
print(pi)    
print(type(pi))
pi=pi.rstrip()   # qator oxiridagi bo'sh joyni olib tashlaydi
pi=pi.replace("\n",'')  # \n ni topib qo'shtirnoq ichidagi belgiga almashtiradi
pi=int(pi)
print(pi)
print(type(pi))

filename='pi.text'
#with open(filename) as file:
#   for line in file:
#       print(line)
with open(filename) as file:
    talabalar=file.readlines()
print(talabalar)
talabalar=[talaba.rstrip()for talaba in talabalar] # bir qator for ishlatdik oxirgi qatorini yani \n ni olib tashladik 
print(talabalar)       
print(type(talabalar))'''
#%% File yozish
faylnomi='new_file.txt'
ism="Olimjon Karimov"
tyil=2003
with open(faylnomi) as fayl:
    fayl.write(ism+'\n')
    fayl.write(str(tyil)+'\n')
faylnomi='new_file.txt'
with open (faylnomi,'a') as fayl:
    fayl.write('Alijon Valeyev\n')
    fayl.write('2000')
#%% Binaryfile o'qish
import pickle
talaba1={"ismi":"hasan","familya":"valiyev","tyil":2003,'kursi':2}
talaba2={"ismi":"alijon","familya":"husanov","tyil":2004,"kursi":1}
with open("info.pkl",'wb') as file:
    file.dump(talaba1,file)
    file.dump(talaba2,file)
#%%  Binaryfile read 
import pickle
with open("info.pkl",'rb') as file:
    talaba1=pickle.load(file)
    talaba2=pickle.load(file)
print(talaba1)
print(talaba2)                