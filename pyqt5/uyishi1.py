
                #  uy ishi 1
# from PyQt5.QtWidgets import QApplication,QWidget
# from PyQt5.QtWidgets import QLabel,QLineEdit,QPushButton
# from PyQt5.QtGui import QFont
# import sys
# app=QApplication(sys.argv)
# oyna=QWidget()
# oyna.setWindowTitle("Mening birinchi dasturim")
# oyna.setGeometry(200,200,800,600)

# ism=QLabel(input("Isminigzni kiriting: "),oyna)
# ism.move(10,50)
# ism.setFont(QFont("Times",20))

# fam=QLabel(input("Familiyanizni kiriting: "),oyna)
# fam.move(260,50)
# fam.setFont(QFont("Times",20))

# sharf=QLabel(input("Sharifingizni kiriting: "),oyna)
# sharf.move(510,50)
# sharf.setFont(QFont("Times",20))
# oyna.show()
# sys.exit(app.exec_())






            # uy ishi 2
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtWidgets import QLabel,QLineEdit,QPushButton,QMessageBox
from PyQt5.QtGui import QFont
import sys
app=QApplication(sys.argv)
oyna=QWidget()
oyna.setWindowTitle("Mening birinchi dasturim")
oyna.setGeometry(200,200,800,600)
ism1=input("Isminigzni kiriting: ")
fam=input("Familiyangizni kiriting: ")
tyil1=(input("tug'ulgan yilni kiriting: "))
button1=QPushButton("ism",oyna)
button1.setFont(QFont("Times",20))
button1.move(50,120)
def fun1():
    win=QMessageBox(ism)
    win.setWindowTitle("Ma'lumotlaringiz!")
    win.setFont(QFont("Times",20))
    
    win.setText(ism1)
    win.show()
button1.clicked.connect(fun1)   # Button bu bosiladigan tugma ya'ni biz bilgan ok 
button2=QPushButton("familiya",oyna)
button2.setFont(QFont("Times",20))
button2.move(300,120)
def fun2():
    win=QMessageBox(ism)
    win.setWindowTitle("Ma'lumotlaringiz!")
    win.setFont(QFont("Times",20))
    
    win.setText(fam)
    win.show()
button2.clicked.connect(fun2)

button3=QPushButton("tug'ulgan yil",oyna)
button3.setFont(QFont("Times",20))
button3.move(550,120)
def fun3():
    win=QMessageBox(ism)  # oyna ichida oynacha yaratib chiqaradi
    win.setWindowTitle("Ma'lumotlaringiz!")
    win.setFont(QFont("Times",20))
    
    win.setText(tyil1)
    win.show()
button3.clicked.connect(fun3)

ism=QLabel("",oyna)
ism.move(10,50)
ism.setFont(QFont("Times",40))
oyna.show()
sys.exit(app.exec_())


 

#                 # uy ishi 3
# from tkinter import *

# from click import command

# def qoshish():
#     son1=int(Entry1.get())
#     son2=int(Entry2.get())
#     qoshish_son=son1+son2
#     label4.configure(text="{0}".format(qoshish_son))
# def ayirish(): 
#     son1=int(Entry1.get())
#     son2=int(Entry2.get())
#     ayirish_son=son1-son2
#     label4.configure(text="{0}".format(ayirish_son))
# def kopaytirish():
#     son1=int(Entry1.get())
#     son2=int(Entry2.get())
#     kopaytirish_son=son1*son2
#     label4.configure(text="{0}".format(kopaytirish_son))
# def bolish():
#     son1=int(Entry1.get())
#     son2=int(Entry2.get())
#     bolish_son=son1/son2
#     label4.configure(text="{0}".format(bolish_son))
# def qoldiq():
#     son1=int(Entry1.get())
#     son2=int(Entry2.get())
#     qoldiq_son=son1%son2
#     label4.configure(text="{0}".format(qoldiq_son))
# def daraja():
#     son1=int(Entry1.get())
#     son2=int(Entry2.get())
#     darja_son=son1**son2
#     label4.configure(text="{0}".format(darja_son))
# Calc=Tk()
# Calc.title("Birinchi kalkulyator")
# Calc.geometry("800x500")
# label1=Label(text="1 sonni kiriting")
# label2=Label(text="2 sonni kiriting")
# Entry1=Entry()
# Entry2=Entry()

# Button1=Button(text="+",command=qoshish )
# Button2=Button(text="-",command=ayirish)
# Button3=Button(text="x",command=kopaytirish)
# Button4=Button(text="/",command=bolish)
# Button5=Button(text="%",command=qoldiq)
# Button6=Button(text="^",command=daraja)
# label3=Label(text="Javob")
# label4=Label(text="0")

# label1.place(x=10,y=40)
# label2.place(x=10,y=80)

# Entry1.place(x=150,y=40)
# Entry2.place(x=150,y=80)

# Button1.place(x=10,y=120)
# Button2.place(x=50,y=120)
# Button3.place(x=90,y=120)
# Button4.place(x=150,y=120)
# Button5.place(x=190,y=120)
# Button6.place(x=230,y=120)
# label3.place(x=10,y=160)
# label4.place(x=60,y=160)

# Calc.mainloop()