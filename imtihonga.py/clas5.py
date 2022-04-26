from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random
import sys


class Window(QMainWindow):

  def __init__(self):
    super().__init__()
    self.setWindowTitle("Color Game")
    self.setGeometry(100, 100, 500, 500)
    self.UiComponents()
    self.show()
    self.count_value=15
    self.score_value=0
    self.start_Flag=False
    self.color_list=['red', 'blue', 'green', 'pink', 'black','yellow', 'orange', 'purple', 'brown']
  def UiComponents(self):
    # head=QLabel("Color Game", self)
    # head.setGeometry(100, 10, 300, 60)
    # font=QFont('Times', 14)
    # font.setBold(True)
    # font.setItalic(True)
    # font.setUnderline(True)
    # head.setFont(font)
    # head.setAlignment(Qt.AlignCenter)
    start=QPushButton("Start / Reset", self)
    start.setGeometry(200, 400, 100, 50)
    start.clicked.connect(self.start_action)
    self.score=QLabel("Score : 0", self)
    self.score.setGeometry(160, 170, 180, 50)
    self.score.setAlignment(Qt.AlignCenter)
    self.score.setFont(QFont('Times', 20))
    self.score.setStyleSheet("QLabel""{""border : 2px solid black;""color : green;""background : lightgrey;""}")
    self.color=QLabel("Color Name", self)
    self.color.setGeometry(50, 210, 400, 120)
    self.color.setAlignment(Qt.AlignCenter)
    self.color.setFont(QFont('Times', 30))
    self.input_text=QLineEdit(self)
    self.input_text.setGeometry(150, 320, 200, 50)
    self.input_text.setFont(QFont('Arial', 14))
    self.input_text.setDisabled(True)
    self.input_text.returnPressed.connect(self.input_action)
    self.count=QLabel("15", self)
    self.count.setGeometry(200, 100, 100, 50)
    self.count.setAlignment(Qt.AlignCenter)
    self.count.setFont(QFont('Times', 25))
    self.count.setStyleSheet("border : 2px solid black;""background : lightgrey;")
    timer=QTimer(self)
    timer.timeout.connect(self.show_time)
    timer.start(1000)
  def show_time(self):
    if self.start_Flag:
      self.count.setText(str(self.count_value))
      if self.count_value==0:
        self.start_Flag=False
        self.input_text.setDisabled(True)
      self.count_value-=1
  def start_action(self):
    self.start_Flag=True
    self.score.setText("Score : 0")
    self.score_value=0
    self.count_value=15
    self.input_text.clear()
    self.input_text.setEnabled(True)
    self.random_color=random.choice(self.color_list)
    self.random_color.lower()
    self.color.setStyleSheet("color : " + self.random_color + ";")
    random_text=random.choice(self.color_list)
    self.color.setText(random_text)
  def input_action(self):
    text=self.input_text.text()
    text.lower()
    if text==self.random_color:
      self.input_text.clear()
      self.score_value += 1
      self.score.setText("Score : " + str(self.score_value))
      self.random_color=random.choice(self.color_list)
      self.random_color.lower()
      self.color.setStyleSheet("color : " + self.random_color + ";")
      random_text=random.choice(self.color_list)
      self.color.setText(random_text)
app=QApplication(sys.argv)
window=Window()
sys.exit(app.exec())