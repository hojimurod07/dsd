
from PyQt5.QtWidgets import *
from  calculator import *

app  = QApplication([])

a = Calc()
a.show()

app.exec_()