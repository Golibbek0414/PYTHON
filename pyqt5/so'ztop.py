# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random
import sys


class Window(QMainWindow):

	def __init__(self):
		super().__init__()

		# Appning titulni nomlavommiz
		self.setWindowTitle("O'yin")

		# Appni geometrik koordinatalarini to'g'illavoldik
		self.setGeometry(100, 100, 320, 350)

		# Ushbu Methodni chaqidik
		self.UiComponents()

		# So'zlar
		self.words = ['red', 'cold', 'hot']

		# Hozirgi so'zimiz
		self.current_text = ""


	def UiComponents(self):

		# Asosiy Metkani e'lon qildik
		head = QLabel("Chalkash So'z O'yini", self)

		# head'ning geometrik shaklini yasavommiz
		head.setGeometry(20, 10, 280, 60)

		# font
		font = QFont('Times', 15)
		font.setBold(True)
		font.setItalic(True)
		font.setUnderline(True)

		# head qanday ko'rinishini fontdan olamiz
		head.setFont(font)

		# head ichidigi yozuv ya'ni "Chalkash So'z O'yini" labelning o'rtasida joylanishi kereligini ko'rsatdik
		head.setAlignment(Qt.AlignCenter)

		# chalkashtirilgan so'zni ko'rsatish uchun bitta label ya'ni metka ochvoldu
		self.ch_soz = QLabel(self)

		# Yuqoridigi labelni geometrik koordinatalarini to'g'illavoldik
		self.ch_soz.setGeometry(30, 80, 260, 50)

		# chalkash soz labelini chegarasi va orqa foni qanaqa bo'lishini yozdik
		self.ch_soz.setStyleSheet("border : 2px solid black; background : white;")

		# chalkash soz labelini ichiga yoziladigan yozuv qanaqa ko'rinishda va razmeri nechchi bo'lishini ko'rsatdik
		self.ch_soz.setFont(QFont('Times', 12))

		# Foydalanuvchi so'z kiritishi uchun line edit ochdik va uni input o'zgaruvchisiga tenglashtirdik
		self.input = QLineEdit(self)

		# inputning geometrik koordinatalarini to'g'illavoldik
		self.input.setGeometry(20, 150, 200, 40)

		# kiritilingan so'zni tekshirish uchun tugma yasadik va uni check o'zgaruvchisiga tenglashtirdik
		self.check = QPushButton("Check", self)

		# check tugmasi geometrik koordinatalarini to'g'illavoldik
		self.check.setGeometry(230, 155, 80, 30)

		# check tugmasi bosilganda qayerga ulanishi kereligini ko'rsatdu
		self.check.clicked.connect(self.check_action)

		# natijani olish uchun 1ta label yasadik va uni result o'zgaruvchisiga tenglashtirdik
		self.result = QLabel(self)

		# result labelini geometrik koordinatalarini to'g'illavoldik
		self.result.setGeometry(40, 210, 240, 50)

		# result da chiqadigan so'z qanaqa ko'rinishda va uning razmerini ko'rsatib o'tvommiza
		self.result.setFont(QFont('Times', 13))

		# resultning chegarasi va orqa foni qanaqa bo'lishini ko'rsatdik
		self.result.setStyleSheet("border : 2px solid black; background : yellow;")

		# o'yinni boshlash va qaytadan o'yinni ishga tushirish uchun start va reset tugmachalarini yasadik
		start = QPushButton("Start", self)
		reset = QPushButton("Reset", self)

		# Ikkala tugmachalar uchun geometrik koordinatalarini to'g'illavoldik
		start.setGeometry(15, 290, 140, 40)
		reset.setGeometry(165, 290, 140, 40)

		# Ikkala tugmacha bosilganida qayerga ulanishi kereligini ko'rsatib o'tdik
		start.clicked.connect(self.start_action)
		reset.clicked.connect(self.reset_action)

	def check_action(self):

		# input editorida yozilgan so'zni text digan o'zgaruvchiga tenglavoldik
		text = self.input.text()

		# text ichidagi so'z current_text icidagi so'z bilan bir hilmi yo'qmi shuni tekshirvommiz
		if text == self.current_text:
			self.result.setText("Correct Answer")

			# To'g'ri javob bo'ganiga resultning orqa fonini yashil rangga o'girvommiz
			self.result.setStyleSheet("background : lightgreen;")

		else:
			self.result.setText("Wrong Answer")

			# Noto'g'ri jovob bo'ganiga result ning orqa fonini qizil qivommiza
			self.result.setStyleSheet("background : red;")



	def start_action(self):

		# bitta random so'zzni current_text ga words digan listimizadan oldik
		self.current_text = random.choice(self.words)

		# sample() funksiyasi bizaga current_text ichidigi so'zlani chalkashtirib berish uchun yordam beradi
        #  va uni random_word o'zgaruvchisiga list ko'rinishida tenglidi
		random_word = random.sample(self.current_text, len(self.current_text))
        
        
		# join() funksiyasi orqali random_word ichidigi ma'lumotni string ko'rinishiga keltiradi
		jumbled = ''.join(random_word)

		# yakuniy chalkashtirilgan so'zni ch_soz ichiga bervoramiza
		self.ch_soz.setText(jumbled)

		# result ichini bo'sh ko'rsatish maqsadida " " dan foydalanamiza
		self.result.setText("")

		# result ning chegarasi va orqa fonini o'zimiz hohlagandeki qilamiza
		self.result.setStyleSheet("border : 2px solid black; background : yellow;")

		# inputni ichiniyam bo'shatamiza
		self.input.setText("")

	def reset_action(self):
		self.current_text = ""


		self.input.setText("")


		self.ch_soz.setText("")
		self.result.setText("")

        #resultning chegarasi va orqa fonini to'g'illimza o'zimiza holagancha
		self.result.setStyleSheet("border : 2px solid black; background : yellow;")


App = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(App.exec())

