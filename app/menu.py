from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QSizePolicy
from settings import *
from binary import *
from caesar import *
from omofo import *
from key_caesar import *

app = QApplication([])

class MainMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
        
    def initUI(self):
        self.h_line = QVBoxLayout()
        self.r_line = QHBoxLayout()
        self.h_line.setContentsMargins(20, 20, 20, 20)
        self.but_1 = QPushButton(txt_shif_1)
        self.but_2 = QPushButton(txt_shif_2)
        self.but_3 = QPushButton(txt_shif_3)
        self.but_4 = QPushButton(txt_shif_4)
        self.but_5 = QPushButton(txt_shif_5)
        self.but_1.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.but_2.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.but_3.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.but_4.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.but_5.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        #self.but_6 = QPushButton(txt_shif_6)
        #self.but_7 = QPushButton(txt_shif_7)
        #self.but_8 = QPushButton(txt_shif_8)
        #self.but_9 = QPushButton(txt_shif_9)
        #self.but_10 = QPushButton(txt_shif_10)
        self.h_line.addWidget(self.but_1)
        self.h_line.addWidget(self.but_2)
        self.h_line.addWidget(self.but_3)
        self.h_line.addWidget(self.but_4)
        self.h_line.addWidget(self.but_5)
        #self.h_line.addWidget(self.but_6, alignment=Qt.AlignLeft)
        #self.h_line.addWidget(self.but_7, alignment=Qt.AlignLeft)
        #self.h_line.addWidget(self.but_8, alignment=Qt.AlignLeft)
        #self.h_line.addWidget(self.but_9, alignment=Qt.AlignLeft)
        #self.h_line.addWidget(self.but_10, alignment=Qt.AlignLeft)
        self.r_line.addLayout(self.h_line)
        self.r_line.addWidget(QLabel(txt_manual), alignment=Qt.AlignRight)
        self.setLayout(self.r_line)

    def connects(self):
        self.but_1.clicked.connect(self.UTF_16)
        self.but_2.clicked.connect(self.Caesar_cipher)
        self.but_3.clicked.connect(self.Caesar_with_key)
        self.but_4.clicked.connect(self.Omofo)
        #self.but_5.clicked.connect(self)
        #self.but_6.clicked.connect(self)
        #self.but_7.clicked.connect(self)
        #self.but_8.clicked.connect(self)
        #self.but_9.clicked.connect(self)
        #self.but_10.clicked.connect(self)

    def UTF_16(self):
        self.hide()
        self.window = utf_window(app, self)

    def Caesar_cipher(self):
        self.hide()
        self.window = caesar(app, self)

    def Omofo(self):
        self.hide()
        self.window = omofo(app, self)
    
    def Caesar_with_key(self):
        self.hide()
        self.window = caesar_with_key(app, self)
    

window = MainMenu()
app.exec_()