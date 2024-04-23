from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit, QComboBox
from settings import *

class omofo(QWidget):
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
        self.back_but = QPushButton('BACK')
        self.input_line = QLineEdit()
        self.key_line = QLineEdit()
        self.mode_box = QComboBox()
        self.mode_box.addItems(['encode', 'decode'])
        self.input_layout.addWidget(self.back_but, alignment=Qt.AlignLeft)
        self.input_layout.addWidget(self.input_line, alignment=Qt.AlignLeft)
        self.input_layout.addWidget(self.key_line, alignment=Qt.AlignLeft)
        self.top_layout.addLayout(self.input_layout)
        self.top_layout.addWidget(self.mode_box, alignment=Qt.AlignLeft)
        self.top_layout.setAlignment(Qt.AlignLeft)
        self.main_layout.addLayout(self.top_layout)
        self.process_but = QPushButton('process')
        self.result_line = QLabel('')
        self.main_layout.addWidget(self.process_but, alignment=Qt.AlignLeft)
        self.main_layout.addWidget(self.result_line, alignment=Qt.AlignLeft)
        self.main_layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.main_layout)

    def connections(self):
        self.process_but.clicked.connect(self.process)
        self.back_but.clicked.connect(self.back)
    
    def process(self):
        if self.mode_box.currentText() == 'encode':
            msg = self.input_line.text()
            key = self.key_line.text()
            result = ''
            found = []
            for i in msg:
                if str(key.find(i)) not in found:
                    result += ' ' + str(key.find(i))
                    found.append(str(key.find(i)))
                else:
                    result += ' ' + str(key.find(i, int(found[-1])))
            self.result_line.setText(result)
        else:
            msg = self.input_line.text()
            key = self.key_line.text()
            msg = msg.split(' ')
            result = ''
            for i in msg:
                result += key[int(i)]
            self.result_line.setText(result)

    def back(self):
        self.hide()
        self.parent.show()