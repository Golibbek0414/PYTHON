



from PyQt5.QtWidgets import QLabel,QLineEdit,QPushButton,QMessageBox,QWidget,QApplication,QMainWindow,QTextEdit
from PyQt5.QtGui import QFont
import sys,time

getter=str()
getter2=str()
class FirstWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 100, 500, 500)
        self.setWindowTitle("Сhinese telegram")
        self.start()
    def font(self,obj):
        obj.setFont(QFont("Times",30))
    def start(self):
        yozuv1=QLabel("Login:",self)
        yozuv1.setFont(QFont("Times",25))
        yozuv1.move(50,60)
        self.log=QLineEdit(self)
        self.log.setFont(QFont("Times",25))
        self.log.move(150,60)
        self.log.setPlaceholderText("login kiriting....")

        yozuv2=QLabel("Parol:",self)
        yozuv2.setFont(QFont("Times",25))
        yozuv2.move(50,150)
        self.par=QLineEdit(self)
        self.par.setFont(QFont("Times",25))
        self.par.move(150,150)
        self.par.setPlaceholderText("parol kiriting....")

        ok=QPushButton("OK",self)
        ok.setFont(QFont("Times",50))
        ok.move(200,250)
        ok.clicked.connect(self.run)
        btn=QPushButton("exit",self)
        btn.clicked.connect(self.hide)
    def hide(self):
        self.hide()
    def run(self):
        log_par=[['Admin','12345'],['User','54321']]
        if log_par[0][0]==self.log.text() and log_par[0][1]==self.par.text():
            self.Chat=Chat()
            self.Chat.show()
        if log_par[1][0]==self.log.text() and log_par[1][1]==self.par.text():
            self.Chat1=Chat1()
            self.Chat1.show()

class Chat(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.btn=QPushButton("Back",self)
        self.btn.clicked.connect(self.run1)
        self.resize(500, 500)
        self.send()
        self.setWindowTitle("Admin's Chat")
        self.show()

    def run1(self):
        self.hide()

    def send(self):
        self.wn1=QTextEdit(self)
        self.wn1.setGeometry(10,40,480,150)
        self.wn1.setFont(QFont("Times",20))
        self.wn1.setPlaceholderText("Text kiriting...")
        self.wn2=QTextEdit(self)
        self.wn2.setGeometry(10,200,480,150)
        self.wn2.setFont(QFont("Times",20))
        self.wn2.setPlaceholderText("Sizga kelgan xabarlar... \n")
        self.wn2.setText(getter2)
        self.send1=QPushButton("Send💬",self)
        self.send1.setFont(QFont("Times",15))
        self.send1.move(200,400)
        self.send1.clicked.connect(self.sender)

    def sender(self):
        global getter
        getter=self.wn1.toPlainText()
        self.send1.hide()


class Chat1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.btn=QPushButton("Back",self)
        self.btn.clicked.connect(self.run1)
        self.resize(500, 500)
        self.send()
        self.setWindowTitle("User's Chat")
        self.show()

    def run1(self):
        self.hide()

    def send(self):
        self.wn1=QTextEdit(self)
        self.wn1.setGeometry(10,40,480,150)
        self.wn1.setFont(QFont("Times",20))
        self.wn1.setPlaceholderText("Text kiriting...")
        self.wn2=QTextEdit(self)
        self.wn2.setGeometry(10,200,480,150)
        self.wn2.setFont(QFont("Times",20))
        self.wn2.setPlaceholderText("Sizga kelgan xabarlar... \n")
        self.wn2.setText(getter)
        self.send1=QPushButton("Send💬",self)
        self.send1.setFont(QFont("Times",15))
        self.send1.move(200,400)
        self.send1.clicked.connect(self.sender)

    def sender(self):
        global getter2
        getter2=self.wn1.toPlainText()
        self.send1.hide()
app=QApplication(sys.argv)
oyna=FirstWindow()
oyna.show()
sys.exit(app.exec_())
