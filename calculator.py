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
        self.nav_text = QLabel("Standart")
        font = QFont()
        font.setPointSize(18)
        self.nav_text.setFont(font)
        self.nav.addWidget(self.nav_text)
        self.history_btn = QPushButton("")
        self.history_btn.setFixedSize(100, 50)
        self.history_btn.setIconSize(QSize(24, 24))

        self.history_btn.setStyleSheet("QPushButton { text-align: left; padding-left: 10px; }")
        self.history_btn.setIcon(QIcon('logo.png'))
        self.nav.addWidget(self.history_btn)

        self.nav_widget = QWidget()
        self.nav_widget.setLayout(self.nav)

