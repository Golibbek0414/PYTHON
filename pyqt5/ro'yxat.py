



from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtWidgets import QLabel,QLineEdit,QPushButton,QMessageBox
from PyQt5.QtGui import QFont
import sys
ism_fam_sharf=[["G'olibbek"],["Ashirov"],["Baxtiyor o'g'li"]]
app=QApplication(sys.argv)
oyna=QWidget()
oyna.setWindowTitle("Mening birinchi dasturim")
oyna.setGeometry(200,200,800,600)
yozuv1=QLabel("Ism",oyna)
yozuv1.setFont(QFont("Times",20))
yozuv1.move(10,50)
ism=QLineEdit(oyna)
ism.setFont(QFont("Times",10))
ism.move(60,60)
ism.setPlaceholderText("ismingizni kiriting....")
yozuv2=QLabel("Familiya",oyna)
yozuv2.setFont(QFont("Times",20))
yozuv2.move(200,50)
fam=QLineEdit(oyna)
fam.setFont(QFont("Times",10))
fam.move(310,60)
fam.setPlaceholderText("familiyangizni kiriting....")
yozuv3=QLabel("Sharif",oyna)
yozuv3.setFont(QFont("Times",20))
yozuv3.move(450,50)
sharf=QLineEdit(oyna)
sharf.setFont(QFont("Times",10))
sharf.move(530,60)
sharf.setPlaceholderText("sharifingizni kiriting....")
ok=QPushButton("OK",oyna)
ok.setFont(QFont("Times",20))
ok.move(120,120)
def fun1():
    win=QMessageBox(oyna)
    win.setFont(QFont("Times",20))
    win.setWindowTitle("Ma'lumotlarni tekshirish")
    win.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel|QMessageBox.Reset)
    win.setIcon(QMessageBox.Information)
    win.setDetailedText("Ismga faqat ism kiritiladi\nFamiliyaga faqat familiya kiritiladi\nSharifga faqat sharif kiritiladi")
    if ism.text()==ism_fam_sharf[0][0] and fam.text()==ism_fam_sharf[1][0] and sharf.text()==ism_fam_sharf[2][0]:
        win.setText("Hush kelibsiz")
    elif ism.text()!=ism_fam_sharf[0][0] and fam.text()==ism_fam_sharf[1][0] and sharf.text()==ism_fam_sharf[2][0]:
        win.setText("Ism xato terilgan")
    elif ism.text()==ism_fam_sharf[0][0] and fam.text()!=ism_fam_sharf[1][0] and sharf.text()==ism_fam_sharf[2][0]:
        win.setText("Familiya xato terilgan")
    elif ism.text()==ism_fam_sharf[0][0] and fam.text()==ism_fam_sharf[1][0] and sharf.text()!=ism_fam_sharf[2][0]:
        win.setText("Sharif xato terilgan")
    elif ism.text()!=ism_fam_sharf[0][0] and fam.text()!=ism_fam_sharf[1][0] and sharf.text()==ism_fam_sharf[2][0]:
        win.setText("Ism va Familya xato terilgan")
    elif ism.text()!=ism_fam_sharf[0][0] and fam.text()==ism_fam_sharf[1][0] and sharf.text()!=ism_fam_sharf[2][0]:
        win.setText("Ism va Sharif xato terilgan")
    elif ism.text()==ism_fam_sharf[0][0] and fam.text()!=ism_fam_sharf[1][0] and sharf.text()!=ism_fam_sharf[2][0]:
        win.setText("Familya va Sharif xato terilgan")
    elif ism.text()!=ism_fam_sharf[0][0] and fam.text()!=ism_fam_sharf[1][0] and sharf.text()!=ism_fam_sharf[2][0]:
        win.setText("Ism Familiya Sharif xato terilgan")
    win.show()
ok.clicked.connect(fun1)
registry=QPushButton("REGISTRY",oyna)
registry.setFont(QFont("Times",20))
registry.move(350,120)
def fun2():
    win=QMessageBox(oyna)
    win.setWindowTitle("Ro'yxatga olish bo'limi")
    win.setFont(QFont("Times",20))
    ism_fam_sharf[0][0]=ism.text()
    ism_fam_sharf[1][0]=fam.text()
    ism_fam_sharf[2][0]=sharf.text()
    win.setText("Ism Familiya Sharif o'zgardi")
    win.show()
registry.clicked.connect(fun2)
oyna.show()
sys.exit(app.exec_())