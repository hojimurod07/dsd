from  PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Calc(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setFixedSize(400,640)
        self.navHeader()
        self.setCentralWidget(self.nav_widget)


    def navHeader(self):
        self.nav = QHBoxLayout()
        self.nav_btn = QPushButton(" ")
        self.nav_btn.setFixedSize(70, 50)
        self.nav_btn.setIconSize(QSize(24, 24))
        self.nav_btn.setIcon(QIcon('nav.png'))
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

        self.nav_widget = QWidget()
        self.nav_widget.setLayout(self.nav)

