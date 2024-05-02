from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit
from settings import *

class utf_window(QWidget):
    def __init__(self, app, parent):
        super().__init__()
        self.parent = parent
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
        self.app = app

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

    def initUI(self):
        self.main_layout = QVBoxLayout()
        self.input_line = QLineEdit()
        self.result_line = QLabel()
        self.encode_but = QPushButton(txt_encode)
        self.decode_but = QPushButton(txt_decode)
        self.copy_to_clip_but = QPushButton(txt_copy)
        self.back = QPushButton(txt_back)
        self.main_layout.addWidget(self.back, alignment=Qt.AlignLeft)
        self.main_layout.addWidget(self.input_line, alignment=Qt.AlignTop)
        self.main_layout.addWidget(self.result_line, alignment=Qt.AlignLeft)
        self.main_layout.addWidget(self.encode_but, alignment=Qt.AlignLeft)
        self.main_layout.addWidget(self.decode_but, alignment=Qt.AlignLeft)
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
        self.parent.show()