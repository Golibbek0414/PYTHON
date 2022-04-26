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
        self.yozuv=QLabel("Butun son qaysi tip orqali e'lon qilinadi?",self)
        self.font(self.yozuv,50,50)
        self.a1=QRadioButton("Int",self)
        self.font(self.a1,100,100)
        self.a2=QRadioButton("Float",self)
        self.font(self.a2,100,150)
        self.a3=QRadioButton("Bool",self)
        self.font(self.a3,100,200)
        self.a4=QRadioButton("String",self)
        self.font(self.a4,100,250)
        ok=QPushButton("Ok",self)
        self.font(ok,50,300)
        ok.clicked.connect(self.test)
    def test(self):
        k=0
        win=QMessageBox(self)
        self.font(win,50,50)
        if self.a1.isChecked():
            win.setText("Siz to'g'ri javob berdingiz👍")
            k=1
        if not(self.a1.isChecked()) and not(self.a2.isChecked()) and not(self.a3.isChecked()) and not(self.a4.isChecked()):
            win.setText("Siz javob variantlarini tanlamadingiz😎")
            k=1
        if k==0:
            win.setText("Siz noto'g'ri javob berdingiz😔")
        win.show()
app=QApplication(sys.argv)
oyna=Window()
oyna.show()
sys.exit(app.exec_())