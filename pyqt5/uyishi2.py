
                         # uy ishi 3
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtWidgets import QLabel,QPushButton,QComboBox,QMessageBox
from PyQt5.QtGui import QFont
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QComboBox")
        self.setGeometry(150,150,2000,1000)
        self.start()
    def font(self,ob,x,y):
        ob.setFont(QFont("Times",25))
        ob.move(x,y)
    def start(self):
        name=input("Ismingizni kiriting: ")

        self.ism=QLabel("Ismingizni kiriting.",self)
        self.font(self.ism,50,10)
        self.ismi=QComboBox(self)
        self.font(self.ismi,100,60)
        self.ismi.addItems(["",name])

        surname=input("Familiyangizni kiriting: ")
        
        self.fam=QLabel("Familiyangizni kiriting",self)
        self.font(self.fam,50,110)
        self.familiya=QComboBox(self)
        self.font(self.familiya,100,160)
        self.familiya.addItems(["",surname])

        self.province =QLabel("Qaysi viloyatda tug'ulgansiz",self)
        self.font(self.province ,50,210)
        self.viloyat=QComboBox(self)
        self.font(self.viloyat,100,260)
        self.viloyat.addItems(["","Toshkent shahar"])

        self.region =QLabel("Qaysi tumanda tug'ulgansiz",self)
        self.font(self.region ,50,310)
        self.tuman=QComboBox(self)
        self.font(self.tuman,100,370)
        self.tuman.addItems(["","Chilonzor tumani","Yunusobod tumani","Serg'ali tumani","Shayhontohir tumani"])
        
        nation=input("Millatingizni kiriting: ")
        
        self.millat=QLabel("Millatingizni kiriting",self)
        self.font(self.millat,50,420)
        self.millat=QComboBox(self)
        self.font(self.millat,100,470)
        self.millat.addItems(["",nation])


        self.jins=QLabel("Jinsingizni kiriting",self)
        self.font(self.jins,50,520)
        self.gender=QComboBox(self)
        self.font(self.gender,100,570)
        self.gender.addItems(["","Erkak","Ayol"])
        ok=QPushButton("OK",self)
        self.font(ok,50,640)
        self.yozuv2=QLabel(self)
        self.font(self.yozuv2,600,50)
        
        ok.clicked.connect(self.run)
       
   
    def run(self):
        win=QMessageBox(oyna)  # oyna ichida oynacha yaratib chiqaradi
        win.setWindowTitle("Ma'lumotlaringiz!")
        win.setFont(QFont("Times",20))
        if self.ismi.currentText()!="":
            self.yozuv2.setText("Sizning ismingiz= "+self.ismi.currentText()+'; Familiyangiz= '+self.familiya.currentText()+"\n"+" shaharingiz= "+self.viloyat.currentText()+"; tumaningiz= "+self.tuman.currentText()+"\n"+"Millatingiz "+self.millat.currentText()+"; Jinsingiz "+self.gender.currentText())
        else:
            self.yozuv2.setText("Siz ma'lumot kiritngincha xatolik qildingiz qaytadan tekshiring!")
        self.yozuv2.adjustSize()
        win.setText()
        win.show()
   
app=QApplication(sys.argv)
oyna=Window()
oyna.show()
sys.exit(app.exec_())





    # uy ishi 1

# from PyQt5.QtWidgets import QApplication, QWidget
# from PyQt5.QtWidgets import QLabel, QPushButton, QRadioButton,QMessageBox
# from PyQt5.QtGui import QFont 
# import sys
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("QRadioButton")
#         self.setGeometry(150,150,900,500)
#         self.start()
#     def font(self,ob,x,y):
#         ob.setFont(QFont("Times",15))
#         ob.move(x,y)
#     def start(self):
#         self.yozuv1=QLabel("Butun son qaysi tip orqali e'lon qilinadi?",self)
#         self.font(self.yozuv1,50,10)
#         self.a1=QRadioButton("String",self)
#         self.font(self.a1,100,30)
#         self.a2=QRadioButton("Float",self)
#         self.font(self.a2,100,50)
#         self.a3=QRadioButton("Bool",self)
#         self.font(self.a3,250,30)
#         self.a4=QRadioButton("Int",self)
#         self.font(self.a4,250,50)


#         self.yozuv2=QLabel("Python dasturlash tilida primitive type tegishli metodni toping?",self)
#         self.font(self.yozuv2,50,80)
#         self.b1=QRadioButton("boal",self)
#         self.font(self.b1,100,100)
#         self.b2=QRadioButton("list",self)
#         self.font(self.b2,100,120)
#         self.b3=QRadioButton("set",self)
#         self.font(self.b3,250,100)
#         self.b4=QRadioButton("bool",self)
#         self.font(self.b4,250,120)


#         self.yozuv3=QLabel("Python dasturlash tilida listga oid metodlarni toping?",self)
#         self.font(self.yozuv3,50,150)
#         self.c1=QRadioButton("boal",self)
#         self.font(self.c1,100,170)
#         self.c2=QRadioButton("str",self)
#         self.font(self.c2,100,190)
#         self.c3=QRadioButton("set",self)
#         self.font(self.c3,250,170)
#         self.c4=QRadioButton("append",self)
#         self.font(self.c4,250,190)

#         self.yozuv4=QLabel("Python dasturlash tilida set oid metodlarni toping?",self)
#         self.font(self.yozuv4,50,220)
#         self.d1=QRadioButton("append",self)
#         self.font(self.d1,100,240)
#         self.d2=QRadioButton("pop",self)
#         self.font(self.d2,100,260)
#         self.d3=QRadioButton("index",self)
#         self.font(self.d3,250,240)
#         self.d4=QRadioButton("union",self)
#         self.font(self.d4,250,260)
        

#         self.yozuv5=QLabel("Python dasturlash tilida touple oid metodlarni toping?",self)
#         self.font(self.yozuv5,50,290)
#         self.e1=QRadioButton("update",self)
#         self.font(self.e1,100,310)
#         self.e2=QRadioButton("remove",self)
#         self.font(self.e2,100,330)
#         self.e3=QRadioButton("items",self)
#         self.font(self.e3,250,310)
#         self.e4=QRadioButton("index",self)
#         self.font(self.e4,250,330)
#         ok=QPushButton("Ok",self)
#         self.font(ok,50,380)
#         ok.clicked.connect(self.test)
#     def test(self):
#         k=0
#         ball=0
#         win=QMessageBox(self)
#         self.font(win,50,50)
#         if self.a4.isChecked():
#             win.setText("Siz to'g'ri javob berdingiz👍") 
#             k=1
#             ball+=1
#         if not(self.a1.isChecked()) and not(self.a2.isChecked()) and not(self.a3.isChecked()) and not(self.a4.isChecked()):
#             win.setText("Siz javob variantlarini tanlamadingiz😎")
#             k=1
#         if k==0:
#             win.setText("Siz noto'g'ri javob berdingiz😔")

#         if self.b4.isChecked():
#             win.setText("Siz to'g'ri javob berdingiz ")
        
#         if self.b4.isChecked():
#             win.setText("Siz to'g'ri javob berdingiz👍") 
#             k=1
#             ball+=1
#         if not(self.b1.isChecked()) and not(self.b2.isChecked()) and not(self.b3.isChecked()) and not(self.b4.isChecked()):
#             win.setText("Siz javob variantlarini tanlamadingiz😎")
#             k=1
#         if k==0:
#             win.setText("Siz noto'g'ri javob berdingiz😔")

#         if self.b4.isChecked():
#             win.setText("Siz to'g'ri javob berdingiz ")

#         if self.c4.isChecked():
#             win.setText("Siz to'g'ri javob berdingiz👍") 
#             k=1
#             ball+=1
#         if not(self.c1.isChecked()) and not(self.c2.isChecked()) and not(self.c3.isChecked()) and not(self.c4.isChecked()):
#             win.setText("Siz javob variantlarini tanlamadingiz😎")
#             k=1
#         if k==0:
#             win.setText("Siz noto'g'ri javob berdingiz😔")

#         if self.c4.isChecked():
#             win.setText("Siz to'g'ri javob berdingiz ")

#         if self.d4.isChecked():
#             win.setText("Siz to'g'ri javob berdingiz👍") 
#             k=1
#             ball+=1
#         if not(self.d1.isChecked()) and not(self.d2.isChecked()) and not(self.d3.isChecked()) and not(self.d4.isChecked()):
#             win.setText("Siz javob variantlarini tanlamadingiz😎")
#             k=1
#         if k==0:
#             win.setText("Siz noto'g'ri javob berdingiz😔")

#         if self.d4.isChecked():
#             win.setText("Siz to'g'ri javob berdingiz ")

#         if self.e4.isChecked():
#             win.setText("Siz to'g'ri javob berdingiz👍") 
#             k=1
#             ball+=1
#         if not(self.e1.isChecked()) and not(self.e2.isChecked()) and not(self.e3.isChecked()) and not(self.e4.isChecked()):
#             win.setText("Siz javob variantlarini tanlamadingiz😎")
#             k=1
#         if k==0:
#             win.setText("Siz noto'g'ri javob berdingiz😔")

#         if self.e4.isChecked():
#             win.setText("Siz to'g'ri javob berdingiz ")
#         win.show()
# app=QApplication(sys.argv)
# oyna=Window()
# oyna.show()
# sys.exit(app.exec_())
























