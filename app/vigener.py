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
        self.process_but = QPushButton('process')
        self.input_layout.addWidget(self.process_but, alignment=Qt.AlignLeft)
        self.top_layout.addLayout(self.input_layout)
        self.top_layout.addWidget(self.encoding_box, alignment = Qt.AlignLeft)
        self.main_layout.addLayout(self.top_layout)
        self.word_line = QLabel('')
        self.main_layout.addWidget(self.word_line, alignment=Qt.AlignLeft)
        self.copy_but = QPushButton('copy')
        self.main_layout.addWidget(self.copy_but, alignment=Qt.AlignLeft)
        self.main_layout.setAlignment(Qt.AlignTop)
        self.top_layout.setAlignment(Qt.AlignLeft)
        self.setLayout(self.main_layout)

    def connects(self):
        self.copy_but.clicked.connect(self.copy)
        self.back_but.clicked.connect(self.back)
        self.process_but.clicked.connect(self.encode_decode)

    def form_dict(self):
        d = {}
        iter = 0
        for i in range(0,127):
            d[iter] = chr(i)
            iter = iter +1
        return d

    def encode_val(self, word):
        list_code = []
        lent = len(word)
        d = self.form_dict() 
        for w in range(lent):
            for value in d:
                if word[w] == d[value]:
                    list_code.append(value) 
        return list_code
    
    def comparator(self, value, key):
    len_key = len(key)
    dic = {}
    iter = 0
    full = 0

    for i in value:
        dic[full] = [i,key[iter]]
        full = full + 1
        iter = iter +1
        if (iter >= len_key):
            iter = 0 
    return dic

    def full_encode(self, value, key):
    dic = self.comparator(value, key)
    lis = []
    d = self.form_dict()

    for v in dic:
        go = (dic[v][0]+dic[v][1]) % len(d)
        lis.append(go) 
    return lis

def decode_val(self, list_in):
    list_code = []
    lent = len(list_in)
    d = self.form_dict() 

    for i in range(lent):
        for value in d:
            if list_in[i] == value:
               list_code.append(d[value]) 
    return list_code

    def encode_decode(self):
        self.message = self.input_line.text().upper()
        self.key = self.step_line.text().upper()
        self.answer = ''
        self.encoding = self.encoding_box.currentText()
        if self.encoding == 'encode':
            self.form_dict()
            en_mes = self.encode_val(self.message)
            en_key = self.encode_val(self.key)

                # Возвращает закодированное слово и ключ
        else:
            pass
                # Возвращает закодированное слово
    def copy(self):
        c1 = self.app.clipboard()
        c2 = self.app.clipboard()
        c1.setText(self.word_line.text())
        c2.setText(self.key_line.text())

    def back(self):
        self.hide()
        self.parent.show()

    def check(self):
        print(self.encoding_box.currentText())

app = QApplication([])
window = VigenerCipher()
app.exec_()