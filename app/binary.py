from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit
from settings import *

class binary(QWidget):
    def __init__(self, app):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
        self.app = app
    def set_appear(self):
        self.setWindowTitle(Title)
        self.resize(win_x, win_y)
        self.move(x, y)

    def initUI(self):
        self.main_layout = QVBoxLayout()
        self.input_line = QLineEdit()
        self.result_line = QLabel()
        self.encode_but = QPushButton('encode')
        self.decode_but = QPushButton('decode')
        self.copy_to_clip_but = QPushButton('copy to clipboard')
        self.main_layout.addWidget(self.input_line, alignment=Qt.AlignLeft)
        self.main_layout.addWidget(self.result_line, alignment=Qt.AlignLeft)
        self.main_layout.addWidget(self.encode_but, alignment=Qt.AlignLeft)
        self.main_layout.addWidget(self.decode_but, alignment=Qt.AlignLeft)
        self.main_layout.addWidget(self.copy_to_clip_but, alignment=Qt.AlignLeft)
        self.setLayout(self.main_layout)

    def connects(self):
        self.encode_but.clicked.connect(self.encode)
        self.decode_but.clicked.connect(self.decode)
        self.copy_to_clip_but.clicked.connect(self.copy)
    
    def encode(self):
        n = self.input_line.text()
        self.result_line.setText(''.join([format(ord(i), '08b') for i in n]))
    
    def decode(self):
        try:
            n = self.input_line.text()
            self.result_line.setText(''.join(chr(int(n[i:i+8], 2)) for i in range(0, len(n), 8)))
        except:
            self.result_line.setText('ошибка')

    def copy(self):
        c = self.app.clipboard()
        c.setText(self.result_line.text())

app = QApplication([])

b = binary(app)
app.exec_()