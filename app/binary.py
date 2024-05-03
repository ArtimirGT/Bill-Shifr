from PyQt5.QtCore import Qt, QSettings
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit
from settings import *

class utf_window(QWidget):
    def __init__(self, app, parent, state):
        super().__init__()
        self.win_x = state[0]
        self.win_y = state[1]
        self.win_height = state[2]
        self.win_width = state[3]
        self.parent = parent
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
        self.app = app

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(self.win_width, self.win_height)
        self.move(self.win_x, self.win_y)

    def initUI(self):
        self.main_layout = QVBoxLayout()
        self.choice_layout = QHBoxLayout()
        self.input_line = QLineEdit()
        self.result_line = QLabel()
        self.encode_but = QPushButton(txt_encode)
        self.decode_but = QPushButton(txt_decode)
        self.copy_to_clip_but = QPushButton(txt_copy)
        self.back = QPushButton(txt_back)
        self.main_layout.addWidget(self.back, alignment=Qt.AlignLeft)
        self.main_layout.addWidget(self.input_line, alignment=Qt.AlignTop)
        #self.main_layout.addWidget(self.encode_but, alignment=Qt.AlignLeft)
        #self.main_layout.addWidget(self.decode_but, alignment=Qt.AlignLeft)
        self.choice_layout.addWidget(self.encode_but, alignment=Qt.AlignLeft)
        self.choice_layout.addWidget(self.decode_but, alignment=Qt.AlignLeft)
        self.choice_layout.setAlignment(Qt.AlignLeft)
        self.main_layout.addLayout(self.choice_layout)
        self.main_layout.addWidget(self.result_line, alignment=Qt.AlignLeft)
        self.main_layout.addWidget(self.copy_to_clip_but, alignment=Qt.AlignLeft)
        self.main_layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.main_layout)

    def connects(self):
        self.back.clicked.connect(self.MainMenu)
        self.encode_but.clicked.connect(self.encode)
        self.decode_but.clicked.connect(self.decode)
        self.copy_to_clip_but.clicked.connect(self.copy)
    
    def encode(self):
        n = self.input_line.text()
        r = ''.join([format(ord(i), '016b') for i in n])
        while '  ' in r:
            r = r.replace('  ', ' ', 1)
        r = r.replace(' ', '', 1)
        self.result_line.setText(r)
    
    def decode(self):
        try:
            n = self.input_line.text()
            n = n.replace(' ', '')
            while ' 0' in n:
                n = n.replace(' 0', ' ')
            self.result_line.setText(''.join(chr(int(n[i:i+16], 2)) for i in range(0, len(n), 16)))
        except:
            self.result_line.setText(txt_error)

    def copy(self):
        c = self.app.clipboard()
        c.setText(self.result_line.text())

    def MainMenu(self):
        self.hide()
        self.parent.move(self.x(), self.y())
        self.parent.resize(self.width(), self.height())
        self.parent.show()