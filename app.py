from src import CalculatorWindow

from PyQt5.QtWidgets import QApplication

import sys

app = QApplication(sys.argv)
w = CalculatorWindow()

if __name__ == '__main__':
    w.show()
    app.exec_()