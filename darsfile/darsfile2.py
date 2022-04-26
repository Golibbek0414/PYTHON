#%% File wrtie
f=open("first","w")
text="Foundation 29 imtihon yaqin\n"
a=123
b=3.14
d=True
f.writelines(text)
f.write(str(a)+" "+str(b)+" "+str(d))
f.writelines("""\nSalom
      Hello
      world""")
f.writelines(["\nsalom","\nhayr","\nalvido"])
f.close   
#%% File read
with open("first","r") as t:
    text=t.read(2)
    print(t.tell())
print(text)
#%% File readline
with open("first","r") as fp:
    matn=fp.readline()
    matn=fp.readline()
print(matn)    
#%% File readlines
with open("first","r") as d:
    st=d.readlines()
new=list()
for i in range(len(st)):
    st[i]=st[i].reaplace("\n","")
print(st)    