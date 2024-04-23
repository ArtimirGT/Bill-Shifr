from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QComboBox, QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit
from settings import *

class VigenerCipher(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
        #self.app = app
        #self.parent = parent

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    
    def initUI(self):
        self.main_layout = QVBoxLayout()
        self.top_layout = QHBoxLayout()
        self.input_layout = QVBoxLayout()
        self.back_but = QPushButton('Back')
        self.input_layout.addWidget(self.back_but, alignment=Qt.AlignLeft)
        self.encoding_box = QComboBox()
        self.encoding_box.addItems(['encode', 'decode'])
        self.input_line = QLineEdit()
        self.input_layout.addWidget(self.input_line, alignment=Qt.AlignLeft)
        self.step_line = QLineEdit()
        self.input_layout.addWidget(self.step_line, alignment=Qt.AlignLeft)
        self.top_layout.addLayout(self.input_layout)
        self.top_layout.addWidget(self.encoding_box, alignment = Qt.AlignLeft)
        self.main_layout.addLayout(self.top_layout)
        self.result_line = QLabel('')
        self.main_layout.addWidget(self.result_line, alignment=Qt.AlignLeft)
        self.copy_but = QPushButton('copy')
        self.main_layout.addWidget(self.copy_but, alignment=Qt.AlignLeft)
        self.main_layout.setAlignment(Qt.AlignTop)
        self.top_layout.setAlignment(Qt.AlignLeft)
        self.setLayout(self.main_layout)

    def connects(self):
        self.copy_but.clicked.connect(self.copy)
        self.back_but.clicked.connect(self.back)

    def encode(self):
        self.encoding = self.encoding_box.currentText()
        if self.encoding == 'encode':


    def copy(self):
        c = self.app.clipboard()
        c.setText(self.result_line.text())

    def back(self):
        pass

    def check(self):
        print(self.language_box.currentText())

app = QApplication([])
window = VigenerCipher()
app.exec_()
ссылка:https://habr.com/ru/articles/140820/