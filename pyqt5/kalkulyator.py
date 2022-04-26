


#Calc.mainloop()



from PyQt5.QtWidgets import *
from PyQt5 import QtCore,QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(400,200,320,315)
        self.widgets()
        self.show()
    def widgets(self):
        self.label=QLabel(self)
        self.label.setGeometry(5,5,310,55)
        self.label.setFont(QFont('Arial',25))


        one=QPushButton("1",self)
        two=QPushButton("2",self)
        three=QPushButton("3",self)
        four=QPushButton("4",self)
        five=QPushButton("5",self)
        six=QPushButton("6",self)
        seven=QPushButton("7",self)
        eight=QPushButton("8",self)
        nine=QPushButton("9",self)
        zero=QPushButton("0",self)
        plus=QPushButton("+",self)
        minus=QPushButton("-",self)
        kopay=QPushButton("*",self)
        bolu=QPushButton("/",self)
        remainder=QPushButton("%",self)
        degree=QPushButton("",self)
        clear=QPushButton("clear",self)
        ravno=QPushButton("=",self)


        one.setFont(QFont('Arial',15))
        two.setFont(QFont('Arial',15))
        three.setFont(QFont('Arial',15))
        four.setFont(QFont('Arial',15))
        five.setFont(QFont('Arial',15))
        six.setFont(QFont('Arial',15))
        seven.setFont(QFont('Arial',15))
        eight.setFont(QFont('Arial',15))
        nine.setFont(QFont('Arial',15))
        zero.setFont(QFont('Arial',15))
        plus.setFont(QFont('Arial',15))
        minus.setFont(QFont('Arial',15))
        kopay.setFont(QFont('Arial',15))
        bolu.setFont(QFont('Arial',15))
        remainder.setFont(QFont('Arial',15))
        degree.setFont(QFont('Arial',15))
        clear.setFont(QFont('Arial',15))
        ravno.setFont(QFont('Arial',15))
        

        one.setGeometry(5,120,70,40)
        two.setGeometry(85,120,70,40)
        three.setGeometry(165,120,70,40)
        four.setGeometry(5,170,70,40)
        five.setGeometry(85,170,70,40)
        six.setGeometry(165,170,70,40)
        seven.setGeometry(5,220,70,40)
        eight.setGeometry(85,220,70,40)
        nine.setGeometry(165,220,70,40)
        zero.setGeometry(5,270,70,40)
        plus.setGeometry(245,120,70,40)
        minus.setGeometry(245,170,70,40)
        kopay.setGeometry(245,220,70,40)
        bolu.setGeometry(245,270,70,40)
        remainder.setGeometry(85,270,70,40)
        degree.setGeometry(165,270,70,40)
        clear.setGeometry(165,70,150,40)
        ravno.setGeometry(5,70,150,40)
        
        
        one.clicked.connect(self.action1)
        two.clicked.connect(self.action2)
        three.clicked.connect(self.action3)
        four.clicked.connect(self.action4)
        five.clicked.connect(self.action5)
        six.clicked.connect(self.action6)
        seven.clicked.connect(self.action7)
        eight.clicked.connect(self.action8)
        nine.clicked.connect(self.action9)
        zero.clicked.connect(self.action0)
        plus.clicked.connect(self.action_plus)
        minus.clicked.connect(self.action_minus)
        kopay.clicked.connect(self.action_kopay)
        bolu.clicked.connect(self.action_bolu)
        remainder.clicked.connect(self.action_remainder)
        degree.clicked.connect(self.action_degree)
        clear.clicked.connect(self.action_clear)
        ravno.clicked.connect(self.action_ravno)
    
    def action_ravno(self):
        result=self.label.text()
        try:
            ans=eval(result)
            self.label.setText(str(ans))
        except ZeroDivisionError:
            self.label.setText("No'lga bolib bo'lmaydi!")
        except:
            self.label.setText("Error")
    def action_plus(self):
        result=self.label.text()
        self.label.setText(result+"+")
    def action_minus(self):
        result=self.label.text()
        self.label.text(result+"-")

    def action_bolu(self):
        result=self.label.text()
        self.label.setText(result+"//")
    def action_kopay(self):
        result=self.label.text()
        self.label.setText(result+"*")
    def action_remainder(self):
        result=self.label.text()
        self.label.setText(result+"%")
    def action_degree(self):
        result=self.label.text()
        self.label.setText(result+"")
    def action_clear(self):
        result=self.label.text()
        self.label.setText(result[:-1])
    def action0(self):
        result=self.label.text()
        self.label.setText(result+"0")
    def action1(self):
        result=self.label.text()
        self.label.setText(result+"1")
    def action2(self):
        result=self.label.text()
        self.label.setText(result+"2")
    def action3(self):
        result=self.label.text()
        self.label.setText(result+"3")
    def action4(self):
        result=self.label.text()
        self.label.setText(result+"4")
    def action5(self):
        result=self.label.text()
        self.label.setText(result+"5")
    def action6(self):
        result=self.label.text()
        self.label.setText(result+"6")
    def action7(self):
        result=self.label.text()
        self.label.setText(result+"7")
    def action8(self):
        result=self.label.text()
        self.label.setText(result+"8")
    def action9(self):
        result=self.label.text()
        self.label.setText(result+"9")

App=QApplication(sys.argv)
window=Window()
sys.exit(App.exec())