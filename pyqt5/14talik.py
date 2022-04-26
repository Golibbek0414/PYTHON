from PyQt5.QtWidgets import QLabel,QLineEdit,QPushButton
from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtGui import QFont
import sys
class FirstWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 500, 500)
        self.btn=QPushButton("Registration",self)
        self.btn.move(100, 100)
        self.btn.clicked.connect(self.run1)
        self.second=SecondWindow()
    def run1(self):
        self.second.show()
class SecondWindow(QWidget):
    def init(self):
        super().init()
        self.setGeometry(100, 100, 500, 500)
        self.start()
    def font(self,obj):
        obj.setFont(QFont("Times",20))
    def start(self):
        login=QLabel("Login: ",self)
        self.font(login)
        login.move(100,100)
        parol=QLabel("Parol: ",self)
        self.font(parol)
        parol.move(100,200)
        btn=QPushButton("Back",self)
        btn.clicked.connect(self.run)
    def run(self):
        self.hide()
app=QApplication(sys.argv)
oyna=FirstWindow()
oyna.show()
sys.exit(app.exec_())