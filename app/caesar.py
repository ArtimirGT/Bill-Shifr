from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit, QComboBox
from settings import *

class caesar(QWidget):
    def __init__(self, app, parent, state):
        super().__init__()
        self.win_x = state[0]
        self.win_y = state[1]
        self.win_height = state[2]
        self.win_width = state[3]
        self.parent = parent
        self.app = app
        self.set_appear()
        self.initUI()
        self.connections()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(self.win_width, self.win_height)
        self.move(self.win_x, self.win_y)

    def initUI(self):
        self.main_layout = QVBoxLayout()
        self.top_layout = QHBoxLayout()
        self.input_layout = QVBoxLayout()
        self.choice_layout = QHBoxLayout()
        self.back_but = QPushButton(txt_back)
        self.input_layout.addWidget(self.back_but, alignment=Qt.AlignLeft)
        self.language_box = QComboBox()
        self.language_box.addItems(['RU', 'EU'])
        self.input_line = QLineEdit()
        self.input_layout.addWidget(self.input_line, alignment=Qt.AlignTop)
        self.step_line = QLineEdit()
        self.input_layout.addWidget(self.step_line, alignment=Qt.AlignLeft)
        self.top_layout.addLayout(self.input_layout)
        #self.top_layout.addWidget(self.language_box, alignment = Qt.AlignLeft)
        self.choice_layout.addWidget(self.language_box, alignment=Qt.AlignLeft)
        self.process_but = QPushButton(txt_process)
        self.choice_layout.addWidget(self.process_but, alignment=Qt.AlignLeft)
        self.main_layout.addLayout(self.top_layout)
        self.choice_layout.setAlignment(Qt.AlignLeft)
        self.main_layout.addLayout(self.choice_layout)
        self.result_line = QLabel('')
        self.main_layout.addWidget(self.result_line, alignment=Qt.AlignLeft)
        self.copy_but = QPushButton(txt_copy)
        self.main_layout.addWidget(self.copy_but, alignment=Qt.AlignLeft)
        self.main_layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.main_layout)
    
    def connections(self):
        self.process_but.clicked.connect(self.encode)
        self.copy_but.clicked.connect(self.copy)
        self.back_but.clicked.connect(self.back)

    def copy(self):
        c = self.app.clipboard()
        c.setText(self.result_line.text())

    def check(self):
        print(self.language_box.currentText())

    def encode(self):
        self.alfavit_EU =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        self.smeshenie = int(self.step_line.text())
        self.message = self.input_line.text().upper()
        self.itog = ''
        self.lang = self.language_box.currentText()
        try:
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
            self.result_line.setText(self.itog)
        except:
            self.result_line.setText(txt_error)

    def back(self):
        self.hide()
        self.parent.move(self.x(), self.y())
        self.parent.resize(self.width(), self.height())
        self.parent.show()