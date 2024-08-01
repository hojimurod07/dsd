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
        self.buttons_created()
        self.asosiy.addLayout(self.nav)
        self.asosiy.addLayout(self.textArea)
        self.asosiy.addLayout(self.main_buttons)
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

        self.line = QLineEdit("0",self)
        self.textArea.addWidget(self.line)
        self.line.setStyleSheet('background : #fffff; color: #000000; font-size: 80px; font-weight: bold; border: none;')
        self.line.setAlignment(Qt.AlignRight)
        # Move the cursor to the end of the text


        # Set a fixed height to make it look more like a calculator
        self.line.setFixedHeight(60)
        font = self.line.font()
        font.setPointSize(22)
        self.line.setFont(font)
        self.line.setCursorPosition(len(self.line.text()))

    def button_clicked(self):
        current_text = self.line.text()
        button_text = self.sender().text()

        # Replace "0" with the button text if "0" is the only character
        if current_text == '0':
            self.line.setText(button_text)
        else:
            self.line.setText(current_text + button_text)


    def buttons_created(self):

        self.main_buttons = QGridLayout()
        self.main_buttons.setSpacing(10)  # Add spacing between buttons

        # Button labels as they might appear on a calculator
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', 'ln', '+',
            'C', '(', ')', '^',
            'sqrt', '%', 'log', '='
        ]

        # Button styling
        button_style = """
        QPushButton {
            background-color: #404040;  /* Blue color */
            color: white;
            font-size: 18px;
            font-weight: bold;
            border: none;
            border-radius: 5px;  /* Rounded corners */;
           
        }
        QPushButton:pressed {
            background-color: #151515;  /* Darker blue when pressed */
        }
        QPushButton:hover {
            background-color: #151515;  /* Slightly lighter blue when hovered */
        }
        """
        last_button_style = """
        QPushButton {
            background-color: #59C5EC;  /* Orange color */
            color: white;
            font-size: 18px;
            font-weight: bold;
            border: none;
            border-radius: 5px;  /* Rounded corners */
        }
        QPushButton:pressed {
            background-color: #247B9B;  /* Darker orange when pressed */
        }
        QPushButton:hover {
            background-color: #247B9B;  /* Lighter orange when hovered */
        }
        """
        button_objects = []
        # Create and add buttons to the grid layout
        row = 0
        col = 0
        for i, text in enumerate(buttons):
            button = QPushButton(text, self)
            button.setFixedSize(95, 65)  # Slightly larger buttons for a better look
            button.setStyleSheet(button_style)
            self.main_buttons.addWidget(button, row, col)
            button_objects.append(button)
            col += 1
            if col > 3:  # 4 buttons per row
                col = 0
                row += 1
        button_objects[-1].setStyleSheet(last_button_style)




