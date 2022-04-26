from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLabel, QPushButton, QRadioButton,QMessageBox
from PyQt5.QtGui import QFont 
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QRadioButton")
        self.setGeometry(150,150,800,500)
        self.start()
    def font(self,ob,x,y):
        ob.setFont(QFont("Times",25))
        ob.move(x,y)
    def start(self):
        self.yozuv=QLabel(self)
        self.font(self.yozuv,50,50)
        self.a1=QRadioButton("0",self)
        self.font(self.a1,200,150)
        self.a2=QRadioButton("x",self)
        self.font(self.a2,100,150)
        
        self.ok=QPushButton("Ok",self)
        self.font(self.ok,50,250)
    
        self.ok.clicked.connect(self.a)

        self.b1=QPushButton("",self)
        self.b1.setGeometry(50,50,40,40)
        self.font(self.a1,100,100)
        self.b2=QPushButton("",self)
        self.b2.setGeometry(50,100,40,40)
        self.font(self.a1,100,100)
        self.b3=QPushButton("",self)
        self.b3.setGeometry(50,150,40,40)
        self.font(self.a1,100,100)
        self.b4=QPushButton("",self)
        self.b4.setGeometry(100,50,40,40)
        self.font(self.a1,100,100)
        self.b5=QPushButton("",self)
        self.b5.setGeometry(100,100,40,40)
        self.font(self.a1,100,100)
        self.b6=QPushButton("",self)
        self.b6.setGeometry(100,150,40,40)
        self.font(self.a1,100,100)
        self.b7=QPushButton("",self)
        self.b7.setGeometry(150,50,40,40)
        self.font(self.a1,100,100)
        self.b8=QPushButton("",self)
        self.b8.setGeometry(150,100,40,40)
        self.font(self.a1,100,100)
        self.b9=QPushButton("",self)
        self.b9.setGeometry(150,150,40,40)
        self.font(self.a1,100,100)

        self.b1.hide()
        self.b2.hide()
        self.b3.hide()
        self.b4.hide()
        self.b5.hide()
        self.b6.hide()
        self.b7.hide()
        self.b8.hide()
        self.b9.hide()
    def a(self):
        if self.a1.isChecked():
            self.a=self.a1.text()
        elif self.a2.isChecked():
            self.a=self.a2.text()
        self.a1.hide()
        self.a2.hide()
        self.ok.hide()

        self.b1.show()
        self.b2.show()
        self.b3.show()
        self.b4.show()
        self.b5.show()
        self.b6.show()
        self.b7.show()
        self.b8.show()
        self.b9.show()

    def A1(self):

        self.k+=1
        self.a1.setText(str())
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


    

app=QApplication(sys.argv)
oyna=Window()
oyna.show()
sys.exit(app.exec_())