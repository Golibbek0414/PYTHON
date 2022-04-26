from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtWidgets import QPushButton,QRadioButton,QMessageBox
from PyQt5.QtGui import QFont
import sys,random
ls=[1,1,2,2,3,3]
random.shuffle(ls)

class Tugma(QPushButton):
    def __init__(self,name,ob,x,y):
        super().__init__(name,ob)
        self.setFont(QFont("Times",40))
        self.setGeometry(x,y,100,100)
    def click(self,fun):
        self.clicked.connect(fun)
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,430,500)
        self.begin()
        self.k=0;self.a=0;self.b=0;self.c=0;self.d=0;self.e=0
        self.sum=0
    def font(self,ob):
        ob.setFont(QFont("Times",40))
    def begin(self):
        
        self.a1=Tugma("",self,50,160)
        self.a2=Tugma("",self,160,160)
        self.a3=Tugma("",self,270,160)
        self.a4=Tugma("",self,50,270)
        self.a5=Tugma("",self,160,270)
        self.a6=Tugma("",self,270,270)

        self.numbers=[self.a1,self.a2,self.a3,self.a4,self.a5,self.a6]

        self.a1.click(self.A1)
        self.a2.click(self.A2)
        self.a3.click(self.A3)
        self.a4.click(self.A4)
        self.a5.click(self.A5)
        self.a6.click(self.A6)

    def A1(self):

        self.k+=1
        self.a1.setText(str(ls[0]))
        if self.a==1:
            if self.a2.text()==self.a1.text():
                self.a1.hide()
                self.a2.hide()
                self.sum+=1
            elif self.a2.text()!=self.a1.text():
                self.a1.setText("")
                self.a2.setText("")
                self.a=0;self.k=0
        if self.b==1:
            if self.a1.text()==self.a3.text():
                self.a1.hide()
                self.a3.hide()
                self.sum+=1
            elif self.a1.text()!=self.a3.text():
                self.a1.setText("")
                self.a3.setText("")
                self.b=0;self.k=0
        if self.c==1:
            if self.a1.text()==self.a4.text():
                self.a1.hide()
                self.a4.hide()
                self.sum+=1
            elif self.a1.text()!=self.a4.text():
                self.a1.setText("")
                self.a4.setText("")
                self.c=0;self.k=0
        if self.d==1:
            if self.a1.text()==self.a5.text():
                self.a1.hide()
                self.a5.hide()
                self.sum+=1
            elif self.a1.text()!=self.a5.text():
                self.a1.setText("")
                self.a5.setText("")
                self.d=0;self.k=0
        if self.e==1:
            if self.a1.text()==self.a6.text():
                self.a1.hide()
                self.a6.hide()
                self.sum+=1
            elif self.a1.text()!=self.a6.text():
                self.a1.setText("")
                self.a6.setText("")
                self.e=0;self.k=0
        if self.sum==3:
            self.oynacha=QMessageBox(self)
            self.setWindowTitle("Info")
            self.oynacha.setText("GAME OVER")
            self.oynacha.show()
            


    def A2(self):
        self.a+=1
        self.a2.setText(str(ls[1]))
        if self.k==1:
            if self.a2.text()==self.a1.text():
                self.a1.hide()
                self.a2.hide()
                self.sum+=1
            elif self.a2.text()!=self.a1.text():
                self.a1.setText("")
                self.a2.setText("")
                self.a=0;self.k=0
        if self.b==1:
            if self.a2.text()==self.a3.text():
                self.a2.hide()
                self.a3.hide()
                self.sum+=1
            elif self.a2.text()!=self.a3.text():
                self.a2.setText("")
                self.a3.setText("")
                self.b=0;self.a=0
        if self.c==1:
            if self.a2.text()==self.a4.text():
                self.a2.hide()
                self.a4.hide()
                self.sum+=1
            elif self.a2.text()!=self.a4.text():
                self.a2.setText("")
                self.a4.setText("")
                self.c=0;self.a=0
        if self.d==1:
            if self.a2.text()==self.a5.text():
                self.a2.hide()
                self.a5.hide()
                self.sum+=1
            elif self.a2.text()!=self.a5.text():
                self.a2.setText("")
                self.a5.setText("")
                self.d=0;self.a=0
        if self.e==1:
            if self.a2.text()==self.a6.text():
                self.a1.hide()
                self.a6.hide()
                self.sum+=1
            elif self.a1.text()!=self.a6.text():
                self.a1.setText("")
                self.a6.setText("")
                self.e=0;self.a=0
        if self.sum==3:
            self.oynacha=QMessageBox(self)
            self.setWindowTitle("Info")
            self.oynacha.setText("GAME OVER")
            self.oynacha.show()

        
    def A3(self):
        self.b+=1
        self.a3.setText(str(ls[2]))
        if self.k==1:
            if self.a3.text()==self.a1.text():
                self.a1.hide()
                self.a3.hide()
                self.sum+=1
            elif self.a2.text()!=self.a1.text():
                self.a1.setText("")
                self.a3.setText("")
                self.k=0;self.b=0
        if self.a==1:
            if self.a3.text()==self.a2.text():
                self.a2.hide()
                self.a3.hide()
                self.sum+=1
            elif self.a3.text()!=self.a2.text():
                self.a2.setText("")
                self.a3.setText("")
                self.a=0;self.b=0
        if self.c==1:
            if self.a3.text()==self.a4.text():
                self.a2.hide()
                self.a4.hide()
                self.sum+=1
            elif self.a2.text()!=self.a4.text():
                self.a2.setText("")
                self.a4.setText("")
                self.c=0;self.b=0
        if self.d==1:
            if self.a3.text()==self.a5.text():
                self.a2.hide()
                self.a5.hide()
                self.sum+=1
            elif self.a3.text()!=self.a5.text():
                self.a2.setText("")
                self.a5.setText("")
                self.d=0;self.b=0
        if self.e==1:
            if self.a3.text()==self.a6.text():
                self.a3.hide()
                self.a6.hide()
                self.sum+=1
            elif self.a3.text()!=self.a6.text():
                self.a3.setText("")
                self.a6.setText("")
                self.e=0;self.b=0
        if self.sum==3:
            self.oynacha=QMessageBox(self)
            self.setWindowTitle("Info")
            self.oynacha.setText("GAME OVER")
            self.oynacha.show()

    def A4(self):
        self.c+=1
        self.a4.setText(str(ls[3]))
        if self.k==1:
            if self.a4.text()==self.a1.text():
                self.a1.hide()
                self.a4.hide()
                self.sum+=1
            elif self.a4.text()!=self.a1.text():
                self.a1.setText("")
                self.a4.setText("")
                self.k=0;self.c=0
        if self.a==1:
            if self.a4.text()==self.a2.text():
                self.a4.hide()
                self.a2.hide()
                self.sum+=1
            elif self.a4.text()!=self.a2.text():
                self.a4.setText("")
                self.a2.setText("")
                self.a=0;self.c=0
        if self.b==1:
            if self.a4.text()==self.a3.text():
                self.a4.hide()
                self.a3.hide()
                self.sum+=1
            elif self.a4.text()!=self.a3.text():
                self.a4.setText("")
                self.a3.setText("")
                self.b=0;self.c=0
        if self.d==1:
            if self.a4.text()==self.a5.text():
                self.a4.hide()
                self.a5.hide()
                self.sum+=1
            elif self.a4.text()!=self.a5.text():
                self.a4.setText("")
                self.a5.setText("")
                self.d=0;self.c=0
        if self.e==1:
            if self.a4.text()==self.a6.text():
                self.a4.hide()
                self.a6.hide()
                self.sum+=1
            elif self.a4.text()!=self.a6.text():
                self.a4.setText("")
                self.a6.setText("")
                self.e=0;self.c=0
        if self.sum==3:
            self.oynacha=QMessageBox(self)
            self.setWindowTitle("Info")
            self.oynacha.setText("GAME OVER")
            self.oynacha.show()
    def A5(self):
        self.d+=1
        self.a5.setText(str(ls[4]))
        if self.k==1:
            if self.a5.text()==self.a1.text():
                self.a5.hide()
                self.a1.hide()
                self.sum+=1
            elif self.a5.text()!=self.a1.text():
                self.a5.setText("")
                self.a1.setText("")
                self.k=0;self.d=0
        if self.a==1:
            if self.a5.text()==self.a2.text():
                self.a5.hide()
                self.a2.hide()
                self.sum+=1
            elif self.a5.text()!=self.a2.text():
                self.a5.setText("")
                self.a2.setText("")
                self.a=0;self.d=0
        if self.b==1:
            if self.a5.text()==self.a3.text():
                self.a5.hide()
                self.a3.hide()
                self.sum+=1
            elif self.a5.text()!=self.a3.text():
                self.a5.setText("")
                self.a3.setText("")
                self.b=0;self.d=0
        if self.c==1:
            if self.a5.text()==self.a4.text():
                self.a5.hide()
                self.a4.hide()
                self.sum+=1
            elif self.a5.text()!=self.a4.text():
                self.a5.setText("")
                self.a4.setText("")
                self.c=0;self.d=0
        if self.e==1:
            if self.a5.text()==self.a6.text():
                self.a5.hide()
                self.a6.hide()
                self.sum+=1
            elif self.a5.text()!=self.a6.text():
                self.a5.setText("")
                self.a6.setText("")
                self.d=0;self.e=0
        if self.sum==3:
            self.oynacha=QMessageBox(self)
            self.setWindowTitle("Info")
            self.oynacha.setText("GAME OVER")
            self.oynacha.show()
    def A6(self):
        self.e+=1
        self.a6.setText(str(ls[5]))
        if self.k==1:
            if self.a6.text()==self.a1.text():
                self.a6.hide()
                self.a1.hide()
                self.sum+=1
            elif self.a6.text()!=self.a1.text():
                self.a6.setText("")
                self.a1.setText("")
                self.k=0;self.e=0
        if self.a==1:
            if self.a6.text()==self.a2.text():
                self.a6.hide()
                self.a2.hide()
                self.sum+=1
            elif self.a6.text()!=self.a2.text():
                self.a6.setText("")
                self.a2.setText("")
                self.a=0;self.e=0
        if self.b==1:
            if self.a6.text()==self.a3.text():
                self.a6.hide()
                self.a3.hide()
                self.sum+=1
            elif self.a6.text()!=self.a3.text():
                self.a6.setText("")
                self.a3.setText("")
                self.b=0;self.e=0
        if self.c==1:
            if self.a6.text()==self.a4.text():
                self.a6.hide()
                self.a4.hide()
                self.sum+=1
            elif self.a6.text()!=self.a4.text():
                self.a6.setText("")
                self.a4.setText("")
                self.c=0;self.e=0
        if self.d==1:
            if self.a6.text()==self.a5.text():
                self.a6.hide()
                self.a5.hide()
                self.sum+=1
            elif self.a6.text()!=self.a5.text():
                self.a6.setText("")
                self.a5.setText("")
                self.d=0;self.e=0
        if self.sum==3:
            self.oynacha=QMessageBox(self)
            self.setWindowTitle("Info")
            self.oynacha.setText("GAME OVER")
            self.oynacha.show()
    
app=QApplication(sys.argv)
oyna=Window()
oyna.show()
sys.exit(app.exec_())

