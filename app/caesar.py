from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit, QComboBox
from settings import *

class caesar(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connections()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.main_layout = QVBoxLayout()
        self.up_layout = QHBoxLayout()
        self.language_box = QComboBox()
        self.language_box.addItems(['RU', 'EU'])
        self.input_line = QLineEdit()
        self.up_layout.addWidget(self.input_line, alignment = Qt.AlignLeft)
        self.up_layout.addWidget(self.language_box, alignment = Qt.AlignLeft)
        self.main_layout.addLayout(self.up_layout)
        self.but = QPushButton('but')
        self.main_layout.addWidget(self.but, alignment=Qt.AlignLeft)
        self.setLayout(self.main_layout)
    
    def connections(self):
        self.but.clicked.connect(self.check)

    def check(self):
        print(self.language_box.currentText())

    def encode(self):
        self.alfavit_EU =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        self.smeshenie = int(input('Шаг шифровки: '))
        self.message = input("Сообщение для ДЕшифровки: ").upper()
        self.itog = ''
        self.lang = self.language_box.currentText()
        if self.lang == 'RU':
            for i in self.message:
                self.mesto = self.alfavit_RU.find(i)
                self.new_mesto = self.mesto + self.smeshenie
                if i in self.alfavit_RU:
                    self.itog += self.alfavit_RU[self.new_mesto]
                else:
                    self.itog += i
        else:
            for i in self.message:
                self.mesto = self.alfavit_EU.find(i)
                self.new_mesto = self.mesto + self.smeshenie
                if i in self.alfavit_EU:
                    self.itog += self.alfavit_EU[self.new_mesto]
                else:
                    self.itog += i

app = QApplication([])

c = caesar()
app.exec_()