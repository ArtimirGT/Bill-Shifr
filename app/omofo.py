from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit, QComboBox
from settings import *

class omofo(QWidget):
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
        self.input_line = QLineEdit()
        self.key_line = QLineEdit()
        self.mode_box = QComboBox()
        self.mode_box.addItems([txt_encode, txt_decode])
        self.input_layout.addWidget(self.back_but, alignment=Qt.AlignLeft)
        self.input_layout.addWidget(self.input_line, alignment=Qt.AlignTop)
        self.input_layout.addWidget(self.key_line, alignment=Qt.AlignLeft)
        self.top_layout.addLayout(self.input_layout)
        #self.top_layout.addWidget(self.mode_box, alignment=Qt.AlignLeft)
        self.top_layout.setAlignment(Qt.AlignLeft)
        self.main_layout.addLayout(self.top_layout)
        self.process_but = QPushButton(txt_process)
        self.result_line = QLabel('')
        self.choice_layout.addWidget(self.mode_box, alignment=Qt.AlignLeft)
        self.choice_layout.addWidget(self.process_but, alignment=Qt.AlignLeft)
        self.choice_layout.setAlignment(Qt.AlignLeft)
        self.main_layout.addLayout(self.choice_layout)
        self.main_layout.addWidget(self.result_line, alignment=Qt.AlignLeft)
        self.copy_but = QPushButton(txt_copy)
        self.main_layout.addWidget(self.copy_but, alignment=Qt.AlignLeft)
        self.main_layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.main_layout)

    def connections(self):
        self.process_but.clicked.connect(self.process)
        self.back_but.clicked.connect(self.back)
        self.copy_but.clicked.connect(self.copy)
    
    def process(self):
        if self.mode_box.currentText() == txt_encode:
            msg = self.input_line.text()
            key = self.key_line.text()
            result = ''
            found = []
            for i in msg:
                if str(key.find(i)) not in found:
                    result += ' ' + str(key.find(i))
                    found.append(str(key.find(i)))
                else:
                    result += ' ' + str(key.find(i, int(found[-1])+1))
                    found.append(str(key.find(i, int(found[-1])+1)))
            self.result_line.setText(result)
        else:
            msg = self.input_line.text()
            if msg[0] == ' ':
                msg = msg.replace(' ', '', 1)
            key = self.key_line.text()
            msg = msg.split(' ')
            result = ''
            try:
                for i in msg:
                    result += key[int(i)]
                self.result_line.setText(result)
            except:
                self.result_line.setText(txt_error)

    def copy(self):
        c = self.app.clipboard()
        c.setText(self.result_line.text())

    def back(self):
        self.hide()
        self.parent.move(self.x(), self.y())
        self.parent.resize(self.width(), self.height())
        self.parent.show()