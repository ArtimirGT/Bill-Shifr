from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit, QComboBox
from settings import *

class caesar_with_key(QWidget):
    def __init__(self, app, parent):
        super().__init__()
        self.parent = parent
        self.app = app
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
        self.top_layout = QHBoxLayout()
        self.input_layout = QVBoxLayout()
        self.choice_layout = QHBoxLayout()
        self.back_but = QPushButton(txt_back)
        self.input_layout.addWidget(self.back_but, alignment=Qt.AlignLeft)
        self.language_box = QComboBox()
        self.language_box.addItems(['RU', 'EU'])
        self.input_line = QLineEdit()
        self.input_layout.addWidget(self.input_line, alignment=Qt.AlignTop)
        self.key_line = QLineEdit()
        self.input_layout.addWidget(self.key_line, alignment=Qt.AlignLeft)
        self.step_line = QLineEdit()
        self.input_layout.addWidget(self.step_line, alignment=Qt.AlignLeft)
        self.top_layout.addLayout(self.input_layout)
        #self.top_layout.addWidget(self.language_box, alignment = Qt.AlignLeft)
        self.main_layout.addLayout(self.top_layout)
        self.encode_but = QPushButton(txt_encode)
        #self.main_layout.addWidget(self.encode_but, alignment=Qt.AlignLeft)
        self.decode_but = QPushButton(txt_decode)
        #self.main_layout.addWidget(self.decode_but, alignment=Qt.AlignLeft)
        self.choice_layout.addWidget(self.language_box, alignment=Qt.AlignLeft)
        self.choice_layout.addWidget(self.encode_but, alignment=Qt.AlignLeft)
        self.choice_layout.addWidget(self.decode_but, alignment=Qt.AlignLeft)
        self.choice_layout.setAlignment(Qt.AlignLeft)
        self.main_layout.addLayout(self.choice_layout)
        self.result_line = QLabel('')
        self.main_layout.addWidget(self.result_line, alignment=Qt.AlignLeft)
        self.copy_but = QPushButton(txt_copy)
        self.main_layout.addWidget(self.copy_but, alignment=Qt.AlignLeft)
        self.main_layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.main_layout)

    def connections(self):
        self.encode_but.clicked.connect(self.encode)
        self.decode_but.clicked.connect(self.decode)
        self.copy_but.clicked.connect(self.copy)
        self.back_but.clicked.connect(self.back)

    def copy(self):
        c = self.app.clipboard()
        c.setText(self.result_line.text())

    def decode(self):
        self.alfavit_EU =  txt_alfavit_EU
        self.alfavit_RU = txt_alfavit_RU
        self.smeshenie = int(self.step_line.text())
        self.key_unedit = self.key_line.text().upper()
        self.key = ''
        for i in self.key_unedit:
            if i not in self.key:
                self.key += i
        self.message = self.input_line.text().upper()
        self.itog = ''
        self.lang = self.language_box.currentText()
        try:
            if self.lang == 'RU':
                self.new_alfavit_RU = ''
                for i in range(len(self.alfavit_RU)):
                    if i == self.smeshenie:
                        self.new_alfavit_RU += self.key
                    if self.alfavit_RU[i-self.smeshenie] not in self.new_alfavit_RU:
                        self.new_alfavit_RU += self.alfavit_RU[i-self.smeshenie]
                for i in self.message:
                    if i not in self.new_alfavit_RU:
                        self.itog += i
                    else:
                        self.itog += self.alfavit_RU[self.new_alfavit_RU.find(i)]
            else:
                self.new_alfavit_EU = ''
                for i in range(len(self.alfavit_EU)):
                    if i == self.smeshenie:
                        self.new_alfavit_EU += self.key
                    if self.alfavit_EU[i-self.smeshenie] not in self.new_alfavit_EU:
                        self.new_alfavit_EU += self.alfavit_EU[i-self.smeshenie]
                for i in self.message:
                    if i not in self.new_alfavit_EU:
                        self.itog += i
                    else:
                        self.itog += self.alfavit_EU[self.new_alfavit_EU.find(i)]
            self.result_line.setText(self.itog)
        except:
            self.result_line.setText(txt_error)

    def encode(self):
        self.alfavit_EU =  txt_alfavit_EU
        self.alfavit_RU = txt_alfavit_RU
        self.smeshenie = int(self.step_line.text())
        self.key_unedit = self.key_line.text().upper()
        self.key = ''
        for i in self.key_unedit:
            if i not in self.key:
                self.key += i
        self.message = self.input_line.text().upper()
        self.itog = ''
        self.lang = self.language_box.currentText()
        try:
            if self.lang == 'RU':
                self.new_alfavit_RU = ''
                for i in range(len(self.alfavit_RU)):
                    if i == self.smeshenie:
                        self.new_alfavit_RU += self.key
                    if self.alfavit_RU[i-self.smeshenie] not in self.new_alfavit_RU:
                        self.new_alfavit_RU += self.alfavit_RU[i-self.smeshenie]
                for i in self.message:
                    if i not in self.alfavit_RU:
                        self.itog += i
                    else:
                        self.itog += self.new_alfavit_RU[self.alfavit_RU.find(i)]

            else:
                self.new_alfavit_EU = ''
                for i in range(len(self.alfavit_EU)):
                    if i == self.smeshenie:
                        self.new_alfavit_EU += self.key
                    if self.alfavit_EU[i-self.smeshenie] not in self.new_alfavit_EU:
                        self.new_alfavit_EU += self.alfavit_EU[i-self.smeshenie]
                for i in self.message:
                    if i not in self.alfavit_EU:
                        self.itog += i
                    else:
                        self.itog += self.new_alfavit_EU[self.alfavit_EU.find(i)]
            self.result_line.setText(self.itog)
        except:
            self.result_line.setText(txt_error)

    def back(self):
        self.hide()
        self.parent.show()