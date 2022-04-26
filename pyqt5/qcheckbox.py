from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtWidgets import QLabel,QPushButton,QCheckBox
from PyQt5.QtGui import QFont
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QCheckBox")
        self.setGeometry(150,150,800,500)
        self.start()
    def font(self,ob,x,y):
        ob.setFont(QFont("Times",25))
        ob.move(x,y)
    def start(self):
        self.yozuv=QLabel("Qaysi dasturlash tillarini bilasiz?",self)
        self.font(self.yozuv,50,50)
        self.v1=QCheckBox("C dasturlash tili",self)
        self.font(self.v1,100,100)
        self.v2=QCheckBox("Python dasturlash tili",self)
        self.font(self.v2,100,150)
        self.v3=QCheckBox("C++ dasturlash tili",self)
        self.font(self.v3,100,200)
        self.v4=QCheckBox("Java dasturlash tili",self)
        self.font(self.v4,100,250)
        self.ok=QPushButton("OK",self)
        self.font(self.ok,50,300)
        self.ok.clicked.connect(self.fun)
        self.back=QPushButton("<---",self)
        self.font(self.back,0,0)
        self.back.hide()
        self.back.clicked.connect(self.run)
    def run(self):
        self.yozuv.setText("Qaysi dasturlash tillarini bilasiz?")
        self.yozuv.adjustSize()
        self.v1.show()
        self.v2.show()
        self.v3.show()
        self.v4.show()
        self.ok.show()
        self.back.hide()
    def fun(self):
        k=0
        self.yozuv.setText("Siz quyidagi dasturlash tillarini bilasiz:\n")
        self.v1.hide()
        self.v2.hide()
        self.v3.hide()
        self.v4.hide()
        if self.v1.isChecked():
            self.yozuv.setText(self.yozuv.text()+"\t"+self.v1.text()+"\n")
            k=1
        if self.v2.isChecked():
            k=1
            self.yozuv.setText(self.yozuv.text()+"\t"+self.v2.text()+"\n")
        if self.v3.isChecked():
            k=1
            self.yozuv.setText(self.yozuv.text()+"\t"+self.v3.text()+"\n")
        if self.v4.isChecked():
            k=1
            self.yozuv.setText(self.yozuv.text()+"\t"+self.v4.text()+"\n")
        if k==0:
            self.yozuv.setText("Siz hech qaysi dasturlash tillarni bilmaysiz.Xa.Xa.Xa.")
        self.yozuv.adjustSize()
        self.ok.hide()
        self.back.show()
app=QApplication(sys.argv)
oyna=Window()
oyna.show()
sys.exit(app.exec_())
