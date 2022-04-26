from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtWidgets import QLabel,QPushButton,QComboBox
from PyQt5.QtGui import QFont
import sys
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QComboBox")
        self.setGeometry(150,150,800,500)
        self.start()
    def font(self,ob,x,y):
        ob.setFont(QFont("Times",25))
        ob.move(x,y)
    def start(self):
        self.yozuv=QLabel("Qaysi dasturlash yo'nalishini tanlaysiz?",self)
        self.font(self.yozuv,50,50)
        self.yonalish=QComboBox(self)
        self.font(self.yonalish,100,100)
        self.yonalish.addItems(["","Frontend","Flutter","Go",".NET","Java(Spring)","NodeJS"])
        ok=QPushButton("OK",self)
        self.font(ok,50,170)
        self.yozuv2=QLabel(self)
        self.font(self.yozuv2,50,250)
        ok.clicked.connect(self.run)
    def run(self):
        if self.yonalish.currentText()!="":
            self.yozuv2.setText("Siz "+self.yonalish.currentText()+" yo'nalishini tanladingiz")
        else:
            self.yozuv2.setText("Siz hech qaysi yo'nalishni tanlamadingiz")
        self.yozuv2.adjustSize()
app=QApplication(sys.argv)
oyna=Window()
oyna.show()
sys.exit(app.exec_())