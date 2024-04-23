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
        pass

    def connections(self):
        pass
