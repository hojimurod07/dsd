from  PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Calc(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setFixedSize(400,640)
        self.asosiy = QVBoxLayout()

        self.navHeader()
        self.textEdit()
        self.asosiy.addLayout(self.nav)
        self.asosiy.addLayout(self.textArea)

        self.w = QWidget()
        self.w.setLayout(self.asosiy)
        self.setCentralWidget(self.w)



    def navHeader(self):
        self.nav = QHBoxLayout()
        self.nav_btn = QPushButton(" ")
        self.nav_btn.setFixedSize(70, 50)
        self.nav_btn.setIconSize(QSize(24, 24))
        self.nav_btn.setIcon(QIcon('new-tab.png'))
        self.nav.addWidget(self.nav_btn)
        self.nav_text = QLabel("Standart")
        font = QFont()
        font.setPointSize(16)
        self.nav_text.setFont(font)
        self.nav.addWidget(self.nav_text)
        self.history_btn = QPushButton("")
        self.history_btn.setFixedSize(70, 50)
        self.history_btn.setIconSize(QSize(24, 24))

        self.history_btn.setStyleSheet("QPushButton { text-align: left; padding-left: 20px; }")
        self.history_btn.setIcon(QIcon('logo.png'))
        self.nav.addWidget(self.history_btn)



    def textEdit(self):
        self.textArea = QHBoxLayout()

        self.line = QLineEdit()
        self.textArea.addWidget(self.line)
        self.line.setStyleSheet('background : #fffff; color: #000000; font-size: 80px; font-weight: bold; border: none;')
        self.line.setAlignment(Qt.AlignRight)
        # Move the cursor to the end of the text


        # Set a fixed height to make it look more like a calculator
        self.line.setFixedHeight(60)
        self.line.setText("0")
